# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StaffShowHistory.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from loadData import *

class Ui_Dialog(object):
    def __init__(self, username):
        object.__init__(self)
        self.username = username
        self.connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='garlic93')

    def tableLoad(self):
        cursor = self.connection.cursor()
        cursor.execute("USE zoo;")
        query = "SELECT name, datetime, location from zoo.show where host_staff = '{}' ; ".format(self.username)
        cursor.execute(query)
        result = cursor.fetchall()
        loadTable(self.historyListTable, result, header=['Name', 'Time', 'Exhibit'], attNo=3)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(525, 402)
        # Dialog = QtWidgets.QWidget(Dialog)
        # Dialog.setObjectName("centralwidget")
        self.staffShowHistoryLabel = QtWidgets.QLabel(Dialog)
        self.staffShowHistoryLabel.setGeometry(QtCore.QRect(190, 40, 151, 21))
        self.staffShowHistoryLabel.setObjectName("staffShowHistoryLabel")
        self.atlantaZooLabel = QtWidgets.QLabel(Dialog)
        self.atlantaZooLabel.setGeometry(QtCore.QRect(40, 40, 111, 16))
        self.atlantaZooLabel.setObjectName("atlantaZooLabel")
        self.historyListTable = QtWidgets.QTableWidget(Dialog)
        self.historyListTable.setGeometry(QtCore.QRect(40, 80, 431, 221))
        self.historyListTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.historyListTable.setObjectName("historyListTable")
        self.backButton = QtWidgets.QPushButton(Dialog)
        self.backButton.setGeometry(QtCore.QRect(200, 330, 113, 32))
        self.backButton.setObjectName("backButton")
        # Dialog.setCentralWidget(Dialog)
        # self.menubar = QtWidgets.QMenuBar(Dialog)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 525, 22))
        # self.menubar.setObjectName("menubar")
        # Dialog.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(Dialog)
        # self.statusbar.setObjectName("statusbar")
        # Dialog.setStatusBar(self.statusbar)
        self.tableLoad()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.staffShowHistoryLabel.setText(_translate("Dialog", "Staff - Show History"))
        self.atlantaZooLabel.setText(_translate("Dialog", "Atlanta Zoo"))
        self.backButton.setText(_translate("Dialog", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    # ui = Ui_Dialog()
    ui = Ui_Dialog("Heejun")
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

