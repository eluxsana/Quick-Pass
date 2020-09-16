# Import the dependencies
from PyQt5 import QtCore, QtGui, QtWidgets
from cryptography.fernet import Fernet

# Encryption Key
key='B1kBgQFFJvRR369BV_ANoIFMaUemm16F-7JfEehj6_A='

# Decodes user data and stores it into an array
def decodeList():
    with open('passmanager.txt', 'r') as file:
        encrpyted = file.read().split()
        elist = []
        f = Fernet(key)
        for x in range(len(encrpyted)):
            decrpyted = f.decrypt(encrpyted[x].encode())
            elist.append(decrpyted.decode())
        return elist

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 403)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.delete_label = QtWidgets.QLabel(self.centralwidget)
        self.delete_label.setGeometry(QtCore.QRect(180, 20, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(36)
        self.delete_label.setFont(font)
        self.delete_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.delete_label.setAlignment(QtCore.Qt.AlignCenter)
        self.delete_label.setObjectName("delete_label")
        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(300, 20, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(36)
        self.pass_label.setFont(font)
        self.pass_label.setStyleSheet("color: rgb(128, 128, 128);")
        self.pass_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_label.setObjectName("pass_label")
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(500, 30, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.delete_button.setFont(font)
        self.delete_button.setStyleSheet("background-color: green;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30px;\n"
"border-color: green;\n"
"padding: 4px;\n"
"color: white;\n"
"")
        self.delete_button.setObjectName("delete_button")
        self.pname_label = QtWidgets.QLabel(self.centralwidget)
        self.pname_label.setGeometry(QtCore.QRect(30, 130, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(24)
        self.pname_label.setFont(font)
        self.pname_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.pname_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pname_label.setObjectName("pname_label")
        self.pname_inp = QtWidgets.QTextEdit(self.centralwidget)
        self.pname_inp.setGeometry(QtCore.QRect(270, 140, 261, 31))
        self.pname_inp.setStyleSheet("background-color: rgb(189, 187, 191);\n"
"border-radius: 5px;\n"
"")
        self.pname_inp.setObjectName("pname_inp")
        self.pname_inp_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.pname_inp_2.setGeometry(QtCore.QRect(90, 210, 441, 131))
        self.pname_inp_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"")
        self.pname_inp_2.setObjectName("pname_inp_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # When button is clicked deletePass function is trigger
        self.delete_button.clicked.connect(lambda: self.deletePass(self.pname_inp.toPlainText()))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Deletes the specified password from password manager directory
    def deletePass(self, name):
        elist = decodeList()
        flag = False
        for i in range(len(elist)):
            # Checks if inputted name is in the directory and the rewrites the file without that entry
            if name == elist[i].split()[0]:
                del elist[i]
                f = Fernet(key)
                flag=True
                open('passmanager.txt', 'w').close()
                with open('passmanager.txt', 'a') as file:
                    for x in range(len(elist)):
                        mssg = f.encrypt(elist[x].encode())
                        file.write(mssg.decode() + '\n')
                self.pname_inp_2.setText("Password has been deleted.")
                break
        # If the name is not in the directory the gives error message
        if not flag:
            self.pname_inp_2.setText("Invalid Entry Try Again")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Delete Password"))
        self.delete_label.setText(_translate("MainWindow", "Delete"))
        self.pass_label.setText(_translate("MainWindow", "Password:"))
        self.delete_button.setText(_translate("MainWindow", "Delete"))
        self.pname_label.setText(_translate("MainWindow", "Password Name:"))
        self.pname_inp.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pname_inp_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

# Initialize the GUI
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
