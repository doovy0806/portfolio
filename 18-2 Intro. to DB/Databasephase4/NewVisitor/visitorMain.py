# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitorMain.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from NewVisitor.visitorsearchAnimals import *
from NewVisitor.visitorsearchExhibit import *
from NewVisitor.visitorsearchShows import *
from NewVisitor.visitorshowHistory import *
from NewVisitor.visitorexhibitHistory import *


class Ui_visitorMain(object):
    def __init__(self, username):
        self.username = username

    def animalDialog(self):
        self.animalWindow = QtWidgets.QDialog()
        self.ui = Ui_searchAnimals(self.username)
        self.ui.setupUi(self.animalWindow)
        self.animalWindow.show()

    def exhibitDialog(self):
        self.exhibitWindow = QtWidgets.QDialog()
        self.ui = Ui_searchExhibit(self.username)
        self.ui.setupUi(self.exhibitWindow)
        self.exhibitWindow.show()

    def showDialog(self):
        self.showWindow = QtWidgets.QDialog()
        self.ui = Ui_searchShows(self.username)
        self.ui.setupUi(self.showWindow)
        self.showWindow.show()

    def showHistoryDialog(self):
        self.showHistoryWindow = QtWidgets.QDialog()
        self.ui = Ui_showHistory(self.username)
        self.ui.setupUi(self.showHistoryWindow)
        self.showHistoryWindow.show()

    def exhibitHistoryDialog(self):
        self.exhibitHistoryWindow = QtWidgets.QDialog()
        self.ui = Ui_exhibitHistory(self.username)
        self.ui.setupUi(self.exhibitHistoryWindow)
        self.exhibitHistoryWindow.show()

    def setupUi(self, visitorMain):
        visitorMain.setObjectName("visitorMain")
        visitorMain.resize(529, 490)
        visitorMain.setStyleSheet("background:rgb(237, 212, 0)")
        self.gridLayout = QtWidgets.QGridLayout(visitorMain)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.logoutButton = QtWidgets.QPushButton(visitorMain)
        self.logoutButton.setStyleSheet("background:rgb(186, 189, 182)")
        self.logoutButton.setObjectName("logoutButton")
        self.gridLayout.addWidget(self.logoutButton, 4, 4, 1, 1)
        self.searchShowsButton = QtWidgets.QPushButton(visitorMain)
        self.searchShowsButton.setStyleSheet("background:rgb(186, 189, 182)")
        self.searchShowsButton.setObjectName("searchShowsButton")
        self.gridLayout.addWidget(self.searchShowsButton, 3, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        self.searchAnimalsButton = QtWidgets.QPushButton(visitorMain)
        self.searchAnimalsButton.setStyleSheet("background:rgb(186, 189, 182)")
        self.searchAnimalsButton.setObjectName("searchAnimalsButton")
        self.gridLayout.addWidget(self.searchAnimalsButton, 4, 2, 1, 1)
        self.viewExhibitButton = QtWidgets.QPushButton(visitorMain)
        self.viewExhibitButton.setStyleSheet("background:rgb(186, 189, 182)")
        self.viewExhibitButton.setObjectName("viewExhibitButton")
        self.gridLayout.addWidget(self.viewExhibitButton, 2, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 6, 1, 1)
        self.viewShowHistoryButton = QtWidgets.QPushButton(visitorMain)
        self.viewShowHistoryButton.setStyleSheet("background:rgb(186, 189, 182)")
        self.viewShowHistoryButton.setObjectName("viewShowHistoryButton")
        self.gridLayout.addWidget(self.viewShowHistoryButton, 3, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 5, 0, 1, 1)
        self.zooLabel = QtWidgets.QLabel(visitorMain)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.zooLabel.setFont(font)
        self.zooLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.zooLabel.setObjectName("zooLabel")
        self.gridLayout.addWidget(self.zooLabel, 1, 2, 1, 3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 3, 1, 1)
        self.searchExhibitButton = QtWidgets.QPushButton(visitorMain)
        self.searchExhibitButton.setStyleSheet("background:rgb(186, 189, 182)")
        self.searchExhibitButton.setObjectName("searchExhibitButton")
        self.gridLayout.addWidget(self.searchExhibitButton, 2, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 5, 1, 1)

        self.searchAnimalsButton.clicked.connect(self.animalDialog)
        self.searchExhibitButton.clicked.connect(self.exhibitDialog)
        self.searchShowsButton.clicked.connect(self.showDialog)
        self.viewShowHistoryButton.clicked.connect(self.showHistoryDialog)
        self.viewExhibitButton.clicked.connect(self.exhibitHistoryDialog)

        self.retranslateUi(visitorMain)
        QtCore.QMetaObject.connectSlotsByName(visitorMain)

    def retranslateUi(self, visitorMain):
        _translate = QtCore.QCoreApplication.translate
        visitorMain.setWindowTitle(_translate("visitorMain", "Dialog"))
        self.logoutButton.setText(_translate("visitorMain", "Log Out"))
        self.searchShowsButton.setText(_translate("visitorMain", "Search Shows"))
        self.searchAnimalsButton.setText(_translate("visitorMain", "Search for Animals"))
        self.viewExhibitButton.setText(_translate("visitorMain", "View Exhibit History"))
        self.viewShowHistoryButton.setText(_translate("visitorMain", "View Show History"))
        self.zooLabel.setText(_translate("visitorMain", "Atlanta Zoo"))
        self.searchExhibitButton.setText(_translate("visitorMain", "Search Exhibits"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    visitorMain = QtWidgets.QDialog()
    ui = Ui_visitorMain("Junho")
    ui.setupUi(visitorMain)
    visitorMain.show()
    sys.exit(app.exec_())

