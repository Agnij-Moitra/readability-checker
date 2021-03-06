# Readability-Checker
This is Readability, a python desktop app that will find the appropriate reeading level of a file eg: 8 grade, 9th grade etc.
# Note:
- **This will find the readability level of a file on the basis of grammar used. And NOT on the basis of scientific dificulty for instance.**
- It is using the [Coleman Liau Index](https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index)
- The sample folders contains some sample txt, pdf and docxs files that you might want to use.
- **If you are on Windows for some reason the texts in the edges won't appear. But it works perfectly fine on other OS(s).**

# Getting Started
1) In your terminal first ensure you are in the correct directory, and Python 3 and pip are installed.
## For MacOS and Linux:
```
./requirements.sh
```
2) And then to run the actual App run in the same terminal (All though you can the absolute path of python instead of `python` ):
```
python main.py
```
If this doesn't work for some reason then run:
```
python3 main.py
```
## For Windows:
1) In your Command Prompt:
```
.\requirements.bat
```
2) Now to run the app:
```
python main.py
```

# Acknowledgements:
- Photo by [Fallon Michael](https://unsplash.com/photos/qmlGWIaIgpo) on [Unsplash](https://unsplash.com/)
- This is inspired from [Coleman Liau Index on Wikipedia](https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index)
- The PDF named [conda-sheet](https://github.com/Agnij-Moitra/readability-checker/blob/main/sample-pdfs/conda-sheet.pdf) is directly from [Anaconda's website](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)
- Some code was was used from:
  - [StackOverFlow](https://stackoverflow.com/questions/2349991/how-to-import-other-python-files)
  - [PyQt Documentation](https://doc.qt.io/qt.html#qt5)
  - [Pdf Miner Six Documentation](https://pdfminersix.readthedocs.io/en/latest/tutorial/composable.html)
  - [Python Docx Documentation](https://python-docx.readthedocs.io/en/latest/)
  - [Kite](https://www.kite.com/python/answers/how-to-check-the-type-of-a-file-in-python)
