import sys
import importlib.util


def main(file_path):
    # importing readability.py
    readability = load_module("readability-algo.py", "main")

    # rasing error
    try:
        # opening the given file
        with open(file_path, 'r') as txtf:
            text = txtf.read().replace("\n", " ")
            readindex = readability.main(text)
            return readindex

    except FileNotFoundError:
        return "404: File Not Found"


def load_module(file_name, module_name):

    spec = importlib.util.spec_from_file_location(module_name, file_name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


        