

# main window for QuickPass which offers the user to upload files, enter a manual password, or use face id to open
# the app
from PyQt5 import QtCore, QtGui, QtWidgets
import os


     # prompts the face recognition code to open once the user clicks on face ID option in the GUI
class Ui_MainWindow(object):
    def face_rec (self):
        os.system("python3 face_detection_cli.py")

    # initializes the code for the gui application for quickPass
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.questionHeader = QtWidgets.QTextEdit(self.centralwidget)
        self.questionHeader.setGeometry(QtCore.QRect(100, 150, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.questionHeader.setFont(font)
        self.questionHeader.setStyleSheet("border-radius: 15 px;")
        self.questionHeader.setObjectName("questionHeader")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(20, 10, 71, 71))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("key.png"))
        self.logo.setObjectName("logo")
        self.face_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.face_label_2.setGeometry(QtCore.QRect(260, 10, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(55)
        self.face_label_2.setFont(font)
        self.face_label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.face_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.face_label_2.setObjectName("face_label_2")
        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(90, 10, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(55)
        self.pass_label.setFont(font)
        self.pass_label.setStyleSheet("color: rgb(128, 128, 128);")
        self.pass_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_label.setObjectName("pass_label")
        self.upload_label = QtWidgets.QPushButton(self.centralwidget)
        self.upload_label.setEnabled(False)
        self.upload_label.setGeometry(QtCore.QRect(110, 210, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.upload_label.setFont(font)
        self.upload_label.setAutoFillBackground(False)
        self.upload_label.setStyleSheet("background-color: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30px;\n"
"border-color: white;\n"
"padding: 4px;\n"
"color: red;")
        self.upload_label.setCheckable(False)
        self.upload_label.setAutoDefault(True)
        self.upload_label.setObjectName("upload_label")
        self.manual_label = QtWidgets.QPushButton(self.centralwidget)
        self.manual_label.setEnabled(False)
        self.manual_label.setGeometry(QtCore.QRect(360, 210, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.manual_label.setFont(font)
        self.manual_label.setAutoFillBackground(False)
        self.manual_label.setStyleSheet("background-color: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30px;\n"
"border-color: white;\n"
"padding: 4px;\n"
"color: red;")
        self.manual_label.setCheckable(False)
        self.manual_label.setAutoDefault(True)
        self.manual_label.setObjectName("manual_label")
        self.face_label = QtWidgets.QPushButton(self.centralwidget)
        self.face_label.setGeometry(QtCore.QRect(90, 300, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.face_label.setFont(font)
        self.face_label.setAutoFillBackground(False)
        self.face_label.setStyleSheet("background-color: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30px;\n"
"border-color: white;\n"
"padding: 4px;\n"
"color: red;")

        self.face_label.setObjectName("face_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.face_label.clicked.connect(self.face_rec)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.questionHeader.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:17pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">What would you like to do today?</p></body></html>"))
        self.face_label_2.setText(_translate("MainWindow", "Pass"))
        self.pass_label.setText(_translate("MainWindow", "Quick"))
        self.upload_label.setText(_translate("MainWindow", "Upload Files"))
        self.manual_label.setText(_translate("MainWindow", "Manual Password"))
        self.face_label.setText(_translate("MainWindow", "Face ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

