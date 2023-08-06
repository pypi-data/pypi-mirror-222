import joblib

def joblib_loader(file_path, ext_type, encoding):
    if ext_type == ".pickle" or ext_type == ".pkl":
        try:
            return joblib.load(file_path), True, "Success"
        except Exception as e:
            if isinstance(e, Warning):
                return e, False, "Warning"
            else:
                return e, False, "Error"
    else:
        return None, False  # サポートされていない拡張子の場合はNoneを返す
