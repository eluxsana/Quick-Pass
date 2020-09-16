# Import Dependencies
from PyQt5 import QtCore, QtGui, QtWidgets
import random
import string
from cryptography.fernet import Fernet

# Encryption Key
key='B1kBgQFFJvRR369BV_ANoIFMaUemm16F-7JfEehj6_A='

# Generates a random alphanumric password that is at least 16 to 32 letters long
def generatePassword():
    length = random.randint(16, 32)
    pwd = ""
    count = 0
    while count != length:
        str1= random.choice(string.ascii_uppercase)
        str2 = random.choice(string.ascii_lowercase)
        str3 = random.choice(string.digits)
        str4 = random.choice(string.punctuation)
        everything = str1 + str2 + str3 + str4
        pwd+= random.choice(everything)
        count+=1
    return pwd

# GUI Properties
class Ui_MainWindow2(object):
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 403)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(290, 30, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(36)
        self.pass_label.setFont(font)
        self.pass_label.setStyleSheet("color: rgb(128, 128, 128);")
        self.pass_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_label.setObjectName("pass_label")
        self.add_label = QtWidgets.QLabel(self.centralwidget)
        self.add_label.setGeometry(QtCore.QRect(200, 30, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(36)
        self.add_label.setFont(font)
        self.add_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.add_label.setAlignment(QtCore.Qt.AlignCenter)
        self.add_label.setObjectName("add_label")
        self.pname_inp = QtWidgets.QTextEdit(self.centralwidget)
        self.pname_inp.setGeometry(QtCore.QRect(220, 110, 261, 31))
        self.pname_inp.setStyleSheet("background-color: rgb(189, 187, 191);\n"
"border-radius: 5px;\n"
"")
        self.pname_inp.setObjectName("pname_inp")
        self.website_inp = QtWidgets.QTextEdit(self.centralwidget)
        self.website_inp.setGeometry(QtCore.QRect(220, 160, 261, 51))
        self.website_inp.setStyleSheet("background-color: rgb(189, 187, 191);\n"
"border-radius: 5px;\n"
"")
        self.website_inp.setObjectName("website_inp")
        self.username_inp = QtWidgets.QTextEdit(self.centralwidget)
        self.username_inp.setGeometry(QtCore.QRect(220, 230, 261, 31))
        self.username_inp.setStyleSheet("background-color: rgb(189, 187, 191);\n"
"border-radius: 5px;\n"
"")
        self.username_inp.setObjectName("username_inp")
        self.password_inp = QtWidgets.QTextEdit(self.centralwidget)
        self.password_inp.setGeometry(QtCore.QRect(220, 320, 261, 31))
        self.password_inp.setStyleSheet("background-color: rgb(189, 187, 191);\n"
"border-radius: 5px;\n"
"")
        self.password_inp.setObjectName("password_inp")
        self.pname_label = QtWidgets.QLabel(self.centralwidget)
        self.pname_label.setGeometry(QtCore.QRect(0, 100, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(24)
        self.pname_label.setFont(font)
        self.pname_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.pname_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pname_label.setObjectName("pname_label")
        self.website_label = QtWidgets.QLabel(self.centralwidget)
        self.website_label.setGeometry(QtCore.QRect(0, 150, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(24)
        self.website_label.setFont(font)
        self.website_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.website_label.setAlignment(QtCore.Qt.AlignCenter)
        self.website_label.setObjectName("website_label")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(0, 220, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(24)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.genpass_op = QtWidgets.QCheckBox(self.centralwidget)
        self.genpass_op.setGeometry(QtCore.QRect(230, 290, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.genpass_op.setFont(font)
        self.genpass_op.setStyleSheet("color: rgb(128, 128, 128);")
        self.genpass_op.setObjectName("genpass_op")
        self.passinp_label = QtWidgets.QLabel(self.centralwidget)
        self.passinp_label.setGeometry(QtCore.QRect(0, 290, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(24)
        self.passinp_label.setFont(font)
        self.passinp_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.passinp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.passinp_label.setObjectName("passinp_label")
        self.AddPass = QtWidgets.QPushButton(self.centralwidget)
        self.AddPass.setGeometry(QtCore.QRect(500, 40, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.AddPass.setFont(font)
        self.AddPass.setStyleSheet("background-color: green;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30px;\n"
"border-color: green;\n"
"padding: 4px;\n"
"color: white;\n"
"")
        self.AddPass.setObjectName("AddPass")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.genpass_op.stateChanged.connect(self.password_inp.hide)
        # Add Button triggers added function
        self.AddPass.clicked.connect(lambda: self.added(self.genpass_op.isChecked(),self.password_inp.toPlainText(),self.username_inp.toPlainText(),self.website_inp.toPlainText(),self.pname_inp.toPlainText()))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Stores user entry in a text file
    def added(self, chk, pass_inp, username, website, name):
        # If CheckBox is checked then generate password
        if chk:
            password=generatePassword()
        else:
            password=pass_inp
        everything = name + " " + website + " " + username + " " + password

        # Append the user data into a text file after encrypyting it using the key
        with open('passmanager.txt', 'a') as file:
            f = Fernet(key)
            encrpyted = f.encrypt(everything.encode())
            file.write(encrpyted.decode() + "\n")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Password"))
        self.pass_label.setText(_translate("MainWindow", "Password:"))
        self.add_label.setText(_translate("MainWindow", "Add"))
        self.pname_inp.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.website_inp.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.username_inp.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.password_inp.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pname_label.setText(_translate("MainWindow", "Password Name:"))
        self.website_label.setText(_translate("MainWindow", "Website:"))
        self.username_label.setText(_translate("MainWindow", "Username:"))
        self.genpass_op.setText(_translate("MainWindow", "Generate Password"))
        self.passinp_label.setText(_translate("MainWindow", "Password:"))
        self.AddPass.setText(_translate("MainWindow", "Add"))

# Initialize GUI
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
