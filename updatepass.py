# Imports the dependencies
from PyQt5 import QtCore, QtGui, QtWidgets
from cryptography.fernet import Fernet

# Encryption Key
key = 'B1kBgQFFJvRR369BV_ANoIFMaUemm16F-7JfEehj6_A='

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
        MainWindow.resize(658, 392)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(320, 40, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(36)
        self.pass_label.setFont(font)
        self.pass_label.setStyleSheet("color: rgb(128, 128, 128);")
        self.pass_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_label.setObjectName("pass_label")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(30, 230, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(24)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.website_inp = QtWidgets.QTextEdit(self.centralwidget)
        self.website_inp.setGeometry(QtCore.QRect(250, 170, 261, 51))
        self.website_inp.setStyleSheet("background-color: rgb(189, 187, 191);\n"
                                       "border-radius: 5px;\n"
                                       "")
        self.website_inp.setObjectName("website_inp")
        self.pname_label = QtWidgets.QLabel(self.centralwidget)
        self.pname_label.setGeometry(QtCore.QRect(30, 110, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(24)
        self.pname_label.setFont(font)
        self.pname_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.pname_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pname_label.setObjectName("pname_label")
        self.username_inp = QtWidgets.QTextEdit(self.centralwidget)
        self.username_inp.setGeometry(QtCore.QRect(250, 240, 261, 31))
        self.username_inp.setStyleSheet("background-color: rgb(189, 187, 191);\n"
                                        "border-radius: 5px;\n"
                                        "")
        self.username_inp.setObjectName("username_inp")
        self.updateButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateButton.setGeometry(QtCore.QRect(530, 290, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.updateButton.setFont(font)
        self.updateButton.setStyleSheet("background-color: green;\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 30px;\n"
                                        "border-color: green;\n"
                                        "padding: 4px;\n"
                                        "color: white;\n"
                                        "")
        self.updateButton.setObjectName("updateButton")
        self.update_label = QtWidgets.QLabel(self.centralwidget)
        self.update_label.setGeometry(QtCore.QRect(190, 40, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(36)
        self.update_label.setFont(font)
        self.update_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.update_label.setAlignment(QtCore.Qt.AlignCenter)
        self.update_label.setObjectName("update_label")
        self.password_inp = QtWidgets.QTextEdit(self.centralwidget)
        self.password_inp.setGeometry(QtCore.QRect(250, 310, 261, 31))
        self.password_inp.setStyleSheet("background-color: rgb(189, 187, 191);\n"
                                        "border-radius: 5px;\n"
                                        "")
        self.password_inp.setObjectName("password_inp")
        self.pname_inp = QtWidgets.QTextEdit(self.centralwidget)
        self.pname_inp.setGeometry(QtCore.QRect(250, 120, 261, 31))
        self.pname_inp.setStyleSheet("background-color: rgb(189, 187, 191);\n"
                                     "border-radius: 5px;\n"
                                     "")
        self.pname_inp.setObjectName("pname_inp")
        self.passinp_label = QtWidgets.QLabel(self.centralwidget)
        self.passinp_label.setGeometry(QtCore.QRect(30, 300, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(24)
        self.passinp_label.setFont(font)
        self.passinp_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.passinp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.passinp_label.setObjectName("passinp_label")
        self.website_label = QtWidgets.QLabel(self.centralwidget)
        self.website_label.setGeometry(QtCore.QRect(30, 160, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(24)
        self.website_label.setFont(font)
        self.website_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.website_label.setAlignment(QtCore.Qt.AlignCenter)
        self.website_label.setObjectName("website_label")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(530, 100, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.searchButton.setFont(font)
        self.searchButton.setStyleSheet("background-color: green;\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 30px;\n"
                                        "border-color: green;\n"
                                        "padding: 4px;\n"
                                        "color: white;\n"
                                        "")
        self.searchButton.setObjectName("searchButton")
        self.errormssg = QtWidgets.QLabel(self.centralwidget)
        self.errormssg.setGeometry(QtCore.QRect(10, 200, 641, 81))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(36)
        self.errormssg.setFont(font)
        self.errormssg.setStyleSheet("color: rgb(255, 0, 0);")
        self.errormssg.setAlignment(QtCore.Qt.AlignCenter)
        self.errormssg.setObjectName("errormssg")
        self.success_label = QtWidgets.QLabel(self.centralwidget)
        self.success_label.setGeometry(QtCore.QRect(70, 360, 511, 31))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(24)
        self.success_label.setFont(font)
        self.success_label.setStyleSheet("color: rgb(128, 128, 128);")
        self.success_label.setText("")
        self.success_label.setAlignment(QtCore.Qt.AlignCenter)
        self.success_label.setObjectName("success_label")
        self.errormssg.raise_()
        self.pass_label.raise_()
        self.username_label.raise_()
        self.website_inp.raise_()
        self.pname_label.raise_()
        self.username_inp.raise_()
        self.updateButton.raise_()
        self.update_label.raise_()
        self.password_inp.raise_()
        self.pname_inp.raise_()
        self.passinp_label.raise_()
        self.website_label.raise_()
        self.searchButton.raise_()
        self.success_label.raise_()
        self.website_label.hide()
        self.website_inp.hide()
        self.username_inp.hide()
        self.username_label.hide()
        self.password_inp.hide()
        self.passinp_label.hide()
        self.updateButton.hide()
        self.errormssg.hide()
        MainWindow.setCentralWidget(self.centralwidget)

        # Find Pass Button Trigger
        self.searchButton.clicked.connect(lambda: self.findPass(self.pname_inp.toPlainText()))
        # Update Button Trigger
        self.updateButton.clicked.connect(lambda: self.updatePass(self.pname_inp.toPlainText(), self.website_inp.toPlainText(), self.username_inp.toPlainText(), self.password_inp.toPlainText()))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # findPass checks if a specified pass name is in the directory
    def findPass(self, name):
        elist = decodeList()
        flag = False
        for i in range(len(elist)):
            if name == elist[i].split()[0]:
                flag = True
                self.errormssg.hide()
                self.website_label.show()
                self.website_inp.show()
                self.username_inp.show()
                self.username_label.show()
                self.password_inp.show()
                self.passinp_label.show()
                self.updateButton.show()
                self.success_label.hide()
        if not flag:
            self.errormssg.show()
            self.website_label.hide()
            self.website_inp.hide()
            self.username_inp.hide()
            self.username_label.hide()
            self.password_inp.hide()
            self.passinp_label.hide()
            self.updateButton.hide()
            self.success_label.hide()

    # updatePass changes the properties of the password entry in the directory
    def updatePass(self, name, website, username, password):
        elist = decodeList()
        for p in range(len(elist)):
            if name == elist[p].split()[0]:
                everything=name+" "+website+" "+username+" "+password
                elist[p]=everything
                f = Fernet(key)
        open('passmanager.txt', 'w').close()
        with open('passmanager.txt', 'a') as file:
            for x in range(len(elist)):
                mssg = f.encrypt(elist[x].encode())
                file.write(mssg.decode() + '\n')
        self.success_label.setText("Password has been updated!")
        self.success_label.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Update Password"))
        self.pass_label.setText(_translate("MainWindow", "Password:"))
        self.username_label.setText(_translate("MainWindow", "Username:"))
        self.website_inp.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pname_label.setText(_translate("MainWindow", "Password Name:"))
        self.username_inp.setHtml(_translate("MainWindow",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.updateButton.setText(_translate("MainWindow", "Update"))
        self.update_label.setText(_translate("MainWindow", "Update"))
        self.password_inp.setHtml(_translate("MainWindow",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pname_inp.setHtml(_translate("MainWindow",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.passinp_label.setText(_translate("MainWindow", "Password:"))
        self.website_label.setText(_translate("MainWindow", "Website:"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.errormssg.setText(_translate("MainWindow", "Invalid Password Name Try Again"))

# Initialize the GUI
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
