import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import sys
import importlib.util

blacklist = ['[document]', 'noscript', 'header', 'html', 'meta', 'head', 'input', 'script']

def main(path):
    readability = load_module("readability-algo.py", "main")
    txt = str(epub2text(path)[1].replace("\n", "").rstrip())

    if txt == "404: Not Found":
        return "404: Not Found"

    if txt == "404: File Extension Doesn't Match":
        return "404: File Extension Doesn't Match"

    readindex = readability.main(txt)
    return readindex


def epub2thtml(epub_path):
    book = epub.read_epub(epub_path)
    chapters = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())
    return chapters


def chap2text(chap):
    output = ''
    soup = BeautifulSoup(chap, 'html.parser')
    text = soup.find_all(text=True)
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    return output


def thtml2ttext(thtml):
    Output = []
    for html in thtml:
        text =  chap2text(html)
        Output.append(text)
    return Output


def epub2text(epub_path):
    chapters = epub2thtml(epub_path)
    ttext = thtml2ttext(chapters)
    return ttext


def load_module(file_name, module_name):
    spec = importlib.util.spec_from_file_location(module_name, file_name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module
