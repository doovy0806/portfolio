# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginScreen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import pymysql
# from login_success import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from juntae.signup import Ui_SignUp
from Admin.adminfunc import Ui_Admin as admin
from Visitor.visitorFunctionality import  Ui_MainWindow as visitor
from Staff.staffFunctionality import Ui_Dialog as staff
class Ui_Dialog(object):
    def changeToSignUpScreen(self):
        self.signUpWindow = QtWidgets.QDialog()
        self.ui = Ui_SignUp()
        self.ui.setupUi(self.signUpWindow)
        self.signUpWindow.show()
    # def successWindowShow(self):
    #     self.successWindow = QtWidgets.QMainWindow()
    #     self.ui = Ui_MainWindow()
    #     self.ui.setupUi(self.successWindow)
    #     self.successWindow.show()
    def failedMessage(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def loginCheck(self):
        email = self.email_line.text()
        password = self.password_line.text()
        connection = pymysql.connect(host ='127.0.0.1', port = 3306, user = 'root',password='garlic93')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM ZOO.USER AS USER WHERE USER.Email = %s AND User.Password = %s;", (email, password))
        result = cursor.fetchall()
        if(len(result) > 0):
            print("login success! Welcome to the atlanta zoo")
            # self.successWindowShow()
            result = result[0][0]
            # self.username=str(result[0]["Name"])
            self.username = str(result)
            query1 = "SELECT * FROM zoo.staff where username='{}';".format(self.username)
            print(query1)
            query2 = "SELECT * FROM zoo.visitor where username='{}';".format(self.username)
            print(query2)
            cursor.execute(query1)
            result1= cursor.fetchall()
            cursor.execute(query2)
            result2 = cursor.fetchall()
            if len(result1)>0:
                self.staffWindow()
            elif len(result2)>0:
                self.visitorWindow()
            else:
                self.adminWindow()
        else:
            print("incorrect email or password. Please check whether you entered correctly. or if you are new user, please sign up")
            msg ="incorrect email or password. Please check whether you entered correctly. or if you are new user, please sign up"
            self.failedMessage("failed login", msg)
        # connection.close()
    def staffWindow(self):
        self.staffDialog = QtWidgets.QDialog()
        self.ui = staff(self.username)
        self.ui.setupUi(self.staffDialog)
        self.staffDialog.show()
    def visitorWindow(self):
        self.visitorDialog = QtWidgets.QDialog()
        self.ui = visitor(self.username)
        self.ui.setupUi(self.visitorDialog)
        self.visitorDialog.show()
    def adminWindow(self):
        self.adminDialog = QtWidgets.QDialog()
        self.ui = admin()
        self.ui.setupUi(self.adminDialog)
        self.adminDialog.show()
    def signUpCheck(self):
        self.changeToSignUpScreen()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(409, 351)
        Dialog.setStyleSheet("QDialog{\n"
                             "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(252, 175, 62, 255), stop:1 rgba(255, 255, 255, 255));\n"
                             "}")
        self.title_label = QtWidgets.QLabel(Dialog)
        self.title_label.setGeometry(QtCore.QRect(50, 30, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.username_label = QtWidgets.QLabel(Dialog)
        self.username_label.setGeometry(QtCore.QRect(50, 110, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.username_label.setFont(font)
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(Dialog)
        self.password_label.setGeometry(QtCore.QRect(50, 150, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.password_label.setFont(font)
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.email_line = QtWidgets.QLineEdit(Dialog)
        self.email_line.setGeometry(QtCore.QRect(170, 110, 151, 25))
        self.email_line.setObjectName("email_line")
        self.password_line = QtWidgets.QLineEdit(Dialog)
        self.password_line.setGeometry(QtCore.QRect(170, 150, 151, 25))
        self.password_line.setObjectName("password_line")
        self.login_button = QtWidgets.QPushButton(Dialog)
        self.login_button.setGeometry(QtCore.QRect(160, 220, 89, 25))
        self.login_button.setObjectName("login_button")
        #######################login_button event########################
        self.login_button.clicked.connect(self.loginCheck)
        ################################################################
        self.signup_button = QtWidgets.QPushButton(Dialog)
        self.signup_button.setGeometry(QtCore.QRect(160, 260, 89, 25))
        self.signup_button.setObjectName("signup_button")
        #######################signup_button event########################
        self.signup_button.clicked.connect(self.signUpCheck)
        ################################################################
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Atlanta Zoo"))
        self.title_label.setText(_translate("Dialog", "Welcome to Atlanta Zoo"))
        self.username_label.setText(_translate("Dialog", "Username"))
        self.password_label.setText(_translate("Dialog", "password"))
        self.login_button.setText(_translate("Dialog", "Login"))
        self.signup_button.setText(_translate("Dialog", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

