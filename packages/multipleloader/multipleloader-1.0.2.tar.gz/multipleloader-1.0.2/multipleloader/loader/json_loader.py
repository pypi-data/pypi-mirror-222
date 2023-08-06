import json

def json_loader(file_path, ext_type, encoding):
    if ext_type == ".json":
        try:
            with open(file_path, "r", encoding=encoding) as json_f:
                json_data = json.load(json_f)
                return json_data, True, "Success"
        except Exception as e:
            if isinstance(e, Warning):
                return e, False, "Warning"
            else:
                return e, False, "Error"
    else:
        return None, False  # サポートされていない拡張子の場合はNoneを返す
