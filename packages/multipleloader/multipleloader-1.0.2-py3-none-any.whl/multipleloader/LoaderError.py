class MultipleLoaderError(Exception):
    def __init__(self, arg=""):
        self.arg = arg

class PathEmptyError(MultipleLoaderError):
    def __str__(self):
        return f"[File Error] File path is empty"

class PathNotFoundError(MultipleLoaderError):
    def __str__(self):
        return f"[File Error] No file path: '{self.arg}'"

class ExtensionSupportError(MultipleLoaderError):
    def __str__(self):
        return f"[File Error] This extension is not supported: '{self.arg}'"

class LibraryNotFoundError(MultipleLoaderError):
    def __str__(self):
        return f"[Library Error] The specified library is not supported or is misspelled: '{self.arg}'"

class LoadingError(MultipleLoaderError):
    def __str__(self):
        return f"[File Error] Cannot open file, and see errors in library: \n│\n└──────[{self.arg[0]}]: {self.arg[1]}\n"

class LoadingWarning(MultipleLoaderError):
    def __str__(self):
        return f"[File Warning] A warning is issued when loading a file. See the warning statement in the library for details: \n│\n└──────[{self.arg[0]}]: {self.arg[1]}\n"

