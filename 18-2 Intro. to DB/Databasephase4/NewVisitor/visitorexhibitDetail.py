# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitorexhibitDetail.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from loadData import *
from time import gmtime, strftime
from NewVisitor.visitoranimalDetail import  Ui_animalDetail

class Ui_exhibitDetail(object):
    def __init__(self, exhibit, username):
        self.exhibit = exhibit
        self.username = username
        self.connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='garlic93')

    def logVisit(self):
        cursor=self.connection.cursor()
        query = "INSERT into zoo.exhibit_visit VALUES ('{}', '{}', curtime() );".format(self.username, self.exhibit)
        cursor.execute(query)
        self.connection.commit()
        cursor.close()


    def exhibitLabelTable(self):


        cursor = self.connection.cursor()
        cursor.execute("USE zoo;")
        #set tables
        query = "SELECT name, species from zoo.Animal where exhibit='{}';".format(self.exhibit)
        cursor.execute(query)
        result = cursor.fetchall()
        loadTable(self.exhibitTable, result, header=['Name', 'Species'], attNo=2)

        #set labels
        query = ("select Name, Size, numAnimals, Water_Feature  from zoo.exhibit join (select count(*) as numAnimals, animal.Exhibit from zoo.animal group by animal.Exhibit) as a on exhibit.name = a.exhibit where name ='{}';").format(self.exhibit)
        cursor.execute(query)
        result = cursor.fetchall()
        exhibitLabels = loadRow(result)
        self.nameItem.setText(exhibitLabels[0])
        self.sizeItem.setText(exhibitLabels[1])
        self.numItem.setText(exhibitLabels[2])
        if exhibitLabels[3] == "0":
            self.waterItem.setText("No")
        else:
            self.waterItem.setText("Yes")
        cursor.close()

    def animalDetail(self):
        animal = self.exhibitTable.selectedItems()
        animalName = animal[0].text()
        animalSpecies = animal[1].text()
        cursor = self.connection.cursor()
        cursor.execute("USE zoo;")
        # set tables
        query = "SELECT * from zoo.Animal where name='{}' and species = '{}';".format(animalName, animalSpecies)
        cursor.execute(query)
        result = cursor.fetchall()
        animalData = loadRow(result)
        cursor.close()
        self.animalWindow = QtWidgets.QDialog()
        self.ui = Ui_animalDetail(animalData)
        self.ui.setupUi(self.animalWindow)
        self.animalWindow.show()


    def setupUi(self, exhibitDetail):
        exhibitDetail.setObjectName("exhibitDetail")
        exhibitDetail.resize(606, 391)
        exhibitDetail.setStyleSheet("background:rgb(237, 212, 0)")
        self.gridLayout = QtWidgets.QGridLayout(exhibitDetail)
        self.gridLayout.setObjectName("gridLayout")
        self.logvisitButton = QtWidgets.QPushButton(exhibitDetail)
        self.logvisitButton.setStyleSheet("background:rgb(186, 189, 182)")
        self.logvisitButton.setObjectName("logvisitButton")
        self.logvisitButton.clicked.connect(self.logVisit)

        self.gridLayout.addWidget(self.logvisitButton, 6, 3, 1, 1)
        self.nameLabel = QtWidgets.QLabel(exhibitDetail)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout.addWidget(self.nameLabel, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 9, 0, 1, 1)
        self.numLabel = QtWidgets.QLabel(exhibitDetail)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.numLabel.setFont(font)
        self.numLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.numLabel.setObjectName("numLabel")
        self.gridLayout.addWidget(self.numLabel, 5, 1, 1, 1)
        self.exhibitTable = QtWidgets.QTableWidget(exhibitDetail)
        self.exhibitTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.exhibitTable.setStyleSheet("background:rgb(238, 238, 236)")
        self.exhibitTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.exhibitTable.setObjectName("exhibitTable")
        self.exhibitTable.setColumnCount(2)
        self.exhibitTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.exhibitTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.exhibitTable.setHorizontalHeaderItem(1, item)
        self.exhibitTable.horizontalHeader().setCascadingSectionResizes(False)
        self.exhibitTable.horizontalHeader().setDefaultSectionSize(150)
        self.exhibitTable.horizontalHeader().setHighlightSections(False)
        self.exhibitTable.horizontalHeader().setMinimumSectionSize(19)
        self.exhibitTable.horizontalHeader().setSortIndicatorShown(False)
        self.exhibitTable.horizontalHeader().setStretchLastSection(True)
        self.exhibitTable.verticalHeader().setCascadingSectionResizes(True)
        self.exhibitTable.verticalHeader().setHighlightSections(True)
        self.exhibitTable.verticalHeader().setSortIndicatorShown(True)
        self.gridLayout.addWidget(self.exhibitTable, 7, 1, 1, 5)
        self.numItem = QtWidgets.QLabel(exhibitDetail)
        self.numItem.setObjectName("numItem")
        self.gridLayout.addWidget(self.numItem, 5, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 3, 1, 1)
        self.waterItem = QtWidgets.QLabel(exhibitDetail)
        self.waterItem.setAlignment(QtCore.Qt.AlignCenter)
        self.waterItem.setObjectName("waterItem")
        self.gridLayout.addWidget(self.waterItem, 5, 5, 1, 1)
        self.nameItem = QtWidgets.QLabel(exhibitDetail)
        self.nameItem.setAlignment(QtCore.Qt.AlignCenter)
        self.nameItem.setObjectName("nameItem")
        self.gridLayout.addWidget(self.nameItem, 4, 2, 1, 1)
        self.sizeItem = QtWidgets.QLabel(exhibitDetail)
        self.sizeItem.setAlignment(QtCore.Qt.AlignCenter)
        self.sizeItem.setObjectName("sizeItem")
        self.gridLayout.addWidget(self.sizeItem, 4, 5, 1, 1)
        self.detailLabel = QtWidgets.QLabel(exhibitDetail)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.detailLabel.setFont(font)
        self.detailLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.detailLabel.setObjectName("detailLabel")
        self.gridLayout.addWidget(self.detailLabel, 1, 1, 1, 5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        self.waterLabel = QtWidgets.QLabel(exhibitDetail)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.waterLabel.setFont(font)
        self.waterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.waterLabel.setObjectName("waterLabel")
        self.gridLayout.addWidget(self.waterLabel, 5, 4, 1, 1)
        self.zooLabel = QtWidgets.QLabel(exhibitDetail)
        self.zooLabel.setObjectName("zooLabel")
        self.gridLayout.addWidget(self.zooLabel, 2, 1, 1, 2)
        self.sizeLabel = QtWidgets.QLabel(exhibitDetail)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sizeLabel.setFont(font)
        self.sizeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sizeLabel.setObjectName("sizeLabel")
        self.gridLayout.addWidget(self.sizeLabel, 4, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        self.backButton = QtWidgets.QPushButton(exhibitDetail)
        self.backButton.setStyleSheet("background:rgb(186, 189, 182)")
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 8, 5, 1, 1)

        self.retranslateUi(exhibitDetail)
        QtCore.QMetaObject.connectSlotsByName(exhibitDetail)

        self.exhibitLabelTable()
        self.exhibitTable.doubleClicked.connect(self.animalDetail)
        # self.exhibitTable.doubleClicked.connect(self.animalDetail)

    def retranslateUi(self, exhibitDetail):
        _translate = QtCore.QCoreApplication.translate
        exhibitDetail.setWindowTitle(_translate("exhibitDetail", "Dialog"))
        self.logvisitButton.setText(_translate("exhibitDetail", "Log Visit"))
        self.nameLabel.setText(_translate("exhibitDetail", "Name:"))
        self.numLabel.setText(_translate("exhibitDetail", "Num Animals:"))
        item = self.exhibitTable.horizontalHeaderItem(0)
        item.setText(_translate("exhibitDetail", "Name"))
        item = self.exhibitTable.horizontalHeaderItem(1)
        item.setText(_translate("exhibitDetail", "Species"))
        self.numItem.setText(_translate("exhibitDetail", "needitem"))
        self.waterItem.setText(_translate("exhibitDetail", "needitem"))
        self.nameItem.setText(_translate("exhibitDetail", "needitem"))
        self.sizeItem.setText(_translate("exhibitDetail", "needitem"))
        self.detailLabel.setText(_translate("exhibitDetail", "Exhibit Detail"))
        self.waterLabel.setText(_translate("exhibitDetail", "Water Feature:"))
        self.zooLabel.setText(_translate("exhibitDetail", "Atlanta Zoo"))
        self.sizeLabel.setText(_translate("exhibitDetail", "Size:"))
        self.backButton.setText(_translate("exhibitDetail", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    exhibitDetail = QtWidgets.QDialog()
    ui = Ui_exhibitDetail('Amazon', 'Junho')
    ui.setupUi(exhibitDetail)
    exhibitDetail.show()
    sys.exit(app.exec_())

