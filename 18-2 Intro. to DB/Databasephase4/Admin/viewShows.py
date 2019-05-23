# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewshows.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from loadData import *

class Ui_Dialog(object):
    def __init__(self):
        object.__init__(self)
        self.connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='garlic93')

        cursor = self.connection.cursor()
        cursor.execute("USE zoo;")
        cursor.close()


    def loadBox(self):
        cursor = self.connection.cursor()
        cursor.execute("USE zoo;")
        query = "SELECT Name from Exhibit; "
        cursor.execute(query)
        result = cursor.fetchall()
        loadExhibit(self.exhibitBox, result)
        cursor.close()


        
    def showSearch(self):
        name = self.nameEdit.toPlainText()
        exhibit = self.exhibitBox.currentText()
        year = self.dateEdit.date().year()
        month = self.dateEdit.date().month()
        day = self.dateEdit.date().day()
        date = "{}-{}-{}".format(year, month, day)
        nextdate ="{}-{}-{}".format(year, month, day+1)


        query = "SELECT * from zoo.Show where name like '%{}%' AND location like '%{}%' AND datetime>={{ts '{} 00:00'}} AND datetime<{{ts '{} 00:00'}}; ".format(name, exhibit, date, nextdate)
        # query = "SELECT * from zoo.Show where name = '{}' AND location = '{}' AND datetime>={{ts '{} 00:00'}} AND datetime<{{ts '{} 00:00'}}; ".format(name, exhibit, date, nextdate)

        # print(query)

        cursor = self.connection.cursor()
        cursor.execute("USE zoo;")
        cursor.execute(query)
        result = cursor.fetchall()
        loadTable(self.showTable, result, ['Name', 'Date', 'Location'], 3)
        cursor.close()
    def removeShow(self):
        show = self.showTable.selectedItems()
        showIndex = self.showTable.currentIndex()
        if len(show)is not 0:
            showName = show[0].text()
            showDate = show[1].text()
            showLocation = show[2].text()

        self.showTable.removeRow(showIndex.row())
        query = "DELETE from zoo.Show WHERE name = '{}' AND datetime = {{st '{}'}} AND location='{}'".format(showName,showDate, showLocation)
        cursor = self.connection.cursor()
        cursor.execute("USE zoo;")
        cursor.execute(query)
        self.connection.commit()



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 575)
        # Dialog = QtWidgets.QWidget(Dialog)
        # Dialog.setObjectName("centralwidget")
        self.dateLabel = QtWidgets.QLabel(Dialog)
        self.dateLabel.setGeometry(QtCore.QRect(440, 70, 60, 16))
        self.dateLabel.setObjectName("dateLabel")
        self.searchButton = QtWidgets.QPushButton(Dialog)
        self.searchButton.setGeometry(QtCore.QRect(400, 120, 113, 32))
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(self.showSearch)

        self.removeButton = QtWidgets.QPushButton(Dialog)
        self.removeButton.setGeometry(QtCore.QRect(350, 440, 113, 32))
        self.removeButton.setObjectName("removeButton")
        self.showTable = QtWidgets.QTableWidget(Dialog)
        self.showTable.setGeometry(QtCore.QRect(80, 170, 621, 231))
        self.showTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.showTable.setObjectName("showTable")
        self.showTable.setColumnCount(0)
        self.showTable.setRowCount(0)
        self.exhibitBox = QtWidgets.QComboBox(Dialog)
        self.exhibitBox.setGeometry(QtCore.QRect(270, 120, 104, 26))
        self.exhibitBox.setObjectName("exhibitBox")
        self.loadBox()
        self.removeButton.clicked.connect(self.removeShow)

        self.backButton = QtWidgets.QPushButton(Dialog)
        self.backButton.setGeometry(QtCore.QRect(610, 440, 113, 32))
        self.backButton.setObjectName("backButton")
        self.nameLabel = QtWidgets.QLabel(Dialog)
        self.nameLabel.setGeometry(QtCore.QRect(180, 80, 60, 16))
        self.nameLabel.setObjectName("nameLabel")
        self.exhibitlabel = QtWidgets.QLabel(Dialog)
        self.exhibitlabel.setGeometry(QtCore.QRect(180, 130, 60, 16))
        self.exhibitlabel.setObjectName("exhibitlabel")
        self.atlantaZooLabel = QtWidgets.QLabel(Dialog)
        self.atlantaZooLabel.setGeometry(QtCore.QRect(180, 30, 171, 31))
        self.atlantaZooLabel.setObjectName("atlantaZooLabel")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(500, 70, 110, 24))
        self.dateEdit.setObjectName("dateEdit")
        self.nameEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.nameEdit.setGeometry(QtCore.QRect(250, 70, 141, 31))
        self.nameEdit.setPlainText("")
        self.nameEdit.setObjectName("nameEdit")
        # Dialog.setCentralWidget(Dialog)
        # self.menubar = QtWidgets.QMenuBar(Dialog)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        # self.menubar.setObjectName("menubar")
        # Dialog.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(Dialog)
        # self.statusbar.setObjectName("statusbar")
        # Dialog.setStatusBar(self.statusbar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.dateLabel.setText(_translate("Dialog", "Data"))
        self.searchButton.setText(_translate("Dialog", "searchButton"))
        self.removeButton.setText(_translate("Dialog", "remove show"))

        self.backButton.setText(_translate("Dialog", "Back"))
        self.nameLabel.setText(_translate("Dialog", "Name"))
        self.exhibitlabel.setText(_translate("Dialog", "Exhibit"))
        self.atlantaZooLabel.setText(_translate("Dialog", "Atlanta zoo  Shows"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

