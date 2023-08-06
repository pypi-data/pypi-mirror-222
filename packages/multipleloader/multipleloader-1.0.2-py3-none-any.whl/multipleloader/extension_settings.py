extensions = {

    ### csv file setup ###
    ".csv": {
        "library": {
            "csv": {
                "keys": ["csv"],
                "default_encoding": "utf-8"
            },
            "pandas": {
                "keys": ["pandas", "pd"],
                "default_encoding": "utf-8"
            }, # default
            "numpy": {
                "keys": ["numpy", "np"],
                "default_encoding": "bytes"
            }
        },
        "DEFAULT": "pandas"
    },
    
    ### tsv file setup ###
    ".tsv": {
        "library": {
            "csv": {
                "keys": ["csv"],
                "default_encoding": "utf-8"
            },
            "pandas": {
                "keys": ["pandas", "pd"],
                "default_encoding": "utf-8"
            }, # default
            "numpy": {
                "keys": ["numpy", "np"],
                "default_encoding": "bytes"
            }
        },
        "DEFAULT": "pandas"
    },

    ### json file setup ###
    ".json": {
        "library": {
            "json": {
                "keys": ["json"],
                "default_encoding": "utf-8"
            }, # default
            "pandas": {
                "keys": ["pandas", "pd"],
                "default_encoding": "utf-8"
            }
        },
        "DEFAULT": "json"
    },

    ### pickle file setup ###
    ".pickle": {
        "library": {
            "pickle": {
                "keys": ["pickle"],
                "default_encoding": "ASCII"
            }, # default
            "pandas": {
                "keys": ["pandas", "pd"],
                "default_encoding": "ASCII"
            },
            "joblib": {
                "keys": ["joblib"],
                "default_encoding": "ASCII"
            }
        },
        "DEFAULT": "pickle"
    },

    ### pkl file setup ###
    ".pkl": {
        "library": {
            "pickle": {
                "keys": ["pickle"],
                "default_encoding": "ASCII"
            }, # default
            "pandas": {
                "keys": ["pandas", "pd"],
                "default_encoding": "ASCII"
            },
            "joblib": {
                "keys": ["joblib"],
                "default_encoding": "ASCII"
            }
        },
        "DEFAULT": "pickle"
    },

    ### npy file setup ###
    ".npy": {
        "library": {
            "numpy": {
                "keys": ["numpy", "np"],
                "default_encoding": "ASCII"
            }
        },
        "DEFAULT": "numpy"
    },

    ### npz file setup ###
    ".npz": {
        "library": {
            "numpy": {
                "keys": ["numpy", "np"],
                "default_encoding": "ASCII"
            }
        },
        "DEFAULT": "numpy"
    }
}
