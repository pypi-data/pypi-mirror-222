import ast
import os
import re
import warnings
from collections import OrderedDict

warnings.filterwarnings("ignore")


class GoConfigure:
    """
    Basic python config parser which attempts to coerce types

    """

    def __init__(self, path):
        """
        :param path: should be a valid file path. It does not hav currently exist. If the file does not exist then it
        will be created.
        """
        self._fl = path
        self._conf_dict = OrderedDict({})
        if not os.path.isfile(path):
            self._create_conf()
        self._read_fl_into()

    def __getitem__(self, key):
        return self._conf_dict[key]

    def __setitem__(self, key, value):
        if key in self._conf_dict:
            self._conf_dict[key] = value
        else:
            raise Exception("Key not found")

    def _create_conf(self):
        """
        Creates the config file if not exists
        :return:
        """
        with open(self._fl, "x") as f:
            f.close()

    def reload(self):
        """
        reloads the config file into the object
        :return:
        """
        self._read_fl_into()

    def make_section(self, k, write=False):
        """
        Created a new section in the config file
        :param k: key of new section
        :param write: Bool - if true writes to file
        :return:
        """
        self._conf_dict[k] = {}
        if write:
            self.write()

    def _read_fl_into(self):
        """
        Reads the config file into an ordered dict
        :return: None
        """
        self._conf_dict = OrderedDict({})
        current_section = None

        with open(self._fl, "r") as f:
            for line in f:
                ln = line.strip()
                # section
                section = re.search('[[].*[]]', ln)
                comment = re.search("[#].*", ln)
                val = None if ln.count("=") == 0 else ln
                if section:
                    current_section = section.group(0).replace("[", "").replace("]", "")
                    comment_no = 0
                    self._conf_dict[current_section] = {}
                elif comment:
                    self._conf_dict[current_section][f"comment_{comment_no}"] = comment.group(0).replace("#",
                                                                                                         "").strip()
                    comment_no += 1
                elif val:
                    key, value = ln.split("=", 1)
                    try:
                        self._conf_dict[current_section][key] = ast.literal_eval(value)
                    except (ValueError, SyntaxError):
                        self._conf_dict[current_section][key] = check_bool(value)

    def __check_section(self, current_section):
        if current_section is None:
            raise Exception("You have not defined a main block. This should appear like [SECTION] ")

    def write(self):
        """
        reloads the config file into the object
        :return: None
        """
        text = ""
        for main_key, main_values in self._conf_dict.items():
            text += f"[{main_key}]\n\n"
            for sub_k, sub_val in main_values.items():
                if "comment_" in sub_k:
                    text += f"#{sub_val}\n"
                else:
                    text += f"{sub_k}={sub_val}\n"

        with open(self._fl, "w") as f:
            f.write(text)


def check_bool(string):
    """
    Checks if a string is a bool
    :param string: string to check
    :return: bool or string
    """
    string = string.strip()
    if string in ["true", "True", "TRUE", "t", "T"]:
        return True
    elif string in ["false", "False", "FALSE", "f", "F"]:
        return False
    else:
        return string
