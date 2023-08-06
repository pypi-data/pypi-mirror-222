# Multiple Loader
# Author: DomZou
# The license is MIT.

import os
from multipleloader.LoaderError import *
from .extension_settings import extensions
from .loader.csv_loader import csv_loader
from .loader.numpy_loader import numpy_loader
from .loader.joblib_loader import joblib_loader
from .loader.json_loader import json_loader
from .loader.pandas_loader import pandas_loader
from .loader.pickle_loader import pickle_loader

from .loader.loading_src.file_main_loader_class import FileLoader


def load(filepath="", lib="", encoding=""):

    """ Separate file name """
    if not len(filepath):
        raise PathEmptyError(filepath)
    else:
        root_ext_pair = os.path.splitext(filepath)

        if root_ext_pair[1].lower() in extensions.keys():
            set_extension = root_ext_pair[1].lower()    # set extension name
        else:
            raise ExtensionSupportError(root_ext_pair[1])
    

    """ Check existence of file """
    if os.path.isfile(filepath):
        print(f"[{set_extension}]: Open File ─────>> {filepath}")
    else:
        raise FileNotFoundError(filepath)
    

    """ Check library and default encoder """
    if len(lib) != 0:
        lib_check_flag = False
        lib_name = lib.lower()
        extension_libs_data = extensions[set_extension]
        for lib_key, lib_name_data in extension_libs_data["library"].items():
            if lib_name in lib_name_data["keys"]:
                lib_check_flag = True
                use_library = lib_key
                if len(encoding) == 0:
                    encoding = lib_name_data["default_encoding"]
                else:
                    encoding = encoding
            
        if lib_check_flag is not True:
            raise LibraryNotFoundError(lib_name)
    else:   # default library
        use_library = extensions[set_extension]["DEFAULT"]
        encoding = extensions[set_extension]["library"][use_library]["default_encoding"]

    """ ### LOADER ### """
    fileloader = FileLoader()
    loader_functions = {
        "numpy": numpy_loader,
        "pandas": pandas_loader,
        "pickle": pickle_loader,
        "json": json_loader,
        "joblib": joblib_loader,
        "csv": csv_loader,
    }
    if use_library in loader_functions:
        loader_func = loader_functions[use_library]
        return fileloader.file_main_loader(file_path=filepath, ext_type=set_extension, lib_name=use_library, loader_func=loader_func, encoding=encoding)




