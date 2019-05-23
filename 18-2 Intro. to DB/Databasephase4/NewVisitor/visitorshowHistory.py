# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitorshowHistory.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from loadData import  *

class Ui_showHistory(object):

    def __init__(self, username):
        self.username = username
        self.connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='garlic93')

    def loadHistory(self):
        cursor = self.connection.cursor()
        query = ("select show_visit, show.datetime, show.location from zoo.show_visit, zoo.show "
                "where show.name=show_visit.show_visit and show_visit.visitor='{}';").format(self.username)
        cursor.execute(query)
        result = cursor.fetchall()
        loadTable(self.showTable, result, ['Name', 'Time', 'Exhibit'], 3)
        cursor.close()

    def searchHistory(self):

        showName= self.nameEdit.text()
        year = self.timeEdit.date().year()
        month = self.timeEdit.date().month()
        day = self.timeEdit.date().day()
        date = "{}-{}-{}".format(year, month, day)
        exhibit = self.exhibitBox.currentText()
        nextdate = "{}-{}-{}".format(year, month, day + 1)

        query = ("select show_visit, show.datetime, show.location from zoo.show_visit, zoo.show "
                 "where show.name=show_visit.show_visit and show_visit.visitor='{}' and show.name like '%{}%' and "
                 "show_visit.datetime>= {{ts '{}'}} and show_visit.datetime<= {{ts '{}'}} and "
                 "show.location like '%{}%';").format(self.username,showName, date,  nextdate, exhibit)
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        loadTable(self.showTable, result, ['Name', 'Time','Exhibit'], 3)
        cursor.close()

    def setupUi(self, showHistory):
        showHistory.setObjectName("showHistory")
        showHistory.resize(611, 453)
        showHistory.setStyleSheet("background:rgb(237, 212, 0)")
        self.gridLayout = QtWidgets.QGridLayout(showHistory)
        self.gridLayout.setObjectName("gridLayout")
        self.searchButton = QtWidgets.QPushButton(showHistory)
        self.searchButton.setStyleSheet("background:rgb(186, 189, 182)")
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(self.searchHistory)

        self.gridLayout.addWidget(self.searchButton, 6, 4, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 7, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 10, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        self.timeEdit = QtWidgets.QDateEdit(showHistory)
        self.timeEdit.setStyleSheet("background:rgb(238, 238, 236)")
        self.timeEdit.setCalendarPopup(True)
        self.timeEdit.setTimeSpec(QtCore.Qt.UTC)
        self.timeEdit.setDate(QtCore.QDate(2018, 1, 1))
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout.addWidget(self.timeEdit, 5, 2, 1, 1)
        self.timeLabel = QtWidgets.QLabel(showHistory)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.timeLabel.setFont(font)
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.gridLayout.addWidget(self.timeLabel, 5, 1, 1, 1)
        self.exhibitLabel = QtWidgets.QLabel(showHistory)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.exhibitLabel.setFont(font)
        self.exhibitLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.exhibitLabel.setObjectName("exhibitLabel")
        self.gridLayout.addWidget(self.exhibitLabel, 4, 4, 1, 1)
        self.zooLabel = QtWidgets.QLabel(showHistory)
        self.zooLabel.setObjectName("zooLabel")
        self.gridLayout.addWidget(self.zooLabel, 2, 1, 1, 2)
        self.showTable = QtWidgets.QTableWidget(showHistory)
        self.showTable.setStyleSheet("background:rgb(238, 238, 236)")
        self.showTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.showTable.setObjectName("showTable")
        self.showTable.setColumnCount(3)
        self.showTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.showTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.showTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.showTable.setHorizontalHeaderItem(2, item)
        self.showTable.horizontalHeader().setCascadingSectionResizes(True)
        self.showTable.horizontalHeader().setHighlightSections(False)
        self.showTable.horizontalHeader().setSortIndicatorShown(True)
        self.showTable.horizontalHeader().setStretchLastSection(True)
        self.showTable.verticalHeader().setVisible(True)
        self.showTable.verticalHeader().setCascadingSectionResizes(True)
        self.gridLayout.addWidget(self.showTable, 8, 1, 1, 6)
        self.nameEdit = QtWidgets.QLineEdit(showHistory)
        self.nameEdit.setStyleSheet("background:rgb(238, 238, 236)")
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 4, 2, 1, 1)
        self.showLabel = QtWidgets.QLabel(showHistory)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.showLabel.setFont(font)
        self.showLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.showLabel.setObjectName("showLabel")
        self.gridLayout.addWidget(self.showLabel, 1, 1, 1, 6)
        self.exhibitBox = QtWidgets.QComboBox(showHistory)
        self.exhibitBox.setStyleSheet("background:rgb(238, 238, 236)")
        self.exhibitBox.setObjectName("exhibitBox")
        self.exhibitBox.addItem("")
        self.exhibitBox.setItemText(0, "")
        self.gridLayout.addWidget(self.exhibitBox, 4, 5, 1, 1)
        self.nameLabel = QtWidgets.QLabel(showHistory)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout.addWidget(self.nameLabel, 4, 1, 1, 1)
        self.backButton = QtWidgets.QPushButton(showHistory)
        self.backButton.setStyleSheet("background:rgb(186, 189, 182)")
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 9, 5, 1, 1)

        self.retranslateUi(showHistory)
        QtCore.QMetaObject.connectSlotsByName(showHistory)

        self.loadHistory()

    def retranslateUi(self, showHistory):
        _translate = QtCore.QCoreApplication.translate
        showHistory.setWindowTitle(_translate("showHistory", "Dialog"))
        self.searchButton.setText(_translate("showHistory", "Search"))
        self.timeLabel.setText(_translate("showHistory", "Time"))
        self.exhibitLabel.setText(_translate("showHistory", "Exhitbit"))
        self.zooLabel.setText(_translate("showHistory", "Atlanta Zoo"))
        item = self.showTable.horizontalHeaderItem(0)
        item.setText(_translate("showHistory", "Name"))
        item = self.showTable.horizontalHeaderItem(1)
        item.setText(_translate("showHistory", "Time"))
        item = self.showTable.horizontalHeaderItem(2)
        item.setText(_translate("showHistory", "Exhibit"))
        self.showLabel.setText(_translate("showHistory", "Show History"))
        self.nameLabel.setText(_translate("showHistory", "Name"))
        self.backButton.setText(_translate("showHistory", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    showHistory = QtWidgets.QDialog()
    ui = Ui_showHistory('Junho')
    ui.setupUi(showHistory)
    showHistory.show()
    sys.exit(app.exec_())

