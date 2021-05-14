# readability-checker
This is Readability, a python desktop app that will find the appropriate reeading level of a file eg: 8 grade, 9th grade etc.

# Getting Started
- In your terminal first ensure you are in the correct directory and python and pip are installed.
- Then run the following to install the requied python modules if you are using MacOS or any distribution of Linux:
```
./requirements.sh
```
- If you are on Windows run:
```
.\requirements.bat
```
- And then to run the actual App run in the same terminal (All though you can the absolute path of python instead of `python` ):
```
python main.py
```

# Note:
- This will find the readability level of a file on the basis of grammar used. And **NOT** on the basis of scientific dificulty for instance.
- It is using the [Coleman Liau Index](https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index)
- The sample folders contains some sample txt, pdf and docxs files that you might want to use.

# Acknowledgements:
- Photo by [Fallon Michael](https://unsplash.com/photos/qmlGWIaIgpo) on [Unsplash](https://unsplash.com/)
- Idea for this project from [Coleman Liau Index on Wikipedia](https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index)
- Some code was was used from:
  - [StackOverFlow](https://stackoverflow.com/questions/2349991/how-to-import-other-python-files)
  - [PyQt Documentation](https://doc.qt.io/qt.html#qt5)
  - [Pdf Miner Six Documentation](https://pdfminersix.readthedocs.io/en/latest/tutorial/composable.html)
  - [Python Docx Documentation](https://python-docx.readthedocs.io/en/latest/)
  - [Kite](https://www.kite.com/python/answers/how-to-check-the-type-of-a-file-in-python)
