##############################################################
# NLP - Information Extraction from Excel files to Smart One #
##############################################################

##############################
# 1. Importing the libraries #
##############################
import pandas as pd
import re
from abc import ABC
from smart_one_scripts.Process import Process


###########################################################
# Class responsible for processing Notebooks' data sheets #
###########################################################
class ProcessNotebook(Process, ABC):

    def __init__(self, xlsx_file):
        self.__cols_to_remove = ["3g4g", "fingerprint", "videomemory", "gsync", "emmcissd",
                                 "howtoupgradememory", "totalsystemmemory", "replaceablebattery",
                                 "rearfacingcamera", "worldfacingcamera", "bundledperipherals",
                                 "lcdcovermaterial", "topcasematerial", "bottomcasematerial",
                                 "expansionslotincludesused"]
        self.__series_sheet = Process.extract_data_from_sheet(xlsx_file, self.__cols_to_remove)

    def get_sheet(self):
        return self.__series_sheet.copy()

    def _Process__get_dimensions(self):
        # Normalizing the features.
        if "dimensioncm" in self.__series_sheet and pd.notnull(self.__series_sheet.dimensioncm):
            self.__series_sheet["dimensionwxdxh"] = self.__series_sheet.dimensioncm \
                if "dimensionwxdxh" not in self.__series_sheet or pd.isnull(self.__series_sheet.dimensionwxdxh) \
                else self.__series_sheet.dimensionwxdxh
        if "dimension" in self.__series_sheet and pd.notnull(self.__series_sheet.dimension):
            self.__series_sheet["dimensionwxdxh"] = self.__series_sheet.dimension \
                if "dimensionwxdxh" not in self.__series_sheet or pd.isnull(self.__series_sheet.dimensionwxdxh) else \
                    self.__series_sheet.dimensionwxdxh
        if "dimensionwxdxh" in self.__series_sheet and pd.notnull(self.__series_sheet.dimensionwxdxh):
            self.__series_sheet["dimensionwxdxh"] = [sb for sb in self.__series_sheet.dimensionwxdxh.split("\n")
                                                     if "cm" in sb][0]
            self.__series_sheet.dimensionwxdxh = re.sub(r"\(\w\)", "",
                                                        Process.clean_text(self.__series_sheet.dimensionwxdxh)).strip()
            self.__series_sheet.dimensionwxdxh = [sb.strip()
                                                  for sb in self.__series_sheet.dimensionwxdxh.replace(
                                                        "cm", "").split("x")]
            if "~" in self.__series_sheet.dimensionwxdxh[2] and "~" not in self.__series_sheet.dimensionwxdxh[1]:
                self.__series_sheet.dimensionwxdxh[1:] = reversed(self.__series_sheet.dimensionwxdxh[1:])
            self.__series_sheet.dimensionwxdxh = f"{self.__series_sheet.dimensionwxdxh[0]} x " \
                                                 f"{self.__series_sheet.dimensionwxdxh[2]} x " \
                                                 f"{self.__series_sheet.dimensionwxdxh[1]}"
            self.__series_sheet["dimensionwxhxd"] = self.__series_sheet.dimensionwxdxh \
                if "dimensionwxhxd" not in self.__series_sheet or pd.isnull(self.__series_sheet.dimensionwxhxd) \
                    else self.__series_sheet.dimensionwxhxd

        # Extracting the "Product Dimension" information.
        if "dimensionwxhxd" in self.__series_sheet and pd.notnull(self.__series_sheet.dimensionwxhxd):
            self.__series_sheet["product_dimension"] = dict(zip(
                ["Width", "Lenght", "Height"],
                [sb.strip() for sb in self.__series_sheet.dimensionwxhxd.replace("cm", "").split("x")]))
        else:
            self.__series_sheet["product_dimension"] = {"Width": None, "Lenght": None, "Height": None}

        # Removing the unnecessary columns.
        self.__series_sheet.drop(labels=["dimensioncm", "dimension", "dimensionwxdxh", "dimensionwxhxd"],
                 inplace=True, errors="ignore")

    def _Process__get_memory(self):
        result = dict()
        # Extracting the "Slots" information.
        if "memoryslot" in self.__series_sheet:
            result["Slots"] = re.search(r"\d+", self.__series_sheet.memoryslot).group() \
                if pd.notnull(self.__series_sheet.memoryslot) else "-"

        # Extracting the "Max Memory Off-Board".
        if "memorymax" in self.__series_sheet:
            result["Max Memory Off-Board"] = re.search(r"\d+", self.__series_sheet.memorymax).group() \
                if pd.notnull(self.__series_sheet.memorymax) else "-"

        # Extracting the information.
        if "onboardmemory" in self.__series_sheet or "dimmmemory" in self.__series_sheet:
            # Extracting the "Type" information.
            result["Type"] = re.search(r"[\d\w]*DDR[\d\w]+", self.__series_sheet.onboardmemory \
                if "onboardmemory" in self.__series_sheet and pd.notnull(self.__series_sheet.onboardmemory) \
                else self.__series_sheet.dimmmemory \
                if "dimmmemory" in self.__series_sheet and pd.notnull(self.__series_sheet.dimmmemory) \
                else "DDR_INVALID").group()
            result["Type"] = "UNKNOWN" if result["Type"] == "DDR_INVALID" else result["Type"]

            # Extracting the "Clock" information.
            result["Clock"] = [c for c in re.findall(r"{}-?(\d+)?".format(result["Type"]),
                                    f"{self.__series_sheet.onboardmemory} {self.__series_sheet.dimmmemory}" \
                                    if ("onboardmemory" in self.__series_sheet and
                                        pd.notnull(self.__series_sheet.onboardmemory) and
                                        "dimmmemory" in self.__series_sheet and
                                        pd.notnull(self.__series_sheet.dimmmemory)) else \
                                    self.__series_sheet.onboardmemory \
                                    if ("onboardmemory" in self.__series_sheet and
                                        pd.notnull(self.__series_sheet.onboardmemory) and
                                        ("dimmmemory" not in self.__series_sheet or
                                         pd.isnull(self.__series_sheet.dimmmemory))) else \
                                    self.__series_sheet.dimmmemory \
                                    if ("dimmmemory" in self.__series_sheet and
                                        pd.notnull(self.__series_sheet.dimmmemory) and
                                        ("onboardmemory" not in self.__series_sheet or
                                         pd.isnull(self.__series_sheet.onboardmemory))) else "") if c]
            result["Clock"] = list(set(result["Clock"]))[0] if len(result["Clock"]) > 0 else "-"

        # Extracting the "Total Off-Board" information.
        if "dimmmemory" in self.__series_sheet and pd.notnull(self.__series_sheet.dimmmemory):
            self.__series_sheet.dimmmemory = self.__series_sheet.dimmmemory.replace(
                result["Type"] if result["Type"] != "-" else "", "")
            self.__series_sheet.dimmmemory = self.__series_sheet.dimmmemory.replace(
                result["Clock"] if result["Clock"] != "-" else "", "")
            result["Total Off-Board"] = re.search(r"\d+", self.__series_sheet.dimmmemory).group() \
                if pd.notnull(self.__series_sheet.dimmmemory) else "-"
        else:
            result["Total Off-Board"] = "-"

        # Extracting the "Total On-Board" information.
        if "onboardmemory" in self.__series_sheet and pd.notnull(self.__series_sheet.onboardmemory):
            self.__series_sheet.onboardmemory = self.__series_sheet.onboardmemory.replace(
                result["Type"] if result["Type"] != "-" else "", "")
            self.__series_sheet.onboardmemory = self.__series_sheet.onboardmemory.replace(
                result["Clock"] if result["Clock"] != "-" else "", "")
            result["Total On-Board"] = re.search(r"\d+", self.__series_sheet.onboardmemory).group() \
                if pd.notnull(self.__series_sheet.onboardmemory) else "-"
        else:
            result["Total On-Board"] = "-"

        # Removing the unnecessary columns.
        self.__series_sheet.drop(labels=["memoryslot", "memorymax", "onboardmemory", "dimmmemory"],
                                 inplace=True, errors="ignore")
        self.__series_sheet["product_memory"] = result

    def _Process__get_weight(self):
        result = dict()
        # Normalizing the content.
        if "weight" in self.__series_sheet and pd.notnull(self.__series_sheet.weight):
            self.__series_sheet.weight = self.__series_sheet.weight.split("\n")[0].lower().strip()
            self.__series_sheet["weightwithbattery"] = self.__series_sheet.weight \
                if "weightwithbattery" not in self.__series_sheet or pd.isnull(self.__series_sheet.weightwithbattery) \
                    else self.__series_sheet.weightwithbattery
        if "weightkg" in self.__series_sheet and pd.notnull(self.__series_sheet.weightkg):
            self.__series_sheet.weightkg = tuple(sorted(list(
                re.findall(r"\d+\.?\d+\s?kg", self.__series_sheet.weightkg.lower()))))
            self.__series_sheet["weightwithoutbattery"] = self.__series_sheet.weightkg[0] \
                if "weightwithoutbattery" not in self.__series_sheet or pd.isnull(
                    self.__series_sheet.weightwithoutbattery) else self.__series_sheet.weightwithoutbattery
            self.__series_sheet["weightwithbattery"] = self.__series_sheet.weightkg[1] \
                if "weightwithbattery" not in self.__series_sheet or pd.isnull(self.__series_sheet.weightwithbattery) \
                    else self.__series_sheet.weightwithbattery
        if "weightwithoutbattery" in self.__series_sheet and "weightwithbattery" in self.__series_sheet:
            result["With Battery"] = re.sub(r"\s*kg", "", self.__series_sheet.weightwithbattery).strip() \
                if pd.notnull(self.__series_sheet.weightwithbattery) else "-"
            result["Without Battery"] = re.sub(r"\s*kg", "", self.__series_sheet.weightwithoutbattery).strip() \
                if pd.notnull(self.__series_sheet.weightwithoutbattery) else "-"

        # Removing the unnecessary columns.
        self.__series_sheet.drop(labels=["weight", "weightkg", "weightwithoutbattery", "weightwithbattery"],
                                 inplace=True, errors="ignore")
        self.__series_sheet["product_weight"] = result

    def _Process__get_power_adapter(self):
        result = dict()
        if "power" in self.__series_sheet and pd.notnull(self.__series_sheet.power):
            self.__series_sheet.acadapter = self.__series_sheet.power \
                if "acadapter" not in self.__series_sheet or pd.isnull(self.__series_sheet.acadapter) \
                    else self.__series_sheet.acadapter
        if pd.notnull(self.__series_sheet.acadapter):
            self.__series_sheet.acadapter = re.sub("\n", ", ", self.__series_sheet.acadapter)
            # Extracting the information about "Power Adapter".
            result["Power Adapter"] = re.search("(.*)Output", self.__series_sheet.acadapter).groups()[0]
            self.__series_sheet.acadapter = self.__series_sheet.acadapter.replace(result["Power Adapter"], "")
            result["Power Adapter"] = dict(zip(["AC", "Description"],
                                               [i.strip() for i in result["Power Adapter"].strip().split(",") if i]))
            groups = re.search(r"(\d+\.?\d*)", result["Power Adapter"]["AC"])
            if groups:
                result["Power Adapter"]["AC"] = groups.group()

            # Extracting the information about "Power Adapter Input/Output".
            result["Power Adapter Output"] = re.search("(Output:.*)Input", self.__series_sheet.acadapter).groups()[0]
            result["Power Adapter Input"] = self.__series_sheet.acadapter.replace(result["Power Adapter Output"], "")
            result["Power Adapter Output"] = result["Power Adapter Output"].replace(
                "Output:", "").strip()
            result["Power Adapter Output"] = dict(
                zip(["DC", "Ampere", "Watts"], [re.search("\d+\.?\d*", i.strip()).group()
                                                for i in result["Power Adapter Output"].split(",")
                                                if i]))
            result["Power Adapter Input"] = re.search("(Input.*)",
                                                      result["Power Adapter Input"]).groups()[0]
            result["Power Adapter Input"] = result["Power Adapter Input"].replace(
                "Input:", "").replace("universal", "").strip()
            result["Power Adapter Input"] = dict(
                zip(["AC", "Hz"], [re.search("\d+[/~\-]?\d*\s*(ghz)?", i, flags=re.IGNORECASE).group()
                                   for i in result["Power Adapter Input"].split("AC")]))
            result["Power Adapter Input"]["Hz"] = Process.convert_to_hz(result["Power Adapter Input"]["Hz"])

        if pd.notnull(self.__series_sheet.battery):
            # Extracting the information about "Battery Life".
            result["Battery Life"] = re.search("\d+WHr", self.__series_sheet.battery).group()

            # Extracting the information about "Battery".
            result["Battery"] = dict(zip(
                ["Ampere", "Cells"], re.findall(r"(\d+\s?mAh)?.*(\d+).cell", self.__series_sheet.battery)[0]))
            result["Battery"]["Ampere"] = re.sub("\D+", "", result["Battery"]["Ampere"]) \
                if result["Battery"]["Ampere"] else "-"

        # Removing the unnecessary columns.
        self.__series_sheet.drop(labels=["acadapter", "battery", "power"], inplace=True, errors="ignore")
        self.__series_sheet["product_power_adapter"] = result

    def _Process__get_screen(self):
        result = dict()
        # Extracting the value of several other features from the unique feature.
        if "display" in self.__series_sheet and pd.notnull(self.__series_sheet.display):
            temp = re.search(r"(\d+\s?x\s?\d+)", self.__series_sheet.display)
            if temp:
                self.__series_sheet.display = self.__series_sheet.display.replace(temp.group(), f"({temp.group()})")
            self.__series_sheet.display = self.__series_sheet.display.split("//")
            self.__series_sheet.panelsize = self.__series_sheet.display[0]
            for feature, pos in zip(["brightness", "resolution", "glare", "colorgamut"],
                                    range(2, len(self.__series_sheet.display))):
                self.__series_sheet[feature] = self.__series_sheet.display[pos]

        # Extracting the "Brightness" information.
        result["Brightness"] = re.sub("nits", "", self.__series_sheet.brightness).strip() \
            if "brightness" in self.__series_sheet and pd.notnull(self.__series_sheet.brightness) else None

        # Extracting the "Size" information.
        result["Size"] = re.sub(r"(-inch|')", "", self.__series_sheet.panelsize).strip() \
            if pd.notnull(self.__series_sheet.panelsize) else None

        # Extracting the "Touch Screen" information.
        if "touchpanel" in self.__series_sheet and pd.notnull(self.__series_sheet.touchpanel):
            result["Touch Screen"] = True if "non-touch" not in self.__series_sheet.touchpanel.lower() else False
        else:
            result["Touch Screen"] = False

        # Extracting the "Screen to Body Ratio" information.
        result["Screen to Body Ratio"] = re.sub(u"\xa0", "", self.__series_sheet.screentobodyratio).replace(
            " ", "").strip() if "screentobodyratio" in self.__series_sheet and \
                                pd.notnull(self.__series_sheet.screentobodyratio) else None

        # Extracting the "Resolution" information.
        if pd.notnull(self.__series_sheet.resolution):
            result["Resolution"] = dict()
            # Extracting the Description of Resolution.
            groups = re.search(r"([\s\d\w\.]+).+", self.__series_sheet.resolution)
            if groups:
                result["Resolution"]["Description"] = groups.groups()[0].strip()
                self.__series_sheet.resolution = self.__series_sheet.resolution.replace(groups.groups()[0], "").strip()
            else:
                result["Resolution"]["Description"] = None

            # Extracting the Dimensions of Resolution.
            groups = re.search(r"\((\d+\s*x\s*\d+)?.*\)", self.__series_sheet.resolution, flags=re.IGNORECASE)
            groups = [i.strip() for i in groups.groups()[0].split("x")] if groups else [None] * 2
            result["Resolution"] = {**result["Resolution"], **dict(zip(["Width", "Height"], groups))}
        else:
            result["Resolution"] = None

        # Extracting the "Type" information.
        result["Type"] = dict()
        if "paneltech" in self.__series_sheet and pd.notnull(self.__series_sheet.paneltech):
            self.__series_sheet["ipslevel"] = self.__series_sheet.paneltech \
                if "ipslevel" not in self.__series_sheet or pd.isnull(self.__series_sheet.ipslevel) \
                    else self.__series_sheet.ipslevel
        if "pantonevalidated" in self.__series_sheet and pd.notnull(self.__series_sheet.pantonevalidated):
            self.__series_sheet["pantone"] = "Pantone Validated" \
                if self.__series_sheet.pantonevalidated.lower() == "yes" and \
                    ("pantone" not in self.__series_sheet or pd.isnull(self.__series_sheet.pantone)) \
                else self.__series_sheet.pantone
        if "antiglare" in self.__series_sheet and pd.notnull(self.__series_sheet.antiglare):
            self.__series_sheet["glare"] = self.__series_sheet.antiglare \
                if "glare" not in self.__series_sheet or pd.isnull(self.__series_sheet.glare) \
                    else self.__series_sheet.glare
        if "resolution" in self.__series_sheet and pd.notnull(self.__series_sheet.resolution) and \
                ("oled" not in self.__series_sheet or pd.isnull(self.__series_sheet.oled)):
            self.__series_sheet["oled"] = "OLED" if "oled" in self.__series_sheet.resolution.lower() else None
        if "responsetimeg2g" in self.__series_sheet and pd.notnull(self.__series_sheet.responsetimeg2g):
            self.__series_sheet["responsetime"] = self.__series_sheet.responsetimeg2g \
                if "responsetime" not in self.__series_sheet or pd.isnull(self.__series_sheet.responsetime) \
                    else self.__series_sheet.responsetime
        if "colorgamut" in self.__series_sheet and pd.notnull(self.__series_sheet.colorgamut):
            self.__series_sheet.colorgamut = re.sub(r"color gamut", "", self.__series_sheet.colorgamut.lower()).strip()
            if re.search(r"^\d+", self.__series_sheet.colorgamut):
                self.__series_sheet.colorgamut = f"{self.__series_sheet.colorgamut.split()[1]}: " \
                                                 f"{self.__series_sheet.colorgamut.split()[0]}"
            else:
                self.__series_sheet.colorgamut = f"{self.__series_sheet.colorgamut.split()[0]}: " \
                                                 f"{self.__series_sheet.colorgamut.split()[1]}"
            self.__series_sheet.colorgamut = re.sub(r":+", ":", self.__series_sheet.colorgamut.lower()).strip()
            self.__series_sheet["ntsc"] = self.__series_sheet.colorgamut.split(":")[1].strip() \
                if "ntsc" in self.__series_sheet.colorgamut.lower() and \
                   ("ntsc" not in self.__series_sheet or pd.isnull(self.__series_sheet.ntsc)) \
                else self.__series_sheet.ntsc if "ntsc" in self.__series_sheet else None
            self.__series_sheet["srgb"] = self.__series_sheet.colorgamut.split(":")[1].strip() \
                if "srgb" in self.__series_sheet.colorgamut.lower() and \
                   ("srgb" not in self.__series_sheet or pd.isnull(self.__series_sheet.srgb)) \
                else self.__series_sheet.srgb if "srgb" in self.__series_sheet else None
            self.__series_sheet["dcip3"] = self.__series_sheet.colorgamut.split(":")[1].strip() \
                if "dci-p3" in self.__series_sheet.colorgamut.lower() and \
                    ("dcip3" not in self.__series_sheet or pd.isnull(self.__series_sheet.dcip3)) \
                else self.__series_sheet.dcip3 if "dcip3" in self.__series_sheet else None
        result["Type"]["ISP-level"] = self.__series_sheet.ipslevel.replace("Panel", "").replace("Value", "").strip() \
            if "ipslevel" in self.__series_sheet and pd.notnull(self.__series_sheet.ipslevel) else None
        result["Type"]["Glare"] = re.sub("display", "", self.__series_sheet.glare).strip().title() \
            if "glare" in self.__series_sheet and pd.notnull(self.__series_sheet.glare) else None
        result["Type"]["Backlit"] = self.__series_sheet.backlit.strip() \
            if "backlit" in self.__series_sheet and pd.notnull(self.__series_sheet.backlit) else None
        result["Type"]["Oled"] = self.__series_sheet.oled.strip() \
            if "oled" in self.__series_sheet and pd.notnull(self.__series_sheet.oled) else None
        result["Type"]["Pantone"] = Process.clean_text(self.__series_sheet.pantone.title().strip(), False) \
            if "pantone" in self.__series_sheet and pd.notnull(self.__series_sheet.pantone) else None
        result["Type"]["Refresh Rate"] = re.sub(
            "refresh rate", "", self.__series_sheet.refreshrate, flags=re.IGNORECASE).strip() \
            if "refreshrate" in self.__series_sheet and pd.notnull(self.__series_sheet.refreshrate) else None
        result["Type"]["Response Time"] = re.sub(
            "response time", "", self.__series_sheet.responsetime.lower()).strip() \
                if "responsetime" in self.__series_sheet and pd.notnull(self.__series_sheet.responsetime) else None
        result["Type"]["NTSC Percent"] = self.__series_sheet.ntsc.strip() \
            if "ntsc" in self.__series_sheet and pd.notnull(self.__series_sheet.ntsc) else None
        result["Type"]["sRGB Percent"] = self.__series_sheet.srgb.strip() \
            if "srgb" in self.__series_sheet and pd.notnull(self.__series_sheet.srgb) else None
        result["Type"]["Adobe RGB Percent"] = self.__series_sheet.adobe.strip() \
            if "adobe" in self.__series_sheet and pd.notnull(self.__series_sheet.adobe) else None
        result["Type"]["DCI-P3 Percent"] = self.__series_sheet.dcip3.strip() \
            if "dcip3" in self.__series_sheet and pd.notnull(self.__series_sheet.dcip3) else None

        # Removing the unnecessary columns.
        self.__series_sheet.drop(index=["brightness", "panelsize", "touchpanel", "screentobodyratio", "ipslevel",
                                        "pantone", "glare", "backlit", "oled", "refreshrate", "responsetimeg2g",
                                        "ntsc", "srgb", "adobe", "dcip3", "resolution", "paneltech", "responsetime",
                                        "pantonevalidated", "antiglare", "colorgamut", "display"],
                                 inplace=True, errors="ignore")
        self.__series_sheet["product_screen"] = result

    def _Process__get_network_connectivity(self):
        result = dict()
        # Normalizing features.
        if "onboardwireless" in self.__series_sheet and pd.notnull(self.__series_sheet.onboardwireless):
            self.__series_sheet["wireless"] = self.__series_sheet.onboardwireless \
                if "wireless" not in self.__series_sheet or pd.isnull(self.__series_sheet.wireless) \
                    else self.__series_sheet.wireless
        if "wirelessmodule" in self.__series_sheet and pd.notnull(self.__series_sheet.wirelessmodule):
            self.__series_sheet["wireless"] = self.__series_sheet.wirelessmodule \
                if "wireless" not in self.__series_sheet or pd.isnull(self.__series_sheet.wireless) \
                    else self.__series_sheet.wireless
        if "wifibluetooth" in self.__series_sheet and pd.notnull(self.__series_sheet.wifibluetooth):
            self.__series_sheet["wireless"] = self.__series_sheet.wifibluetooth \
                if "wireless" not in self.__series_sheet or pd.isnull(self.__series_sheet.wireless) \
                    else self.__series_sheet.wireless

        # Normalizing the content of "wireless" content.
        self.__series_sheet.wireless = self.__series_sheet.wireless.replace(
            "802.11ax+Bluetooth 5.0", "Wi-Fi 6(Gig+)(802.11ax)+Bluetooth 5.0").strip()
        self.__series_sheet.wireless = re.sub("Intel", "", self.__series_sheet.wireless).strip()
        self.__series_sheet.wireless = Process.clean_text(self.__series_sheet.wireless).strip()
        self.__series_sheet.wireless = self.__series_sheet.wireless.split("+")
        if len(self.__series_sheet.wireless) > 2:
            self.__series_sheet.wireless = ["+".join(self.__series_sheet.wireless[:-1]).strip(),
                                            self.__series_sheet.wireless[-1].strip()]
        else:
            self.__series_sheet.wireless = [sb.strip() for sb in self.__series_sheet.wireless]

        # Extracting the "Connectivity" information.
        self.__series_sheet["product_connectivity"] = re.search(
            r"bluetooth\s?(\d+\.?\d*)",
            Process.clean_text(self.__series_sheet.wireless[-1], False),
            flags=re.IGNORECASE)
        self.__series_sheet.wireless = self.__series_sheet.wireless[0]
        if pd.notnull(self.__series_sheet.product_connectivity):
            self.__series_sheet.product_connectivity = {"Bluetooth Version":
                                                            self.__series_sheet.product_connectivity.groups()[0]}

        # Extracting the "Wireless Network" information.
        result["Wireless Network"] = dict()
        result["Wireless Network"]["Type"] = self.__series_sheet.wireless.strip() \
            if pd.notnull(self.__series_sheet.wireless) else None
        result["Wireless Network"]["Specification"] = re.search(r"wi-fi \d+\w?", self.__series_sheet.wireless,
                                                                flags=re.IGNORECASE)
        if pd.notnull(result["Wireless Network"]["Specification"]):
            result["Wireless Network"]["Specification"] = result["Wireless Network"]["Specification"].group()

        # Extracting the "Ethernet Network" information.
        result["Ethernet Network"] = dict()
        result["Ethernet Network"]["Type"] = self.__series_sheet.lan.strip() \
            if "lan" in self.__series_sheet and pd.notnull(self.__series_sheet.lan) else None

        # Removing the unnecessary columns.
        self.__series_sheet.drop(index=["onboardwireless", "wirelessmodule", "wifibluetooth",
                                        "lan", "wireless"], inplace=True, errors="ignore")
        self.__series_sheet["product_network"] = result

    def _Process__get_keyboard(self):
        result = dict()
        if pd.notnull(self.__series_sheet.keyboardtype):
            # Extracting the "BackLit Keyboard" information.
            result["BackLit Keyboard"] = True if "backlit" in self.__series_sheet.keyboardtype.lower() else False
            self.__series_sheet.keyboardtype = re.sub("backlit", "", self.__series_sheet.keyboardtype,
                                                      flags=re.IGNORECASE).strip()

            # Extracting the "Keyboard" information.
            result["Keyboard"] = Process.clean_text(
                re.split("keyboard", self.__series_sheet.keyboardtype, flags=re.IGNORECASE)[0]).strip()
        else:
            result["BackLit Keyboard"] = False
            result["Keyboard"] = None

        # Removing the unnecessary columns.
        self.__series_sheet.drop(index=["keyboardtype"], inplace=True, errors="ignore")
        self.__series_sheet["product_keyboard"] = result

    def _Process__get_in_box(self):
        result = dict()
        # Normalizing the features.
        for feature in ["additionalaccessories", "suppliedaccessories"]:
            if feature in self.__series_sheet and pd.notnull(self.__series_sheet[feature]):
                self.__series_sheet["includedinthebox"] = Process.clean_text(self.__series_sheet[feature]) \
                    if "includedinthebox" not in self.__series_sheet or pd.isnull(self.__series_sheet.includedinthebox) \
                    else f"{self.__series_sheet.includedinthebox.strip()}\n" \
                         f"{Process.clean_text(self.__series_sheet[feature]).strip()}"

        # Extracting the "In Box" information.
        result["In Box"] = self.__series_sheet.includedinthebox.strip() \
            if "includedinthebox" in self.__series_sheet and pd.notnull(self.__series_sheet.includedinthebox) \
                else None

        # Removing the unnecessary columns.
        self.__series_sheet.drop(index=["additionalaccessories", "suppliedaccessories",
                                        "includedinthebox"], inplace=True, errors="ignore")
        self.__series_sheet["product_in_box"] = result

    def _Process__get_product_info(self):
        result = dict()
        # Extracting the "Part Number" information.
        result["Part Number"] = Process.clean_text(self.__series_sheet.partno.strip()) \
            if "partno" in self.__series_sheet and pd.notnull(self.__series_sheet.partno) else None

        # Extracting the "Model Name" information.
        result["Model Name"] = Process.clean_text(self.__series_sheet.modelname.strip()) \
            if "modelname" in self.__series_sheet and pd.notnull(self.__series_sheet.modelname) else None

        # Extracting the "EAN Code" information.
        result["EAN Code"] = Process.clean_text(self.__series_sheet.eancode.strip()) \
            if "eancode" in self.__series_sheet and pd.notnull(self.__series_sheet.eancode) else None

        # Extracting the "UPC Code" information.
        result["UPC Code"] = Process.clean_text(self.__series_sheet.upccode.strip()) \
            if "upccode" in self.__series_sheet and pd.notnull(self.__series_sheet.upccode) else None

        # Extracting the "Marketing Name" information.
        result["Marketing Name"] = Process.clean_text(self.__series_sheet.marketingname.strip()) \
            if "marketingname" in self.__series_sheet and pd.notnull(self.__series_sheet.marketingname) else None

        # Removing the unnecessary columns.
        self.__series_sheet.drop(index=["partno", "modelname", "eancode", "upccode", "marketingname"],
                                 inplace=True, errors="ignore")
        self.__series_sheet["product_info"] = result

    def _Process__get_audio(self):
        result = dict()
        # Normalizing the features.
        if "speakers" in self.__series_sheet and pd.notnull(self.__series_sheet.speakers):
            self.__series_sheet["audio"] = self.__series_sheet.speakers \
                if "audio" not in self.__series_sheet or pd.isnull(self.__series_sheet.audio) \
                    else f"{self.__series_sheet.audio}, {self.__series_sheet.speakers}"
        if "audiotech" in self.__series_sheet and pd.notnull(self.__series_sheet.audiotech):
            self.__series_sheet["audio"] = self.__series_sheet.audiotech \
                if "audio" not in self.__series_sheet or pd.isnull(self.__series_sheet.audio)\
                    else f"{self.__series_sheet.audio}, {self.__series_sheet.audiotech}"
        if "voicecontrol" in self.__series_sheet and pd.notnull(self.__series_sheet.voicecontrol):
            self.__series_sheet["audio"] = self.__series_sheet.voicecontrol \
                if "audio" not in self.__series_sheet or pd.isnull(self.__series_sheet.audio) \
                    else f"{self.__series_sheet.audio}, {self.__series_sheet.voicecontrol}"

        if "audio" in self.__series_sheet and pd.notnull(self.__series_sheet.audio):
            # Extracting the "Microphone" and "Subwoofer" information.
            result["Microphone"] = True if "microphone" in self.__series_sheet.audio.lower() else False
            result["Subwoofer"] = True if "subwoofer" in self.__series_sheet.audio.lower() else False

            # Cleaning the content of "audio" feature.
            self.__series_sheet.audio = Process.clean_text(Process.clean_text(
                self.__series_sheet.audio, False).replace("\n", ", ")).strip()

            # Extracting the "Audio" information.
            result["Audio"] = re.sub(", ", "\n", self.__series_sheet.audio, flags=re.IGNORECASE).strip()
        else:
            result["Microphone"] = False
            result["Subwoofer"] = False
            result["Audio"] = None

        # Removing the unnecessary columns.
        self.__series_sheet.drop(index=["speakers", "audiotech", "voicecontrol", "audio"],
                                 inplace=True, errors="ignore")
        self.__series_sheet["product_audio"] = result

    def _Process__get_camera(self):
        result = dict()
        # Normalizing the features.
        if "videocamera" in self.__series_sheet and pd.notnull(self.__series_sheet.videocamera):
            self.__series_sheet["webcam"] = self.__series_sheet.videocamera \
                if "webcam" not in self.__series_sheet or pd.isnull(self.__series_sheet.webcam) \
                    else self.__series_sheet.webcam
        if "frontfacingcamera" in self.__series_sheet and pd.notnull(self.__series_sheet.frontfacingcamera):
            self.__series_sheet["webcam"] = self.__series_sheet.frontfacingcamera \
                if "webcam" not in self.__series_sheet or pd.isnull(self.__series_sheet.webcam) \
                    else self.__series_sheet.webcam

        if "webcam" in self.__series_sheet and pd.notnull(self.__series_sheet.webcam):
            # Cleaning the content of "webcam" feature.
            self.__series_sheet.webcam = Process.clean_text(Process.clean_text(
                self.__series_sheet.webcam.replace(" ; ", ", "),
                    normalize_spaces=False, remove_parenthesis=True).replace("\n", ", ")).strip()
            self.__series_sheet.webcam = ",".join([sb.strip() for sb in self.__series_sheet.webcam.split(",")])
            self.__series_sheet.webcam = re.sub(",", "\n", self.__series_sheet.webcam, flags=re.IGNORECASE).strip()
            self.__series_sheet.webcam = re.sub("web\s?camera", "camera",
                                                self.__series_sheet.webcam, flags=re.IGNORECASE).strip()

            # Extracting the "Front WebCam" and "Front Flash" information.
            result["Front WebCam"] = dict()
            result["Front WebCam"]["Front Flash"] = True if "front flash" in self.__series_sheet.webcam.lower() \
                else False
            result["Front WebCam"]["Type"] = re.split("camera", self.__series_sheet.webcam,
                                                      flags=re.IGNORECASE)[0].strip()
            if len(result["Front WebCam"]["Type"].split()) > 1:
                result["Front WebCam"]["Type"] = result["Front WebCam"]["Type"].split()[1].strip()
            result["Camera Features"] = re.sub("{} camera".format(result["Front WebCam"]["Type"]),
                                               "", self.__series_sheet.webcam).strip()
            result["Camera Features"] = result["Camera Features"] \
                if result["Camera Features"] != result["Front WebCam"]["Type"] and \
                   len(result["Camera Features"]) > 0 else None
            result["Camera Features"] = "\n".join([sb.strip() for sb in result["Camera Features"].split("\n")]) \
                if result["Camera Features"] else None
        else:
            result["Front WebCam"] = {"Type": None, "Front Flash": False}
            result["Camera Features"] = None

        # Notebooks don't rear cameras.
        result["Rear WebCam"] = {"Type": None, "Rear Flash": False}

        # Removing the unnecessary columns.
        self.__series_sheet.drop(index=["videocamera", "frontfacingcamera", "webcam"],
                                 inplace=True, errors="ignore")
        self.__series_sheet["product_camera"] = result

    def _Process__get_storage_card_reader(self):
        result = dict()
        # Normalizing the features.
        if "systemstorageinstalled" in self.__series_sheet and pd.notnull(self.__series_sheet.systemstorageinstalled):
            self.__series_sheet["storage"] = self.__series_sheet.systemstorageinstalled \
                if "storage" not in self.__series_sheet or pd.isnull(self.__series_sheet.storage) \
                    else self.__series_sheet.storage

        if pd.notnull(self.__series_sheet.storage):
            # Normalizing the content.
            self.__series_sheet.storage = Process.clean_text(re.sub("performance", "", self.__series_sheet.storage,
                                                                    flags=re.IGNORECASE)).strip()
            temp = re.search(r"^\w+ \d+\wb?", self.__series_sheet.storage, flags=re.IGNORECASE)
            if pd.notnull(temp):
                temp = temp.group().strip()
                self.__series_sheet.storage = re.sub(temp, f"{temp.split()[1]} {temp.split()[0]}",
                                                     self.__series_sheet.storage).strip()

            # Extracting the "RPM" information.
            result["RPM"] = re.search(r"\d+\s?rpm", self.__series_sheet.storage, flags=re.IGNORECASE)
            if pd.notnull(result["RPM"]):
                result["RPM"] = result["RPM"].group().strip()
                self.__series_sheet.storage = re.sub(result["RPM"], "", self.__series_sheet.storage).strip()
                result["RPM"] = re.sub("rpm", "", result["RPM"],
                                       flags=re.IGNORECASE).strip()

            # Extracting the "Size" information.
            result["Size"] = re.search(r"^\d+\s?\wb?", self.__series_sheet.storage, flags=re.IGNORECASE)
            if pd.notnull(result["Size"]):
                result["Size"] = result["Size"].group().strip()
                self.__series_sheet.storage = Process.clean_text(
                    re.sub(r"^\d+\s?\wb?", "", self.__series_sheet.storage, flags=re.IGNORECASE).strip())
                result["Size"] = Process.convert_to_gb(result["Size"]).strip()

            # Extracting the "System SSD Cache" information.
            temp = re.split(r"(ssd|hdd)", self.__series_sheet.storage, flags=re.IGNORECASE)
            result["System SSD Cache"] = temp[-1].strip() \
                if len(temp[-1].strip()) > 0 and len(temp) > 2 else None
            self.__series_sheet.storage = f"{temp[1]} {temp[0]}".strip() if len(temp) >= 2 else temp[0].strip()

            # Extracting the "Type" information.
            result["Type"] = self.__series_sheet.storage
        else:
            result["Type"] = None
            result["RPM"] = None
            result["Size"] = None
            result["System SSD Cache"] = None

        # Normalizing and extracting the "Card Reader" information.
        if "cardreader" in self.__series_sheet and pd.notnull(self.__series_sheet.cardreader):
            self.__series_sheet.cardreader = self.__series_sheet.cardreader.replace("Type:", "").replace(
                "Spec:", "").replace("\n", ",").strip()
        elif self.__series_sheet["product_connectors"]["Connectors"]:
            self.__series_sheet["cardreader"] = [
                sb.strip() for sb in self.__series_sheet["product_connectors"]["Connectors"].split("\n")
                if "card reader" in sb.lower()]
            if len(self.__series_sheet.cardreader) > 0:
                self.__series_sheet["cardreader"] = [
                    sb.strip()
                    for sb in re.split("card reader", self.__series_sheet["cardreader"][0], flags=re.IGNORECASE)
                    if sb.strip()][0]
            else:
                self.__series_sheet["cardreader"] = None
        else:
            self.__series_sheet["cardreader"] = None
        self.__series_sheet["product_card_reader"] = {"Card Reader": Process.clean_text(
            self.__series_sheet.cardreader)}

        # Removing the unnecessary columns.
        self.__series_sheet.drop(index=["systemstorageinstalled", "storage", "cardreader"],
                                 inplace=True, errors="ignore")
        self.__series_sheet["product_storage"] = result

    def _Process__get_color(self):
        result = dict()
        # Normalizing the features.
        if "lcdcovercolordecoration" in self.__series_sheet and pd.notnull(self.__series_sheet.lcdcovercolordecoration):
            self.__series_sheet["lcdcovercolor"] = self.__series_sheet.lcdcovercolordecoration \
                if "lcdcovercolor" not in self.__series_sheet or pd.isnull(self.__series_sheet["lcdcovercolor"]) \
                    else self.__series_sheet["lcdcovercolor"]
        if "topcasecolordecoration" in self.__series_sheet and pd.notnull(self.__series_sheet.topcasecolordecoration):
            self.__series_sheet["topcasecolor"] = self.__series_sheet.topcasecolordecoration \
                if "topcasecolor" not in self.__series_sheet or pd.isnull(self.__series_sheet["topcasecolor"]) \
                    else self.__series_sheet["topcasecolor"]
        for feature in ["lcdcovercolor", "topcasecolor", "bottomcasecolor"]:
            if feature in self.__series_sheet and pd.notnull(self.__series_sheet[feature]):
                self.__series_sheet["color"] = Process.clean_text(self.__series_sheet[feature]) \
                    if "color" not in self.__series_sheet or pd.isnull(self.__series_sheet.color) \
                        else f"{self.__series_sheet.color} / {Process.clean_text(self.__series_sheet[feature])}"

        if pd.notnull(self.__series_sheet.color):
            # Normalizing the content.
            self.__series_sheet.color = " / ".join(set([c.title().strip()
                                                        for c in self.__series_sheet.color.split("/")])).strip()

            # Extracting the "Color" information.
            result["Color"] = Process.clean_text(self.__series_sheet.color)
        else:
            result["Color"] = None

        # Defining the value for "Color Id" feature.
        result["Color Id"] = None

        # Removing the unnecessary columns.
        self.__series_sheet.drop(index=["lcdcovercolordecoration", "topcasecolordecoration",
                                        "lcdcovercolor", "topcasecolor", "bottomcasecolor", "color"],
                                 inplace=True, errors="ignore")
        self.__series_sheet["product_color"] = result

    def _Process__get_connectors(self):
        result = dict()
        # Normalizing the features.
        for feature in ["usbport", "displayoutput", "externalvideodisplaymodes", "thunderbolt",
                        "mic", "interface"]:
            if feature in self.__series_sheet and pd.notnull(self.__series_sheet[feature]):
                self.__series_sheet["ioports"] = self.__series_sheet[feature] \
                    if "ioports" not in self.__series_sheet or pd.isnull(self.__series_sheet.ioports) \
                        else f"{self.__series_sheet.ioports}\n{self.__series_sheet[feature]}"

        if "ioports" in self.__series_sheet and pd.notnull(self.__series_sheet.ioports):
            # Normalizing the content.
            self.__series_sheet.ioports = "\n".join(
                [Process.clean_text(Process.clean_text(sb.strip(), remove_specials=False).replace(
                    "Spec:", "Card Reader"), False).strip()
                 for sb in self.__series_sheet.ioports.split("\n") if len(sb) > 0])

            # Extracting the "Connectors" information.
            result["Connectors"] = Process.clean_text(self.__series_sheet.ioports, False)
        else:
            result["Connectors"] = None

        # Removing the unnecessary columns.
        self.__series_sheet.drop(index=["usbport", "displayoutput", "externalvideodisplaymodes", "thunderbolt",
                                        "mic", "ioports", "interface"],
                                 inplace=True, errors="ignore")
        self.__series_sheet["product_connectors"] = result

    def _Process__get_extra_features(self):
        result = dict()
        # Normalizing the features and their content.
        if "numberpad" in self.__series_sheet and pd.notnull(self.__series_sheet.numberpad):
            self.__series_sheet.numberpad = self.__series_sheet.numberpad \
                if "support" in self.__series_sheet.numberpad.lower() \
                    else f"Support {self.__series_sheet.numberpad}"
        if "viewingangle" in self.__series_sheet and pd.notnull(self.__series_sheet.viewingangle):
            self.__series_sheet.viewingangle = f"Viewing Angle {self.__series_sheet.viewingangle}"
        if "m2slotssupporteithersataandnvme" in self.__series_sheet and pd.notnull(self.__series_sheet.m2slotssupporteithersataandnvme):
            self.__series_sheet.m2slotssupporteithersataandnvme = f"{self.__series_sheet.m2slotssupporteithersataandnvme} M.2 SATA/NVMe slots"
        if "aurasync" in self.__series_sheet and pd.notnull(self.__series_sheet.aurasync):
            self.__series_sheet.aurasync = "Support Aura Sync" \
                if "yes" == self.__series_sheet.aurasync.lower().strip() else None
        if "adaptivesynctechnology" in self.__series_sheet and pd.notnull(self.__series_sheet.adaptivesynctechnology):
            self.__series_sheet.adaptivesynctechnology = f"{self.__series_sheet.adaptivesynctechnology} as Adaptative Sync Technology"
        if "contrastratio" in self.__series_sheet and pd.notnull(self.__series_sheet.contrastratio):
            self.__series_sheet["contrast"] = self.__series_sheet.contrastratio \
                if "contrast" not in self.__series_sheet or pd.isnull(self.__series_sheet.contrast) \
                    else self.__series_sheet.contrast
        if "contrast" in self.__series_sheet and pd.notnull(self.__series_sheet.contrast):
            self.__series_sheet.contrast = self.__series_sheet.contrast \
                if len(self.__series_sheet.contrast.split(":")[0]) == 1 \
                    else ":".join(self.__series_sheet.contrast.split(":")[::-1])
            self.__series_sheet.contrast = f"Contrast {self.__series_sheet.contrast}"
        if "m2ssdsupportlist" in self.__series_sheet and pd.notnull(self.__series_sheet.m2ssdsupportlist):
            self.__series_sheet.m2ssdsupportlist = re.sub(
                r"[\n\r]+", ", ", re.sub(r"\d\.\s?", "", self.__series_sheet.m2ssdsupportlist.strip()))
            if "m2slotssupporteithersataandnvme" in self.__series_sheet and pd.notnull(self.__series_sheet.m2slotssupporteithersataandnvme):
                self.__series_sheet.m2ssdsupportlist = f"{self.__series_sheet.m2slotssupporteithersataandnvme}: " \
                                                       f"{self.__series_sheet.m2ssdsupportlist}"
                self.__series_sheet.drop(index="m2slotssupporteithersataandnvme", inplace=True, errors="ignore")

        # Extracting the "Extra Features" information.
        for feature in ["militarygrade", "numberpad", "viewingangle", "aurasync", "adaptivesynctechnology",
                        "contrast", "screenpad", "m2ssdsupportlist", "m2slotssupporteithersataandnvme"]:
            if feature in self.__series_sheet and pd.notnull(self.__series_sheet[feature]):
                result["Extra Features"] = Process.clean_text(self.__series_sheet[feature]) \
                    if "Extra Features" not in result or pd.isnull(result["Extra Features"]) \
                    else f"{result['Extra Features']}\n{Process.clean_text(self.__series_sheet[feature])}"
        if "Extra Features" not in result:
            result["Extra Features"] = None

        # Removing the unnecessary columns.
        self.__series_sheet.drop(index=["militarygrade", "numberpad", "viewingangle", "aurasync",
                                        "adaptivesynctechnology", "contrast", "screenpad", "m2ssdsupportlist",
                                        "m2slotssupporteithersataandnvme", "contrastratio"],
                                 inplace=True, errors="ignore")
        self.__series_sheet["product_extra_features"] = result

    def _Process__get_softwares(self):
        result = dict()
        # Extracting the "Operation System" information.
        if "operatingsystem" in self.__series_sheet and pd.notnull(self.__series_sheet.operatingsystem):
            self.__series_sheet.operatingsystem = self.__series_sheet.operatingsystem.replace("-OS", " OS")
            result["Operation System"] = Process.clean_text(
                re.split(r"[^\s\d\w\.]", self.__series_sheet.operatingsystem)[0].strip())

        # Extracting the "Security" information.
        if "security" in self.__series_sheet and pd.notnull(self.__series_sheet.security):
            result["Security"] = Process.clean_text(
                self.__series_sheet.security, False, normalize_break_lines=True).strip()

        # Normalizing the features and their content.
        if "office" in self.__series_sheet and pd.notnull(self.__series_sheet.office):
            self.__series_sheet.office = Process.clean_text(self.__series_sheet.office.strip()).strip()
            self.__series_sheet.office = re.sub(r"\s+\-$", "", self.__series_sheet.office).strip()
        if "builtinapps" in self.__series_sheet and pd.notnull(self.__series_sheet.builtinapps):
            self.__series_sheet.builtinapps = Process.clean_text(self.__series_sheet.builtinapps.strip(), False,
                                                                 normalize_break_lines=True).strip()
            if "myasusfeature" in self.__series_sheet and pd.notnull(self.__series_sheet.myasusfeature):
                self.__series_sheet.builtinapps = "\n".join([
                    sb for sb in self.__series_sheet.builtinapps.split("\n")
                    if Process.clean_text(sb, False, True).strip().lower() not in self.__series_sheet.myasusfeature.lower()])
                self.__series_sheet.builtinapps = self.__series_sheet.builtinapps \
                    if len(self.__series_sheet.builtinapps.strip()) > 0 else None
        if "myasusfeature" in self.__series_sheet and pd.notnull(self.__series_sheet.myasusfeature):
            self.__series_sheet.myasusfeature = Process.clean_text(self.__series_sheet.myasusfeature.strip(), False,
                                                                   normalize_break_lines=True).strip()
        if "software" in self.__series_sheet and pd.notnull(self.__series_sheet.software):
            self.__series_sheet.software = Process.clean_text(self.__series_sheet.software.strip(), False,
                                                              normalize_break_lines=True).strip()
        for feature in ["myasusfeature", "builtinapps", "office"]:
            if feature in self.__series_sheet and pd.notnull(self.__series_sheet[feature]):
                self.__series_sheet["software"] = self.__series_sheet[feature] \
                    if "software" not in self.__series_sheet or pd.isnull(self.__series_sheet.software) \
                        else f"{self.__series_sheet.software}\n{self.__series_sheet[feature]}"

        # Extracting the "Softwares" information.
        if "software" in self.__series_sheet and pd.notnull(self.__series_sheet.software):
            self.__series_sheet.software = "\n".join([
                Process.clean_text(sb, False).strip() for sb in self.__series_sheet.software.split("\n")])
            result["Softwares"] = Process.clean_text(self.__series_sheet.software, False) \
                if pd.notnull(self.__series_sheet.software) else None
        else:
            result["Softwares"] = None

        # Removing the unnecessary columns.
        self.__series_sheet.drop(index=["operatingsystem", "security", "office",
                                        "myasusfeature", "builtinapps", "software"],
                                 inplace=True, errors="ignore")
        self.__series_sheet["product_softwares"] = result

    def _Process__get_processor(self):
        result = dict()
        # Extracting the "Chipset" information.
        if "chipset" in self.__series_sheet and pd.notnull(self.__series_sheet.chipset):
            self.__series_sheet.chipset = re.sub("chipsets?", "", self.__series_sheet.chipset,
                                                 flags=re.IGNORECASE).strip()
            result["Chipset"] = Process.clean_text(self.__series_sheet.chipset)
        else:
            result["Chipset"] = None

        # Normalizing the features.
        if "onboardprocessor" in self.__series_sheet and pd.notnull(self.__series_sheet.onboardprocessor):
            self.__series_sheet["processor"] = self.__series_sheet.onboardprocessor \
                if "processor" not in self.__series_sheet or pd.isnull(self.__series_sheet.processor) \
                    else self.__series_sheet.processor

        # Extracting the "Processor" data.
        if "processor" in self.__series_sheet and pd.notnull(self.__series_sheet.processor):
            self.__series_sheet.processor = re.sub("mobile", "", self.__series_sheet.processor,
                                                   flags=re.IGNORECASE).strip()
            self.__series_sheet.processor = Process.clean_text(self.__series_sheet.processor)
            self.__series_sheet.processor = re.sub("\d+th\s? gen(eration)?", "", self.__series_sheet.processor,
                                                   flags=re.IGNORECASE).strip()
            self.__series_sheet.processor = self.__series_sheet.processor.replace(
                "IntelCore", "Intel Core").replace("AMDRyzen", "AMD Ryzen").strip()

            # Splitting the text in two parts.
            self.__series_sheet.processor = [t.strip() for t in self.__series_sheet.processor.split("Processor")]

            # Extracting the "Processor Vendor" information.
            result["Processor Vendor"] = self.__series_sheet.processor[0].split()[0].strip()
            self.__series_sheet.processor[0] = self.__series_sheet.processor[0].replace(
                result["Processor Vendor"], "").strip()

            # Extracting the "Processor Family" and "Model" information.
            if len(self.__series_sheet.processor[0].split("-")) > 1:
                result["Processor Family"] = self.__series_sheet.processor[0].split("-")[0].strip()
                result["Model"] = {"Model": self.__series_sheet.processor[0].split("-")[1].strip()}
            else:
                result["Processor Family"] = " ".join(self.__series_sheet.processor[0].split()[:-1])
                result["Model"] = {"Model": self.__series_sheet.processor[0].split()[-1]}

            # Extracting the Frequency of Processor.
            self.__series_sheet.processor = self.__series_sheet.processor[1].lower()
            groups = re.search(r"(\d+\.?\d+)\s*\whz", self.__series_sheet.processor)
            if groups:
                result["Model"]["Frequency"] = groups.groups()[0]
                self.__series_sheet.processor = self.__series_sheet.processor.replace(groups.group(), "").strip()
            else:
                result["Model"]["Frequency"] = None

            # Extracting the Cache of Processor.
            groups = re.search(r"(\d+\.?\d*)\s*\w+\s*cache", self.__series_sheet.processor)
            if groups:
                result["Model"]["Cache"] = groups.groups()[0]
                self.__series_sheet.processor = self.__series_sheet.processor.replace(groups.group(), "").strip()
            else:
                result["Model"]["Cache"] = None

            # Extracting the Number of Cores of Processor.
            expressions = [r"(\d+)\s*cores?", r"(\d+)c/\d+t", r"(\d+)-core", r"(\d+)..cores"]
            groups = [re.search(e, self.__series_sheet.processor)
                      for e in expressions if re.search(e, self.__series_sheet.processor)]
            if groups:
                groups = groups[0]
                result["Model"]["Cores"] = groups.groups()[0]
                self.__series_sheet.processor = self.__series_sheet.processor.replace(groups.group(), "").strip()
            else:
                result["Model"]["Cores"] = None
        else:
            result["Processor Family"] = None
            result["Processor Vendor"] = None
            result["Model"] = None

        # Removing the unnecessary columns.
        self.__series_sheet.drop(index=["chipset", "onboardprocessor", "processor"], inplace=True, errors="ignore")
        self.__series_sheet["product_processor"] = result

    def _Process__get_gpu(self):
        result = dict()
        # Normalizing the features and their content.
        if "vram" in self.__series_sheet and pd.notnull(self.__series_sheet.vram):
            self.__series_sheet["graphicmemory"] = self.__series_sheet.vram \
                if "graphicmemory" not in self.__series_sheet or pd.isnull(self.__series_sheet.graphicmemory) \
                    else self.__series_sheet.graphicmemory
        if "igpu" in self.__series_sheet and pd.notnull(self.__series_sheet.igpu):
            self.__series_sheet["intergratedgpu"] = self.__series_sheet.igpu \
                if "intergratedgpu" not in self.__series_sheet or pd.isnull(self.__series_sheet.intergratedgpu) \
                    else self.__series_sheet.intergratedgpu
        if "graphic" in self.__series_sheet and pd.notnull(self.__series_sheet.graphic):
            self.__series_sheet["graphics"] = self.__series_sheet.graphic \
                if "graphics" not in self.__series_sheet or pd.isnull(self.__series_sheet.graphics) \
                    else self.__series_sheet.graphics
        if "discreteoptimus" in self.__series_sheet and pd.notnull(self.__series_sheet.discreteoptimus):
            self.__series_sheet["discreteshare"] = self.__series_sheet.discreteoptimus \
                if "discreteshare" not in self.__series_sheet or pd.isnull(self.__series_sheet.discreteshare) \
                    else self.__series_sheet.discreteshare
        if "discreteshare" in self.__series_sheet or pd.notnull(self.__series_sheet.discreteshare):
            temp = re.search(r"\((.+)\)", self.__series_sheet.discreteshare)
            if temp:
                self.__series_sheet.discreteshare = re.sub(r"[\(\)]+", "", temp.group()).strip()

        # Extracting the "Memory" information.
        if "graphicmemory" in self.__series_sheet and pd.notnull(self.__series_sheet.graphicmemory):
            self.__series_sheet.graphicmemory = self.__series_sheet.graphicmemory.split()
            self.__series_sheet.graphicmemory[0] = Process.convert_to_gb(self.__series_sheet.graphicmemory[0])
            result["Memory"] = dict(zip(["Type", "Size"], self.__series_sheet.graphicmemory[::-1]))
        else:
            result["Memory"] = None

        # Extracting the remainder of data.
        if "discreteshare" in self.__series_sheet and pd.notnull(self.__series_sheet.discreteshare):
            # Checking if a GPU is dedicated/discrete/optimus or shared.
            if self.__series_sheet.discreteshare == "Share":
                self.__series_sheet.intergratedgpu = Process.clean_text(
                    self.__series_sheet.intergratedgpu \
                        if "intergratedgpu" in self.__series_sheet and pd.notnull(self.__series_sheet.intergratedgpu) \
                        else self.__series_sheet.graphics \
                        if "graphics" in self.__series_sheet and pd.notnull(self.__series_sheet.graphics) \
                        else None, remove_parenthesis=True)
                if pd.notnull(self.__series_sheet.intergratedgpu):
                    self.__series_sheet.intergratedgpu = self.__series_sheet.intergratedgpu.replace(
                        "Laptop GPU", "").strip()
                    result["Vendor"] = self.__series_sheet.intergratedgpu.split()[0].upper().strip()
                    result["Model"] = Process.clean_text(
                        " ".join(self.__series_sheet.intergratedgpu.split()[1:]).strip(), False)
                    result["Type"] = {"Type": f"{result['Vendor']} INTEGRATED", "SubType": "SHARED"}
            else:
                self.__series_sheet.graphics = Process.clean_text(
                    self.__series_sheet.graphics \
                        if "graphics" in self.__series_sheet and pd.notnull(self.__series_sheet.graphics) \
                        else self.__series_sheet.intergratedgpu \
                        if "intergratedgpu" in self.__series_sheet and pd.notnull(self.__series_sheet.intergratedgpu) \
                        else None)
                if pd.notnull(self.__series_sheet.graphics):
                    self.__series_sheet.graphics = self.__series_sheet.graphics.replace("Laptop GPU", "").strip()
                    result["Vendor"] = self.__series_sheet.graphics.split()[0].upper().strip()
                    result["Model"] = Process.clean_text(
                        " ".join(self.__series_sheet.graphics.split()[1:]).strip(), False)
                    self.__series_sheet.discreteshare = "OPTIMUS" \
                        if "optimus" in self.__series_sheet.discreteshare.lower() else "DISCRETE"
                    result["Type"] = {"Type": f"{result['Vendor']} {self.__series_sheet.discreteshare}",
                                      "SubType": "DEDICATED"}

        # Removing the unnecessary columns.
        self.__series_sheet.drop(index=["vram", "igpu", "graphic", "discreteoptimus", "discreteshare",
                                        "graphicmemory", "intergratedgpu", "graphics"], inplace=True, errors="ignore")
        self.__series_sheet["product_gpu"] = result