# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SignUp(object):
    def signUpAsStaff(self):
        email = self.reg_email_line.text()
        username = self.reg_username_line.text()
        password = self.reg_pass_line.text()
        conf_password = self.reg_conf_line.text()
        if (password != conf_password):
            msg = "confirm password doesn't match with your password"
            self.failedMessage("failed registration", msg)

        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='garlic93')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM ZOO.USER AS USER WHERE USER.Email = %s;", (email))
        result = cursor.fetchall()
        if (result[0] == email):
            self.failedMessage("failed registration", "this email is already existed ")
        sql_registration_query = "INSERT INTO ZOO.USER VALUES (%s, %s, %s, staff);"
        cursor.execute(sql_registration_query, (username, email, password))
        cursor.execute("INSERT INTO zoo.STAFF(username) Select U.username From User U Where U.username = %s;",
                       username)
        connection.commit()
        connection.close()

    def signUpAsVisitor(self):
        #the input data in registration screen
        email = self.reg_email_line.text()
        username = self.reg_username_line.text()
        password = self.reg_pass_line.text()
        conf_password = self.reg_conf_line.text()
        if(password != conf_password):
            msg = "confirm password doesn't match with your password"
            self.failedMessage("failed registration", msg)

        connection = pymysql.connect(host ='127.0.0.1', port = 3306, user = 'root',password='garlic93')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM ZOO.USER AS USER WHERE USER.Email = %s;", (email))
        result = cursor.fetchall()
        if(result[0]==email):
            self.failedMessage("failed registration", "this email is already existed ")
        sql_registration_query = "INSERT INTO ZOO.USER VALUES (%s, %s, %s, vistor);"
        cursor.execute(sql_registration_query, (username, email, password))
        cursor.execute("INSERT INTO zoo.VISITOR(username) Select U.username From User U Where U.username = %s;", username)
        connection.commit()
        connection.close()

    def failedMessage(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(399, 372)
        Dialog.setStyleSheet("QDialog{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(252, 175, 62, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 40, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 170, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 200, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.reg_email_line = QtWidgets.QLineEdit(Dialog)
        self.reg_email_line.setGeometry(QtCore.QRect(210, 110, 151, 25))
        self.reg_email_line.setObjectName("reg_email_line")
        self.reg_username_line = QtWidgets.QLineEdit(Dialog)
        self.reg_username_line.setGeometry(QtCore.QRect(210, 140, 151, 25))
        self.reg_username_line.setObjectName("reg_username_line")
        self.reg_pass_line = QtWidgets.QLineEdit(Dialog)
        self.reg_pass_line.setGeometry(QtCore.QRect(210, 170, 151, 25))
        self.reg_pass_line.setObjectName("reg_pass_line")
        self.reg_conf_line = QtWidgets.QLineEdit(Dialog)
        self.reg_conf_line.setGeometry(QtCore.QRect(210, 200, 151, 25))
        self.reg_conf_line.setObjectName("reg_conf_line")
        self.reg_visitor_button = QtWidgets.QPushButton(Dialog)
        self.reg_visitor_button.setGeometry(QtCore.QRect(70, 250, 121, 25))
        self.reg_visitor_button.setObjectName("reg_visitor_button")
        ############register as visitor#####################################
        self.reg_visitor_button.clicked.connect(self.signUpAsVisitor)
        ######################################################################
        self.reg_staff_button = QtWidgets.QPushButton(Dialog)
        self.reg_staff_button.setGeometry(QtCore.QRect(210, 250, 111, 25))
        self.reg_staff_button.setObjectName("reg_staff_button")
        ###############register as staff################################
        self.reg_staff_button.clicked.connect(self.signUpAsStaff)
        ###############################################################

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Atlanta Zoo Registration"))
        self.label_2.setText(_translate("Dialog", "Email"))
        self.label_3.setText(_translate("Dialog", "Username"))
        self.label_4.setText(_translate("Dialog", "Password"))
        self.label_5.setText(_translate("Dialog", "Confirm Password"))
        self.reg_visitor_button.setText(_translate("Dialog", "Register Visitor"))
        self.reg_staff_button.setText(_translate("Dialog", "Register Staff"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_SignUp()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

