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
        MainWindow.resize(640, 386)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.view_label = QtWidgets.QLabel(self.centralwidget)
        self.view_label.setGeometry(QtCore.QRect(180, 30, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(36)
        self.view_label.setFont(font)
        self.view_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.view_label.setAlignment(QtCore.Qt.AlignCenter)
        self.view_label.setObjectName("view_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(270, 30, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(36)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("color: rgb(128, 128, 128);")
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.pname_inp = QtWidgets.QTextEdit(self.centralwidget)
        self.pname_inp.setGeometry(QtCore.QRect(240, 160, 261, 31))
        self.pname_inp.setStyleSheet("background-color: rgb(189, 187, 191);\n"
"border-radius: 5px;\n"
"")
        self.pname_inp.setObjectName("pname_inp")
        self.pname_label = QtWidgets.QLabel(self.centralwidget)
        self.pname_label.setGeometry(QtCore.QRect(30, 150, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(24)
        self.pname_label.setFont(font)
        self.pname_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.pname_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pname_label.setObjectName("pname_label")
        self.mssg_label = QtWidgets.QLabel(self.centralwidget)
        self.mssg_label.setGeometry(QtCore.QRect(20, 100, 441, 51))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.mssg_label.setFont(font)
        self.mssg_label.setStyleSheet("color: rgb(128, 128, 128);")
        self.mssg_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mssg_label.setObjectName("mssg_label")
        self.viewButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewButton.setGeometry(QtCore.QRect(510, 140, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.viewButton.setFont(font)
        self.viewButton.setStyleSheet("background-color: green;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 30px;\n"
"border-color: green;\n"
"padding: 4px;\n"
"color: white;\n"
"")
        self.viewButton.setObjectName("viewButton")
        self.passNameOut = QtWidgets.QLabel(self.centralwidget)
        self.passNameOut.setGeometry(QtCore.QRect(50, 200, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.passNameOut.setFont(font)
        self.passNameOut.setStyleSheet("color: rgb(128, 128, 128);")
        self.passNameOut.setAlignment(QtCore.Qt.AlignCenter)
        self.passNameOut.setObjectName("passNameOut")
        self.websiteOut = QtWidgets.QLabel(self.centralwidget)
        self.websiteOut.setGeometry(QtCore.QRect(40, 240, 451, 31))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.websiteOut.setFont(font)
        self.websiteOut.setStyleSheet("color: rgb(128, 128, 128);")
        self.websiteOut.setAlignment(QtCore.Qt.AlignCenter)
        self.websiteOut.setObjectName("websiteOut")
        self.usernameOut = QtWidgets.QLabel(self.centralwidget)
        self.usernameOut.setGeometry(QtCore.QRect(40, 280, 451, 21))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.usernameOut.setFont(font)
        self.usernameOut.setStyleSheet("color: rgb(128, 128, 128);")
        self.usernameOut.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameOut.setObjectName("usernameOut")
        self.passwordOut = QtWidgets.QLabel(self.centralwidget)
        self.passwordOut.setGeometry(QtCore.QRect(40, 310, 451, 31))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.passwordOut.setFont(font)
        self.passwordOut.setStyleSheet("color: rgb(128, 128, 128);")
        self.passwordOut.setAlignment(QtCore.Qt.AlignCenter)
        self.passwordOut.setObjectName("passwordOut")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.viewButton.clicked.connect(lambda: self.findPass(self.pname_inp.toPlainText(),self.websiteOut,self.usernameOut,self.passwordOut))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def findPass(self, name, websiteOut, userOut, passOut):
        elist = decodeList()
        flag = False
        for i in range(len(elist)):
            if name == elist[i].split()[0]:
                flag = True
                websiteOut.setText("Website: "+elist[i].split()[1])
                userOut.setText("Username: "+ elist[i].split()[2])
                passOut.setText("Password: "+ elist[i].split()[3])
        if not flag:
            websiteOut.setText("")
            userOut.setText("Password Name Does Not Exist Try Again")
            passOut.setText("")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "View Password"))
        self.view_label.setText(_translate("MainWindow", "View"))
        self.password_label.setText(_translate("MainWindow", "Password:"))
        self.pname_inp.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pname_label.setText(_translate("MainWindow", "Password Name:"))
        self.mssg_label.setText(_translate("MainWindow", "Enter the name of the password you wish to view:"))
        self.viewButton.setText(_translate("MainWindow", "View"))
        self.passNameOut.setText(_translate("MainWindow", ""))
        self.websiteOut.setText(_translate("MainWindow", ""))
        self.usernameOut.setText(_translate("MainWindow", ""))
        self.passwordOut.setText(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
