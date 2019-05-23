# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addShow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from loadData import *


class Ui_addShowView(object):
    def __init__(self):
        object.__init__(self)
        self.connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='garlic93')

    def loadStaffBox(self):
        self.cursor = self.connection.cursor()
        query = "SELECT username from zoo.user NATURAL JOIN zoo.staff;"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        loadExhibit(self.staffBox, result)

    def loadBox(self):
        self.cursor = self.connection.cursor()
        self.cursor.execute("USE zoo;")
        query = "SELECT Name from Exhibit; "
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        loadExhibit(self.exhibitBox, result)


    def showAdd(self):
        name = self.nameEdit.toPlainText()
        exhibit = self.exhibitBox.currentText()

        year = self.dateEdit.date().year()
        month = self.dateEdit.date().month()
        day = self.dateEdit.date().day()
        time = str(self.timeEdit.time().toPyTime())
        staff= self.staffBox.currentText()
        date = "{}-{}-{}".format(year, month, day)
        query = "INSERT into zoo.Show VALUE ('{}', {{ts '{} {}'}}, '{}', '{}');".format(name, date, time, exhibit, staff)
        print(query)
        # print(query)
        # cursor = self.connection.cursor()
        # cursor.execute("USE zoo;")
        self.cursor.execute(query)
        self.connection.commit()


        # error message when insertion has failed.





    def setupUi(self, addShowView):
        addShowView.setObjectName("addShowView")
        addShowView.resize(800, 575)
        self.atlantaZooLabel = QtWidgets.QLabel(addShowView)
        self.atlantaZooLabel.setGeometry(QtCore.QRect(40, 20, 91, 31))
        self.atlantaZooLabel.setObjectName("atlantaZooLabel")
        self.addShowLabel = QtWidgets.QLabel(addShowView)
        self.addShowLabel.setGeometry(QtCore.QRect(290, 20, 81, 31))
        self.addShowLabel.setObjectName("addShowLabel")
        self.NameLabel = QtWidgets.QLabel(addShowView)
        self.NameLabel.setGeometry(QtCore.QRect(30, 60, 71, 21))
        self.NameLabel.setObjectName("NameLabel")
        self.ExhibitLabel = QtWidgets.QLabel(addShowView)
        self.ExhibitLabel.setGeometry(QtCore.QRect(30, 100, 71, 21))
        self.ExhibitLabel.setObjectName("ExhibitLabel")
        self.staffLabel = QtWidgets.QLabel(addShowView)
        self.staffLabel.setGeometry(QtCore.QRect(30, 160, 81, 21))
        self.staffLabel.setObjectName("staffLabel")
        self.dateLabel = QtWidgets.QLabel(addShowView)
        self.dateLabel.setGeometry(QtCore.QRect(30, 210, 81, 21))
        self.dateLabel.setObjectName("dateLabel")
        self.timeLabel = QtWidgets.QLabel(addShowView)
        self.timeLabel.setGeometry(QtCore.QRect(30, 270, 81, 21))
        self.timeLabel.setObjectName("timeLabel")
        self.nameEdit = QtWidgets.QTextEdit(addShowView)
        self.nameEdit.setGeometry(QtCore.QRect(80, 60, 111, 31))
        self.nameEdit.setObjectName("nameEdit")

        self.dateEdit = QtWidgets.QDateEdit(addShowView)
        self.dateEdit.setGeometry(QtCore.QRect(80, 210, 121, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.timeEdit = QtWidgets.QTimeEdit(addShowView)
        self.timeEdit.setGeometry(QtCore.QRect(80, 260, 81, 31))
        self.timeEdit.setObjectName("timeEdit")
        self.addButton = QtWidgets.QPushButton(addShowView)
        self.addButton.setGeometry(QtCore.QRect(290, 120, 91, 31))
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(self.showAdd)

        self.backButton = QtWidgets.QPushButton(addShowView)
        self.backButton.setGeometry(QtCore.QRect(310, 260, 81, 31))
        self.backButton.setObjectName("backButton")
        self.exhibitBox = QtWidgets.QComboBox(addShowView)
        self.exhibitBox.setGeometry(QtCore.QRect(80, 100, 101, 31))
        self.exhibitBox.setEditable(False)
        self.exhibitBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.exhibitBox.setObjectName("exhibitBox")
        self.loadBox()

        self.staffBox = QtWidgets.QComboBox(addShowView)
        self.staffBox.setGeometry(QtCore.QRect(80, 150, 101, 31))
        self.staffBox.setObjectName("staffBox")

        self.loadStaffBox()

        self.retranslateUi(addShowView)
        QtCore.QMetaObject.connectSlotsByName(addShowView)

    def retranslateUi(self, addShowView):
        _translate = QtCore.QCoreApplication.translate
        addShowView.setWindowTitle(_translate("addShowView", "Dialog"))
        self.atlantaZooLabel.setText(_translate("addShowView", "Atlanta Zoo"))
        self.addShowLabel.setText(_translate("addShowView", "Add Show"))
        self.NameLabel.setText(_translate("addShowView", "Name"))
        self.ExhibitLabel.setText(_translate("addShowView", "Exhibit"))
        self.staffLabel.setText(_translate("addShowView", "Staff"))
        self.dateLabel.setText(_translate("addShowView", "Date"))
        self.timeLabel.setText(_translate("addShowView", "Time"))
        self.addButton.setText(_translate("addShowView", "Add Show"))
        self.backButton.setText(_translate("addShowView", "Back"))
        # self.staffBox.setItemText(0, _translate("addShowView", "mammal"))
        # self.staffBox.setItemText(1, _translate("addShowView", "bird"))
        # self.staffBox.setItemText(2, _translate("addShowView", "amphibian"))
        # self.staffBox.setItemText(3, _translate("addShowView", "reptile"))
        # self.staffBox.setItemText(4, _translate("addShowView", "fish"))
        # self.staffBox.setItemText(5, _translate("addShowView", "invertebrate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addShowView = QtWidgets.QDialog()
    ui = Ui_addShowView()
    ui.setupUi(addShowView)
    addShowView.show()
    sys.exit(app.exec_())

