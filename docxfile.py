import sys
import importlib.util
import docx


def main(doc_path):
    # importing readability.py
    readability = load_module("readability-algo.py", "main")
    doc_txt = str(extract_txt(doc_path))

    if doc_txt == "404: Not File Found":
        return "404: Not File Found"

    readindex = readability.main(doc_txt)
    return readindex


def extract_txt(doc_path):
    try:
        extracted_txt = ""
        doc = docx.Document(doc_path)
        for para in doc.paragraphs:
            extracted_txt += str(para.text)
        return extracted_txt
    except:
        return "404: File Not Found"


def load_module(file_name, module_name):
    spec = importlib.util.spec_from_file_location(module_name, file_name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

