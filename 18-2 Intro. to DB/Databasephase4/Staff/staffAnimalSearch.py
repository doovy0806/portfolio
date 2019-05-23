# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewanimals.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
import pymysql
from loadData import loadTable, loadExhibit
from Staff.staffAnimalCare import Ui_Dialog as animalCare

class Ui_Dialog(object):
    def __init__(self, username):
        object.__init__(self)
        self.username = username
        self.connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='garlic93')

    def tableLoad(self):
        cursor = self.connection.cursor()
        cursor.execute("USE zoo;")
        query = "SELECT * from Animal;"
        cursor.execute(query)
        result = cursor.fetchall()
        loadTable(self.animalTable, result,header = ['Name', 'Species', 'Age', 'Type', 'Exhibit'], attNo=5)


    def loadBox(self):
        cursor = self.connection.cursor()
        cursor.execute("USE zoo;")
        query = "SELECT Name from Exhibit;"
        cursor.execute(query)
        result = cursor.fetchall()
        loadExhibit(self.exhibitBox, result)
    def animalRemove(self):
        animal = self.animalTable.selectedItems()
        animalIndex = self.animalTable.currentIndex()
        if len(animal) is not 0:
            animalName = animal[0].text()
            species = animal[1].text()

        query = "DELETE from zoo.Animal WHERE name = '{}' AND species='{}';".format(animalName, species)

        cursor = self.connection.cursor()
        cursor.execute("USE zoo;")
        cursor.execute(query)
        self.connection.commit()
        self.animalTable.removeRow(animalIndex.row())
        cursor.close()
    def animalSearch(self):
        nameToStr = self.inputnames.toPlainText()
        speciesToStr = self.inputspecies.toPlainText()
        minToInt = self.agemin.value()
        maxToInt = self.agemax.value()
        typeToStr = self.animaltype.currentText()
        exhibitToString = self.exhibitBox.currentText()

        query = "SELECT * from zoo.Animal where name like '%{}%' AND species like '%{}%' AND age >= {} AND age <= {} AND type like '%{}%' and exhibit like '%{}%';".format(nameToStr, speciesToStr, minToInt, maxToInt, typeToStr, exhibitToString)
        print(query)
        cursor = self.connection.cursor()
        cursor.execute("USE zoo;")
        cursor.execute(query)
        result = cursor.fetchall()
        loadTable(self.animalTable, result, ['Name', 'Species', 'Age', 'Type', 'Exhibit'], 5)
        cursor.close()
    def detailShow(self):


        animal = self.animalTable.selectedItems()
        animalItems = []
        for i in animal:
            animalItems.append(i.text())
        self.detailWindow = QtWidgets.QDialog()
        self.ui = animalCare(animalItems, self.username)
        self.ui.setupUi(self.detailWindow)
        self.detailWindow.show()
        # QtWidgets.QApplication.quit()
        # self.close()




    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 575)

        # Dialog = QtWidgets.QWidget(Dialog)
        # Dialog.setObjectName("centralwidget")
        self.specieslabel = QtWidgets.QLabel(Dialog)
        self.specieslabel.setGeometry(QtCore.QRect(140, 160, 60, 16))
        self.specieslabel.setObjectName("specieslabel")
        self.namelabel = QtWidgets.QLabel(Dialog)
        self.namelabel.setGeometry(QtCore.QRect(140, 110, 60, 16))
        self.namelabel.setObjectName("namelabel")
        self.inputnames = QtWidgets.QPlainTextEdit(Dialog)
        self.inputnames.setGeometry(QtCore.QRect(210, 100, 141, 31))
        self.inputnames.setPlainText("")
        self.inputnames.setObjectName("inputnames")
        self.agelabel = QtWidgets.QLabel(Dialog)
        self.agelabel.setGeometry(QtCore.QRect(420, 110, 111, 21))
        self.agelabel.setObjectName("agelabel")
        self.animalTable = QtWidgets.QTableWidget(Dialog)
        self.animalTable.setGeometry(QtCore.QRect(90, 270, 621, 181))
        self.animalTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.animalTable.setObjectName("tableWidget")
        self.animalTable.setColumnCount(0)
        self.animalTable.setRowCount(0)
        self.agemin = QtWidgets.QSpinBox(Dialog)
        self.agemin.setGeometry(QtCore.QRect(510, 110, 61, 21))
        self.agemin.setObjectName("agemin")
        self.minlabel = QtWidgets.QLabel(Dialog)
        self.minlabel.setGeometry(QtCore.QRect(510, 90, 60, 16))
        self.minlabel.setObjectName("minlabel")
        self.exhibitlable = QtWidgets.QLabel(Dialog)
        self.exhibitlable.setGeometry(QtCore.QRect(420, 60, 60, 16))
        self.exhibitlable.setObjectName("exhibitlable")
        self.exhibitBox = QtWidgets.QComboBox(Dialog)
        self.exhibitBox.setGeometry(QtCore.QRect(510, 50, 104, 26))
        self.exhibitBox.setObjectName("exhibitBox")
        self.loadBox()

        self.backButton = QtWidgets.QPushButton(Dialog)
        self.backButton.setGeometry(QtCore.QRect(570, 470, 113, 32))
        self.backButton.setObjectName("backButton")

        self.animaltype = QtWidgets.QComboBox(Dialog)
        self.animaltype.setGeometry(QtCore.QRect(510, 150, 104, 26))
        self.animaltype.setEditable(False)
        self.animaltype.setObjectName("animaltype")
        self.animaltype.addItem("")
        self.animaltype.addItem("")
        self.animaltype.addItem("")
        self.animaltype.addItem("")
        self.animaltype.addItem("")
        self.animaltype.addItem("")
        self.inputspecies = QtWidgets.QPlainTextEdit(Dialog)
        self.inputspecies.setGeometry(QtCore.QRect(210, 150, 141, 31))
        self.inputspecies.setObjectName("inputspecies")
        self.searchButton = QtWidgets.QPushButton(Dialog)
        self.searchButton.setGeometry(QtCore.QRect(350, 230, 113, 32))
        self.searchButton.setObjectName("Search")
        self.searchButton.clicked.connect(self.animalSearch)
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(140, 60, 171, 31))
        self.title.setObjectName("title")
        self.maxlabel = QtWidgets.QLabel(Dialog)
        self.maxlabel.setGeometry(QtCore.QRect(580, 90, 60, 16))
        self.maxlabel.setObjectName("maxlabel")
        self.typelabel = QtWidgets.QLabel(Dialog)
        self.typelabel.setGeometry(QtCore.QRect(420, 150, 111, 31))
        self.typelabel.setObjectName("typelabel")
        self.agemax = QtWidgets.QSpinBox(Dialog)
        self.agemax.setGeometry(QtCore.QRect(580, 110, 61, 21))
        self.agemax.setObjectName("agemax")
        self.animalTable.doubleClicked.connect(self.detailShow)
        # self.removeButton = QtWidgets.QPushButton(Dialog)
        # self.removeButton.setGeometry(QtCore.QRect(350, 470, 141, 31))
        # self.removeButton.setObjectName("removelabel")
        # self.removeButton.clicked.connect(self.animalRemove)

        # Dialog.setCentralWidget(Dialog)
        # self.menubar = QtWidgets.QMenuBar(Dialog)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.specieslabel.setText(_translate("Dialog", "Species"))
        self.namelabel.setText(_translate("Dialog", "Name"))
        self.agelabel.setText(_translate("Dialog", "Age"))
        self.minlabel.setText(_translate("Dialog", "Min"))
        self.exhibitlable.setText(_translate("Dialog", "Exhibit"))
        self.backButton.setText(_translate("Dialog", "Back"))
        self.animaltype.setItemText(0, _translate("Dialog", "fish"))
        self.animaltype.setItemText(1, _translate("Dialog", "mammal"))
        self.animaltype.setItemText(2, _translate("Dialog", "bird"))
        self.animaltype.setItemText(3, _translate("Dialog", "amphibian"))
        self.animaltype.setItemText(4, _translate("Dialog", "reptile"))
        self.animaltype.setItemText(5, _translate("Dialog", "invertebrate"))
        self.searchButton.setText(_translate("Dialog", "Search"))
        self.title.setText(_translate("Dialog", "Atlanta zoo  Animals"))
        self.maxlabel.setText(_translate("Dialog", "Max"))
        self.typelabel.setText(_translate("Dialog", "Type"))
        # self.removeButton.setText(_translate("Dialog", "Remove Animal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

