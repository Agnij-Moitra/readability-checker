import sys
import importlib.util
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdftypes import PDFNotImplementedError


def main(pdf_path):
    # importing readability.py
    readability = load_module("readability-algo.py", "main")
    pdf_text = str(convert_pdf_to_string(pdf_path))

    if pdf_text == "404: Not Found":
        return "404: Not Found"

    if pdf_text == "404: File Extension Doesn't Match":
        return "404: File Extension Doesn't Match"

    readindex = readability.main(pdf_text)
    return readindex


'''
Reference for convert_pdf_to_string : https://pdfminersix.readthedocs.io/en/latest/tutorial/composable.html#extract-text-from-a-pdf-using-python-part-2
'''


def convert_pdf_to_string(file_path):
    try:
        output_string = StringIO()
        try:
            with open(file_path, 'rb') as in_file:
                parser = PDFParser(in_file)
                doc = PDFDocument(parser)
                rsrcmgr = PDFResourceManager()
                device = TextConverter(
                    rsrcmgr, output_string, laparams=LAParams())
                interpreter = PDFPageInterpreter(rsrcmgr, device)
                for page in PDFPage.create_pages(doc):
                    interpreter.process_page(page)

            return(output_string.getvalue())

        except FileNotFoundError:
            return "404: Not Found"

    except:
        return "404: File Extension Doesn't Match"


def load_module(file_name, module_name):

    spec = importlib.util.spec_from_file_location(module_name, file_name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module
