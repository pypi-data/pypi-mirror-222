import csv

def csv_loader(file_path, ext_type, encoding):
    if ext_type == ".csv":
        try:
            with open(file_path, "r", encoding=encoding) as csv_f:
                return csv.reader(csv_f), True, "Success"
        except Exception as e:
            if isinstance(e, Warning):
                return e, False, "Warning"
            else:
                return e, False, "Error"
    elif ext_type == ".tsv":
        try:
            with open(file_path, "r", encoding=encoding) as tsv_f:
                return csv.reader(tsv_f, delimiter='\t'), True, "Success"
        except Exception as e:
            if isinstance(e, Warning):
                return e, False, "Warning"
            else:
                return e, False, "Error"
    else:
        return None, False  # サポートされていない拡張子の場合はNoneを返す