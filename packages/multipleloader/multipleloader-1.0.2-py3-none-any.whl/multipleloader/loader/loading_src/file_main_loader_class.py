import concurrent.futures
import multiprocessing
import os
import time

from ...LoaderError import *

class FileLoader:
    def __init__(self):
        # 共有変数を作成
        self.FINISHER_FLAG = multiprocessing.Value('i', 0)
        self.str_c = 1
        self.str_c_max = 8
        self.sub_str_c = 0
        self.sub_str_c_max = 1500
        self.mode = 1
        self.error_checker = True
        self.error_type = ""

    def file_loader_func(self, file_path, ext_type, load_func, encoding):
        # 関数file_loader_funcの処理を定義
        loaded_data, self.error_checker, self.error_type = load_func(file_path=file_path, ext_type=ext_type, encoding=encoding)
        self.FINISHER_FLAG.value = 1
        return loaded_data

    def load_timer(self, file_name, lib_name):
        # 共有変数の値を参照
        sub_str_c = self.sub_str_c
        sub_str_c_max = self.sub_str_c_max

        if self.mode == 1:
            cui_pattern_1 = ["⠸", "⢰", "⣠", "⣄", "⡆", "⠇", "⠋", "⠙"]
            cui_pattern_1_len = len(cui_pattern_1)
            c_1 = 0
            while self.FINISHER_FLAG.value == 0:
                print("\r" + f"Library [{lib_name}] " + str("─"*c_1 + ">>").ljust(cui_pattern_1_len+2) + f" {file_name} [ {cui_pattern_1[c_1]}  ] ", end="")
                if sub_str_c == sub_str_c_max:
                    sub_str_c = 0
                    if c_1 == cui_pattern_1_len-1:
                        c_1 = 0
                    else:
                        c_1 += 1
                else:
                    sub_str_c += 1
            if self.error_checker == True:
                print("\r" + f"Library [{lib_name}] " + "─"*cui_pattern_1_len + ">>" + f" {file_name} [ " + "\033[32m" + "✔ " + "\033[0m" + " ] ", end="")  # green
                return 1
            elif self.error_checker == False:
                print("\r" + f"Library [{lib_name}] " + "─"*cui_pattern_1_len + ">>" + f" {file_name} [ " + "\033[31m" + "✘ " + "\033[0m" + " ] ", end="")  # red
                print("\n")
                return 100
            
        elif self.mode == 2:
            str_c = self.str_c
            str_c_max = self.str_c_max
            while (self.FINISHER_FLAG.value == 0) or (str_c != str_c_max):
                print("\r" + f"Library [{lib_name}]: {file_name} " + str("─"*str_c + ">>").ljust(str_c_max+2) + " [ DATA ] ", end="")
                self.FINISHER_FLAG.value = self.FINISHER_FLAG.value
                if sub_str_c == sub_str_c_max:
                    sub_str_c = 0
                    if str_c == str_c_max:
                        str_c = 0
                    else:
                        str_c += 1
                else:
                    sub_str_c += 1
            if self.error_checker == True:
                print("\r" + f"Library [{lib_name}]: {file_name} " + str("─"*str_c + ">>").ljust(str_c_max+2) + " [ DATA ] ────> LOADING COMPLETED ", end="")
                return 2
            elif self.error_checker == False:
                print("\r" + f"Library [{lib_name}]: {file_name} " + str("─"*str_c + ">>").ljust(str_c_max+2) + " [ DATA ] ────> LOADING FALSE ", end="")
                print("\n")
                return 200

    def file_main_loader(self, file_path, ext_type, lib_name, loader_func, encoding):
        file_name = os.path.basename(file_path)
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            # 並列処理を開始
            future1 = executor.submit(self.file_loader_func, file_path=file_path, ext_type=ext_type, load_func=loader_func, encoding=encoding)
            future2 = executor.submit(self.load_timer, file_name=file_name, lib_name=lib_name)

            # 結果を受け取る
            load_data = future1.result()
            time.sleep(1)
            if self.error_checker == False:
                if self.error_type == "Error":
                    class_name = load_data.__class__.__name__
                    raise LoadingError([class_name, load_data]) # Error
                elif self.error_type == "Warning":
                    class_name = load_data.__class__.__name__
                    raise LoadingWarning([class_name, load_data]) # Warning

            # 並列処理の完了を待つ
            concurrent.futures.wait([future1, future2])
        print("\n")
        return load_data