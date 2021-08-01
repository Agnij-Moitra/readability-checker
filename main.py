import importlib.util
import os
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import resolve1
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdftypes import PDFNotImplementedError
from io import StringIO
from docx import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):

    def load_module(self, file_name, module_name):
        spec = importlib.util.spec_from_file_location(module_name, file_name)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module

    def main(self, path, extension):
        supported_ex = [".txt", ".pdf", ".docx", ".epub"]

        if extension not in supported_ex:
            self.show_popup("Not supported",
                            f"{extension} is not supported", "warning")

        if extension == ".txt":
            txtmod = self.load_module("TxtFile.py", "main")
            index = txtmod.main(path)
            if "404:" not in index:
                self.show_popup(
                    "Readability", f"Your File's Readability index is {index}", "info")
            else:
                self.show_popup("File Error", "File is empty", "warning")

        if extension == ".pdf":
            txtmod = self.load_module("PdfFile.py", "main")
            # if "Upgrade to more" in str(txtmod):
            #     self.show_popup(
            #         "Readability", "Sorry you need to upgrade to premium in order to scan more than 200 pages", "info")

            #     return None

            index = txtmod.main(path)
            if "404:" not in index:
                self.show_popup(
                    "Readability", f"Your File's Readability index is {index}", "info")
            else:
                self.show_popup("File Error", "File is empty", "warning")

        if extension == ".docx":
            txtmod = self.load_module("docxfile.py", "main")
            index = txtmod.main(path)
            if "404:" not in str(index):
                self.show_popup(
                    "Readability", f"Your File's Readability index is {index}", "info")
            else:
                self.show_popup("File Error", "File is empty", "warning")

        if extension == ".epub":
            txtmod = self.load_module("epub.py", "main")
            index = txtmod.main(path)
            if "404:" not in str(index):
                self.show_popup(
                    "Readability", f"Your File's Readability index is {index}", "info")
            else:
                self.show_popup("File Error", "File is empty", "warning")


    def show_popup(self, title, content, type):
        msg = QMessageBox()
        msg.setWindowTitle(str(title))
        msg.setText(str(content))

        if type == "info":
            msg.setIcon(QMessageBox.Information)

        if type == "warning":
            msg.setIcon(QMessageBox.Warning)

        exit_show_popup = msg.exec_()

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        return filename[0]

    def pushButton_handler(self):
        file_path = self.open_dialog_box()
        file_extension = os.path.splitext(file_path)
        self.main(file_path, file_extension[1])

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1271, 851)
        MainWindow.setFixedSize(1271, 851)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(-20, -30, 1331, 861))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("images/susan-q-yin-2JIvboGLeho-unsplash.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410 - 150, 35, 821 - 75, 101))
        self.label.setStyleSheet("font: 30pt \"Arial\";\n"
                                "color: white;\n"
                                "text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;\n"
                                "border-radius: 25px;\n"
                                "background: rgb(255, 0, 0, 0.6);\n"
                                "padding: 20px;\n"
                                "font-family: Garamond, serif;\n"
                                "width: 200px;\n"
                                "height: 150px;\n"
                                "border-style: outset;\n"
                                "font-weight: bold;\n"
                                "border-width: 2px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 150, 851, 500))
        self.label_2.setStyleSheet("font: 30pt \"Arial\";\n"
                                    "color: white;\n"
                                    "text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;\n"
                                    "border-radius: 25px;\n"
                                    "background: rgb(255, 0, 0, 0.6);\n"
                                    "padding: 20px;\n"
                                    "width: 200px;\n"
                                    "height: 150px;\n"
                                    "border-style: outset;\n"
                                    "border-width: 2px;\n"
                                    "font-family: Garamond, serif;\n"
                                    "font-weight: 10000;\n")

        self.label_2.setObjectName("label_2")
        self.label_2.setWordWrap(True)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 660, 491, 101))
        self.pushButton.setStyleSheet("font: 30pt;\n"
                                    "color: white;\n"
                                    "text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;\n"
                                    "border-radius: 25px;\n"
                                    "background: rgb(255, 0, 0, 0.6);\n"
                                    "padding: 20px;\n"
                                    "width: 200px;\n"
                                    "height: 150px;\n"
                                    "border-style: outset;\n"
                                    "font-family: Garamond, serif;\n"
                                    "border-color: black;\n"
                                    "font-weight: 5000;\n"
                                    "border-width: 2px;\n")

        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1271, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.pushButton_handler)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Readability", "Empirical Reading Co-Pilot 📚"))
        self.label.setText(_translate("MainWindow", "Empirical Reading Co-Pilot 📚"))
        self.label_2.setText(_translate("MainWindow", "This will use the Coleman–Liau index to check the readability of a particular file. NOTE It will find the readability of the file on the basis of grammar used and NOT the basis of scientific difficulty. As of now .txt, .pdf and .docx .epub files are supported."))
        self.pushButton.setText(_translate("MainWindow", "Add File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    