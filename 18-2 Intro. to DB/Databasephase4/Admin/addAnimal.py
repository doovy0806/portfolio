# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addAnimal.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from loadData import *


class Ui_addAnimalView(object):
    def __init__(self):
        object.__init__(self)
        self.connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='garlic93')

    def loadBox(self):
        self.cursor = self.connection.cursor()
        self.cursor.execute("USE zoo;")
        query = "SELECT Name from Exhibit; "
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        loadExhibit(self.exhibitBox, result)


    def animalAdd(self):
        name = self.nameEdit.toPlainText()
        exhibit = self.exhibitBox.currentText()
        species = self.speciesEdit.toPlainText()
        animaltype = self.typeBox.currentText()
        age = self.ageBox.value()
        query = "INSERT into Animal VALUE ('{}', '{}', '{}', '{}', '{}');".format(name, species, age, animaltype, exhibit)
        print(query)
        # print(query)
        # cursor = self.connection.cursor()
        # cursor.execute("USE zoo;")
        self.cursor.execute(query)
        self.connection.commit()


        # error message when insertion has failed.





    def setupUi(self, addAnimalView):
        addAnimalView.setObjectName("addAnimalView")
        addAnimalView.resize(800, 550)
        self.atlantaZooLabel = QtWidgets.QLabel(addAnimalView)
        self.atlantaZooLabel.setGeometry(QtCore.QRect(130, 60, 91, 31))
        self.atlantaZooLabel.setObjectName("atlantaZooLabel")
        self.addAnimalLabel = QtWidgets.QLabel(addAnimalView)
        self.addAnimalLabel.setGeometry(QtCore.QRect(380, 60, 81, 31))
        self.addAnimalLabel.setObjectName("addAnimalLabel")
        self.NameLabel = QtWidgets.QLabel(addAnimalView)
        self.NameLabel.setGeometry(QtCore.QRect(120, 100, 71, 21))
        self.NameLabel.setObjectName("NameLabel")
        self.ExhibitLabel = QtWidgets.QLabel(addAnimalView)
        self.ExhibitLabel.setGeometry(QtCore.QRect(120, 160, 71, 21))
        self.ExhibitLabel.setObjectName("ExhibitLabel")
        self.typeLabel = QtWidgets.QLabel(addAnimalView)
        self.typeLabel.setGeometry(QtCore.QRect(120, 230, 81, 21))
        self.typeLabel.setObjectName("typeLabel")
        self.speciesLabel = QtWidgets.QLabel(addAnimalView)
        self.speciesLabel.setGeometry(QtCore.QRect(120, 300, 81, 21))
        self.speciesLabel.setObjectName("speciesLabel")
        self.ageLabel = QtWidgets.QLabel(addAnimalView)
        self.ageLabel.setGeometry(QtCore.QRect(120, 380, 81, 21))
        self.ageLabel.setObjectName("ageLabel")
        self.nameEdit = QtWidgets.QTextEdit(addAnimalView)
        self.nameEdit.setGeometry(QtCore.QRect(170, 100, 111, 31))
        self.nameEdit.setObjectName("nameEdit")
        self.speciesEdit = QtWidgets.QTextEdit(addAnimalView)
        self.speciesEdit.setGeometry(QtCore.QRect(170, 300, 121, 31))
        self.speciesEdit.setObjectName("speciesEdit")
        self.ageBox = QtWidgets.QSpinBox(addAnimalView)
        self.ageBox.setGeometry(QtCore.QRect(170, 370, 81, 31))
        self.ageBox.setObjectName("ageBox")
        self.addButton = QtWidgets.QPushButton(addAnimalView)
        self.addButton.setGeometry(QtCore.QRect(400, 160, 91, 31))
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(self.animalAdd)

        self.backButton = QtWidgets.QPushButton(addAnimalView)
        self.backButton.setGeometry(QtCore.QRect(400, 300, 81, 31))
        self.backButton.setObjectName("backButton")
        self.exhibitBox = QtWidgets.QComboBox(addAnimalView)
        self.exhibitBox.setGeometry(QtCore.QRect(170, 160, 104, 26))
        self.exhibitBox.setEditable(False)
        self.exhibitBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.exhibitBox.setObjectName("exhibitBox")
        self.loadBox()

        self.typeBox = QtWidgets.QComboBox(addAnimalView)
        self.typeBox.setGeometry(QtCore.QRect(170, 230, 101, 31))
        self.typeBox.setObjectName("typeBox")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")
        self.typeBox.addItem("")

        self.retranslateUi(addAnimalView)
        QtCore.QMetaObject.connectSlotsByName(addAnimalView)

    def retranslateUi(self, addAnimalView):
        _translate = QtCore.QCoreApplication.translate
        addAnimalView.setWindowTitle(_translate("addAnimalView", "Dialog"))
        self.atlantaZooLabel.setText(_translate("addAnimalView", "Atlanta Zoo"))
        self.addAnimalLabel.setText(_translate("addAnimalView", "Add Animal"))
        self.NameLabel.setText(_translate("addAnimalView", "Name"))
        self.ExhibitLabel.setText(_translate("addAnimalView", "Exhibit"))
        self.typeLabel.setText(_translate("addAnimalView", "Type"))
        self.speciesLabel.setText(_translate("addAnimalView", "Species"))
        self.ageLabel.setText(_translate("addAnimalView", "Age"))
        self.addButton.setText(_translate("addAnimalView", "Add Animal"))
        self.backButton.setText(_translate("addAnimalView", "Back"))
        self.typeBox.setItemText(0, _translate("addAnimalView", "mammal"))
        self.typeBox.setItemText(1, _translate("addAnimalView", "bird"))
        self.typeBox.setItemText(2, _translate("addAnimalView", "amphibian"))
        self.typeBox.setItemText(3, _translate("addAnimalView", "reptile"))
        self.typeBox.setItemText(4, _translate("addAnimalView", "fish"))
        self.typeBox.setItemText(5, _translate("addAnimalView", "invertebrate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addAnimalView = QtWidgets.QDialog()
    ui = Ui_addAnimalView()
    ui.setupUi(addAnimalView)
    addAnimalView.show()
    sys.exit(app.exec_())

