# Import the dependencies
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime, date
import os

# Gets the Date Time Information
today = date.today()
date = today.strftime("%B %d, %Y")
now = datetime.now()
current_time = now.strftime("%H:%M")

# GUI Properties
class Ui_QuickPass(object):
    # Button Functions - opens a specified python file using the terminal command
    def openAdd(self):
        os.system('python3 addpass.py')
    def openDelete(self):
        os.system('python3 deletepass.py')
    def openView(self):
        os.system('python3 viewpass.py')
    def openUpdate(self):
        os.system('python3 updatepass.py')

    def setupUi(self, QuickPass):
        QuickPass.setObjectName("QuickPass")
        QuickPass.resize(620, 387)
        QuickPass.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(QuickPass)
        self.centralwidget.setObjectName("centralwidget")
        self.DeletePass = QtWidgets.QPushButton(self.centralwidget)
        self.DeletePass.setGeometry(QtCore.QRect(70, 290, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.DeletePass.setFont(font)
        self.DeletePass.setStyleSheet("background-color: white;\n"
                                      "border-style: outset;\n"
                                      "border-width: 2px;\n"
                                      "border-radius: 30px;\n"
                                      "border-color: grey;\n"
                                      "padding: 4px;\n"
                                      "color: red;\n"
                                      "")
        self.DeletePass.setObjectName("DeletePass")
        self.quick_label = QtWidgets.QLabel(self.centralwidget)
        self.quick_label.setGeometry(QtCore.QRect(70, -10, 221, 111))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(55)
        font.setItalic(False)
        self.quick_label.setFont(font)
        self.quick_label.setAutoFillBackground(False)
        self.quick_label.setStyleSheet("color: rgb(128, 128, 128);\n"
                                       "background-color: rgb(255, 255, 255);")
        self.quick_label.setAlignment(QtCore.Qt.AlignCenter)
        self.quick_label.setObjectName("quick_label")
        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(260, 0, 111, 91))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(55)
        font.setItalic(False)
        self.pass_label.setFont(font)
        self.pass_label.setAutoFillBackground(False)
        self.pass_label.setStyleSheet("color: rgb(255, 0, 0);\n"
                                      "background-color: rgb(255, 255,255);")
        self.pass_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_label.setObjectName("pass_label")
        self.Icon = QtWidgets.QLabel(self.centralwidget)
        self.Icon.setEnabled(False)
        self.Icon.setGeometry(QtCore.QRect(10, 0, 81, 101))
        self.Icon.setText("")
        self.Icon.setPixmap(QtGui.QPixmap("key.png"))
        self.Icon.setObjectName("Icon")
        self.mssg_label = QtWidgets.QLabel(self.centralwidget)
        self.mssg_label.setGeometry(QtCore.QRect(20, 100, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(24)
        self.mssg_label.setFont(font)
        self.mssg_label.setStyleSheet("color: rgb(128, 128, 128);")
        self.mssg_label.setObjectName("mssg_label")
        self.UpdatePass = QtWidgets.QPushButton(self.centralwidget)
        self.UpdatePass.setGeometry(QtCore.QRect(340, 290, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.UpdatePass.setFont(font)
        self.UpdatePass.setStyleSheet("background-color: white;\n"
                                      "border-style: outset;\n"
                                      "border-width: 2px;\n"
                                      "border-radius: 30px;\n"
                                      "border-color: grey;\n"
                                      "padding: 4px;\n"
                                      "color: red;\n"
                                      "")
        self.UpdatePass.setObjectName("UpdatePass")
        self.ViewPass = QtWidgets.QPushButton(self.centralwidget)
        self.ViewPass.setGeometry(QtCore.QRect(340, 170, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.ViewPass.setFont(font)
        self.ViewPass.setStyleSheet("background-color: white;\n"
                                    "border-style: outset;\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 30px;\n"
                                    "border-color: grey;\n"
                                    "padding: 4px;\n"
                                    "color: red;\n"
                                    "")
        self.ViewPass.setObjectName("ViewPass")
        self.AddPass = QtWidgets.QPushButton(self.centralwidget)
        self.AddPass.setGeometry(QtCore.QRect(70, 170, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(18)
        self.AddPass.setFont(font)
        self.AddPass.setStyleSheet("background-color: white;\n"
                                   "border-style: outset;\n"
                                   "border-width: 2px;\n"
                                   "border-radius: 30px;\n"
                                   "border-color: grey;\n"
                                   "padding: 4px;\n"
                                   "color: red;\n"
                                   "")
        self.AddPass.setObjectName("AddPass")
        self.date_label = QtWidgets.QLabel(self.centralwidget)
        self.date_label.setGeometry(QtCore.QRect(380, 0, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(24)
        self.date_label.setFont(font)
        self.date_label.setStyleSheet("color: rgb(128, 128, 128);")
        self.date_label.setAlignment(QtCore.Qt.AlignCenter)
        self.date_label.setObjectName("date_label")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(380, 40, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Futura")
        font.setPointSize(24)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("color: rgb(128, 128, 128);")
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        QuickPass.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(QuickPass)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        QuickPass.setStatusBar(self.statusbar)

        # Button triggers corresponding functions
        self.AddPass.clicked.connect(self.openAdd)
        self.DeletePass.clicked.connect(self.openDelete)
        self.ViewPass.clicked.connect(self.openView)
        self.UpdatePass.clicked.connect(self.openUpdate)

        self.retranslateUi(QuickPass)
        QtCore.QMetaObject.connectSlotsByName(QuickPass)

    def retranslateUi(self, QuickPass):
        _translate = QtCore.QCoreApplication.translate
        QuickPass.setWindowTitle(_translate("QuickPass", "QuickPass"))
        self.DeletePass.setText(_translate("QuickPass", "Delete Password(s)"))
        self.quick_label.setText(_translate("QuickPass", "Quick"))
        self.pass_label.setText(_translate("QuickPass", "Pass"))
        self.mssg_label.setText(_translate("QuickPass", "What would you like to do today:"))
        self.UpdatePass.setText(_translate("QuickPass", "Update Password"))
        self.ViewPass.setText(_translate("QuickPass", "View Password(s)"))
        self.AddPass.setText(_translate("QuickPass", "Add Password"))
        self.date_label.setText(_translate("QuickPass", date))
        self.time_label.setText(_translate("QuickPass", current_time))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    QuickPass = QtWidgets.QMainWindow()
    ui = Ui_QuickPass()
    ui.setupUi(QuickPass)
    QuickPass.show()
    sys.exit(app.exec_())
