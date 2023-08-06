import numpy as np

def numpy_loader(file_path, ext_type, encoding):
    if ext_type == ".csv":
        try:
            return np.genfromtxt(file_path, delimiter=",", encoding=encoding), True, "Success"
        except Exception as e:
            if isinstance(e, Warning):
                return e, False, "Warning"
            else:
                return e, False, "Error"
    elif ext_type == ".tsv":
        try:
            return np.genfromtxt(file_path, delimiter="\t", encoding=encoding), True, "Success"
        except Exception as e:
            if isinstance(e, Warning):
                return e, False, "Warning"
            else:
                return e, False, "Error"
    elif ext_type == ".npy" or ext_type == ".npz":
        try:
            return np.load(file_path, encoding=encoding), True, "Success"
        except Exception as e:
            if isinstance(e, Warning):
                return e, False, "Warning"
            else:
                return e, False, "Error"
    else:
        return None, False  # サポートされていない拡張子の場合はNoneを返す
