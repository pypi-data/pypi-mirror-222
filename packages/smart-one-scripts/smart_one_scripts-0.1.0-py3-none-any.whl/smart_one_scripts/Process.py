##############################################################
# NLP - Information Extraction from Excel files to Smart One #
##############################################################

##############################
# 1. Importing the libraries #
##############################
import warnings
import pandas as pd
import numpy as np
import re
import unicodedata
import unidecode
from abc import abstractmethod, ABC


##############################
### Super Class "Process" ####
##############################
class Process(ABC):

    def preprocess(self):
        self.__get_power_adapter()
        self.__get_screen()
        self.__get_network_connectivity()
        self.__get_keyboard()
        self.__get_audio()
        self.__get_camera()
        self.__get_connectors()
        self.__get_storage_card_reader()
        self.__get_color()
        self.__get_in_box()
        self.__get_product_info()
        self.__get_extra_features()
        self.__get_softwares()
        self.__get_processor()
        self.__get_weight()
        self.__get_memory()
        self.__get_dimensions()
        self.__get_gpu()

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, '__get_power_adapter') and callable(subclass.__get_power_adapter) and
                hasattr(subclass, '__get_screen') and callable(subclass.__get_screen) and
                hasattr(subclass, '__get_network_connectivity') and callable(subclass.__get_network_connectivity) and
                hasattr(subclass, '__get_keyboard') and callable(subclass.__get_keyboard) and
                hasattr(subclass, '__get_audio') and callable(subclass.__get_audio) and
                hasattr(subclass, '__get_camera') and callable(subclass.__get_camera) and
                hasattr(subclass, '__get_connectors') and callable(subclass.__get_connectors) and
                hasattr(subclass, '__get_storage_card_reader') and callable(subclass.__get_storage_card_reader) and
                hasattr(subclass, '__get_color') and callable(subclass.__get_color) and
                hasattr(subclass, '__get_in_box') and callable(subclass.__get_in_box) and
                hasattr(subclass, '__get_product_info') and callable(subclass.__get_product_info) and
                hasattr(subclass, '__get_extra_features') and callable(subclass.__get_extra_features) and
                hasattr(subclass, '__get_softwares') and callable(subclass.__get_softwares) and
                hasattr(subclass, '__get_processor') and callable(subclass.__get_processor) and
                hasattr(subclass, '__get_weight') and callable(subclass.__get_weight) and
                hasattr(subclass, '__get_memory') and callable(subclass.__get_memory) and
                hasattr(subclass, '__get_dimensions') and callable(subclass.__get_dimensions) and
                hasattr(subclass, '__get_gpu') and callable(subclass.__get_gpu) or
                NotImplemented)

    @abstractmethod
    def __get_dimensions(self):
        raise NotImplementedError

    @abstractmethod
    def __get_memory(self):
        raise NotImplementedError

    @abstractmethod
    def __get_weight(self):
        raise NotImplementedError

    @abstractmethod
    def __get_power_adapter(self):
        raise NotImplementedError

    @abstractmethod
    def __get_screen(self):
        raise NotImplementedError

    @abstractmethod
    def __get_network_connectivity(self):
        raise NotImplementedError

    @abstractmethod
    def __get_keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def __get_audio(self):
        raise NotImplementedError

    @abstractmethod
    def __get_camera(self):
        raise NotImplementedError

    @abstractmethod
    def __get_storage_card_reader(self):
        raise NotImplementedError

    @abstractmethod
    def __get_color(self):
        raise NotImplementedError

    @abstractmethod
    def __get_in_box(self):
        raise NotImplementedError

    @abstractmethod
    def __get_product_info(self):
        raise NotImplementedError

    @abstractmethod
    def __get_connectors(self):
        raise NotImplementedError

    @abstractmethod
    def __get_extra_features(self):
        raise NotImplementedError

    @abstractmethod
    def __get_softwares(self):
        raise NotImplementedError

    @abstractmethod
    def __get_processor(self):
        raise NotImplementedError

    @abstractmethod
    def __get_gpu(self):
        raise NotImplementedError

    @staticmethod
    def clean_text(text, normalize_spaces=True, remove_parenthesis=False,
                   normalize_break_lines=False, remove_specials=True):
        if pd.isnull(text):
            return None
        # Removing the special characters and extra whitespace.
        if remove_specials:
            text = re.sub("N/A", "", text, flags=re.IGNORECASE).strip()
            text = text.replace("\u00C2", "").replace("\u00A9", "").replace(
                "\u2122", "").replace("\u00AE", "").replace(u"\xa0", " ").replace(
                "//", "\n").replace("\\n", "\n").replace("\"", "").replace(
                "'", "").replace("\r", "").strip()

        if normalize_break_lines:
            text = re.sub(r"[\n\r]+", "\n", text).strip()

        if remove_parenthesis:
            text = re.sub(r"\(.*\)", "", text).strip()

        text = unicodedata.normalize("NFKD", text)
        text = unidecode.unidecode(text)
        if normalize_spaces:
            text = re.sub(r"\s+", " ", text)
        return text

    @staticmethod
    def convert_to_gb(value):
        value = [i for i in re.split(r"^(\d+)\s*(\w+)$", value,
                                     flags=re.IGNORECASE) if len(i) > 0]
        if len(value) > 1:
            if value[1].lower() == "gb" or value[1].lower() == "g":
                exp = 0
            elif value[1].lower() == "tb":
                exp = 1
            elif value[1].lower() == "pb":
                exp = 2
            elif value[1].lower() == "eb":
                exp = 3
            elif value[1].lower() == "zb":
                exp = 4
            elif value[1].lower() == "yb":
                exp = 5
            else:
                exp = -1
            return str(int((1024 ** exp) * int(value[0]))) if exp != -1 else "".join(value)
        else:
            return value[0]

    @staticmethod
    def convert_to_hz(value):
        value = [i for i in re.split(r"^([\d/]+)\s*(\w+)$", value,
                                     flags=re.IGNORECASE) if len(i) > 0]
        value = [*value[0].split("/"), value[-1]]
        value = [v.strip() for v in value]
        if len(value) > 1:
            if value[-1].lower() == "dahz": # decahertz
                exp = 1
            elif value[-1].lower() == "hhz": # hectohertz
                exp = 2
            elif value[-1].lower() == "khz": # quilohertz
                exp = 3
            elif value[-1].lower() == "mhz": # megahertz
                exp = 6
            elif value[-1].lower() == "ghz": # gigahertz
                exp = 9
            elif value[-1].lower() == "thz": # terahertz
                exp = 12
            elif value[-1].lower() == "phz": # petahertz
                exp = 15
            elif value[-1].lower() == "ehz": # exahertz
                exp = 18
            elif value[-1].lower() == "zhz": # zetahertz
                exp = 21
            elif value[-1].lower() == "yhz": # yotahertz
                exp = 24
            elif value[-1].lower() == "rhz": # ronnahertz
                exp = 27
            elif value[-1].lower() == "qhz": # quennahertz
                exp = 30
            else:
                exp = -1
            if exp != -1:
                return "/".join([str(int((10 ** exp) * int(i))) for i in value[:-1]])
            return "".join(["/".join(value[:-1]), value[-1]])
        else:
            return value[0]

    @staticmethod
    def __normalize_column_sheet(text):
        text = re.sub(r"[^\d\w]+", "", text.lower())
        text = unicodedata.normalize("NFKD", text)
        text = unidecode.unidecode(text)
        return text

    @staticmethod
    def __remove_duplicated_columns(sheet):
        column_count = sheet.index.value_counts()
        if column_count[column_count > 1].size > 0:
            col = sheet[column_count[column_count > 1].index].index.unique()[0]
            c_values = [str(v) for v in sheet[col].unique() if v]
            if len(c_values) == 0:
                sheet[col] = None
            elif len(c_values) == 1:
                sheet[col] = c_values[0]
            else:
                sheet[col] = ", ".join(c_values)
        return sheet[~sheet.index.duplicated(keep="first")]

    @staticmethod
    def __remove_unnecessary_columns(sheet, cols=None):
        if cols:
            sheet.drop(labels=cols, inplace=True, errors="ignore")
        cols = [c for c in sheet.index if pd.isnull(sheet[c])]
        sheet.drop(labels=cols, inplace=True, errors="ignore")
        return sheet

    @staticmethod
    def extract_data_from_sheet(xlsx_file, cols_to_remove=None):
        # Ignoring the warnings.
        warnings.simplefilter("ignore")

        # Reading the file.
        sheet = pd.read_excel(xlsx_file)

        # Validating the spreadsheet.
        if sheet.shape[1] != 2:
            raise Exception(f"Planilha '{xlsx_file}' não está no formato correto!!!")

        # Extracting and preprocessing the data.
        sheet.replace({np.nan: None}, inplace=True)
        sheet.dropna(axis=0, how="all", inplace=True)
        sheet.columns = [f"col{i+1}" for i in range(sheet.shape[1])]
        sheet.col1 = sheet.col1.apply(Process.__normalize_column_sheet)
        sheet = pd.Series(index=sheet.T.loc["col1"].tolist(), data=sheet.T.loc["col2"].tolist())
        sheet = Process.__remove_duplicated_columns(sheet)
        sheet = Process.__remove_unnecessary_columns(sheet, cols_to_remove)
        return sheet
