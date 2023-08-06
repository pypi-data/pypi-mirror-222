import pandas as pd
import warnings

def pandas_loader(file_path, ext_type, encoding):
    warnings.simplefilter('error', pd.errors)   # DtypeWarning etc...

    if ext_type == ".csv":
        try:
            return pd.read_csv(file_path, encoding=encoding), True, "Success"
        except Exception as e:
            if isinstance(e, Warning):
                return e, False, "Warning"
            else:
                return e, False, "Error"
    elif ext_type == ".tsv":
        try:
            return pd.read_table(file_path, encoding=encoding), True, "Success"
        except Exception as e:
            if isinstance(e, Warning):
                return e, False, "Warning"
            else:
                return e, False, "Error"
        except pd.errors.DtypeWarning as e:
            return e, False, "Warning"
    elif ext_type == ".pickle":
        try:
            return pd.read_pickle(file_path), True, "Success"
        except Exception as e:
            if isinstance(e, Warning):
                return e, False, "Warning"
            else:
                return e, False, "Error"
        except pd.errors.DtypeWarning as e:
            return e, False, "Warning"
    elif ext_type == ".json":
        try:
            return pd.read_json(file_path, encoding=encoding), True, "Success"
        except Exception as e:
            if isinstance(e, Warning):
                return e, False, "Warning"
            else:
                return e, False, "Error"
        except pd.errors.DtypeWarning as e:
            return e, False, "Warning"
    else:
        return None, False  # サポートされていない拡張子の場合はNoneを返す