import sys
import os
import importlib.util
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):

    def load_module(self, file_name, module_name):
        spec = importlib.util.spec_from_file_location(module_name, file_name)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module

    def main(self, path, extension):
        supported_ex = [".txt", ".pdf", ".docx"]

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
            index = txtmod.main(path)
            if "404:" not in index:
                self.show_popup(
                    "Readability", f"Your File's Readability index is {index}", "info")
            else:
                self.show_popup("File Error", "File is empty", "warning")

        if extension == ".docx":
            txtmod = self.load_module("docxfile.py", "main")
            index = txtmod.main(path)
            if "404:" not in index:
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
        MainWindow.resize(817, 564)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 851, 581))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap(
            "images/fallon-michael-qmlGWIaIgpo-unsplash.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 10, 391, 81))
        self.label.setStyleSheet("color: white;\n"
                                 "background-color: rgb(170, 85, 0);\n"
                                 "font: bold 20pt \"Newspaper\";\n"
                                 "border-style: outset;\n"
                                 "border-width: 2px;\n"
                                 "padding: 6px;\n"
                                 "min-width: 10px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 681, 301))
        self.label_2.setStyleSheet("color: white;\n"
                                   "font: 23pt \"Newspaper\";\n"
                                   "background-color: rgb(170, 85, 0);\n"
                                   "border-style: outset;\n"
                                   "border-width: 2px;\n"
                                   "padding: 6px;\n"
                                   "min-width: 10px;")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 430, 211, 51))
        self.pushButton.setStyleSheet("color: white;\n"
                                      "background-color: rgb(170, 85, 0);\n"
                                      "font: 20pt \"Newspaper\";\n"
                                      "border-style: outset;\n"
                                      "border-width: 2px;\n"
                                      "border-radius: 10px;\n"
                                      "border-color: black;\n"
                                      "padding: 6px;\n"
                                      "min-width: 10px;")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 817, 22))
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
        MainWindow.setWindowTitle(_translate("Readability", "Readability"))
        self.label.setText(_translate("MainWindow", "Readability Checker"))
        self.label_2.setText(_translate("MainWindow", "This will use the Coleman–Liau index\n"
                                        "to check the readbility of a particular file.\n"
                                        "NOTE though It will find the readability\n"
                                        "of the file on the basis of grammar used\n"
                                        "and NOT the basis of scientific\n"
                                        "difficulty for example.\n"
                                        "As of now .txt, .pdf and .docx files are\n"
                                        "supported"))
        self.pushButton.setText(_translate("MainWindow", "Add File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
