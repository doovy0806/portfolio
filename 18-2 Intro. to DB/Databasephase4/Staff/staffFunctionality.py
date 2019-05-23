# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StaffFunctionality1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Staff.staffAnimalSearch import Ui_Dialog as uiStaffAnimal
from Staff.staffShowHistory import Ui_Dialog as uiStaffShow

class Ui_Dialog(object):
    def __init__(self, username):
        object.__init__(self)
        self.username = username


    def animalSearch(self):
        self.animalWindow = QtWidgets.QDialog()
        self.ui = uiStaffAnimal(self.username)
        self.ui.setupUi(self.animalWindow)
        self.animalWindow.show()
    def showDetail(self):
        self.showWindow = QtWidgets.QDialog()
        self.ui = uiStaffShow(self.username)
        self.ui.setupUi(self.showWindow)
        self.showWindow.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(536, 346)
        # Dialog = QtWidgets.QWidget(Dialog)
        # Dialog.setObjectName("centralwidget")
        self.atlantaZooLabel = QtWidgets.QLabel(Dialog)
        self.atlantaZooLabel.setGeometry(QtCore.QRect(220, 20, 91, 21))
        self.atlantaZooLabel.setObjectName("atlantaZooLabel")
        self.searchAnimalPushButton = QtWidgets.QPushButton(Dialog)
        self.searchAnimalPushButton.setGeometry(QtCore.QRect(30, 90, 131, 31))
        self.searchAnimalPushButton.setObjectName("searchAnimalPushButton")
        self.searchAnimalPushButton.clicked.connect(self.animalSearch)
        self.viewShowsPushButton = QtWidgets.QPushButton(Dialog)
        self.viewShowsPushButton.setGeometry(QtCore.QRect(200, 90, 113, 32))
        self.viewShowsPushButton.setObjectName("viewShowsPushButton")
        self.viewShowsPushButton.clicked.connect(self.showDetail)
        self.logOutPushButton = QtWidgets.QPushButton(Dialog)
        self.logOutPushButton.setGeometry(QtCore.QRect(370, 90, 113, 32))
        self.logOutPushButton.setObjectName("logOutPushButton")
        # Dialog.setCentralWidget(Dialog)
        # self.menubar = QtWidgets.QMenuBar(Dialog)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 536, 22))
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
        self.atlantaZooLabel.setText(_translate("Dialog", "Atlanta Zoo"))
        self.searchAnimalPushButton.setText(_translate("Dialog", "Search Animals"))
        self.viewShowsPushButton.setText(_translate("Dialog", "View Shows"))
        self.logOutPushButton.setText(_translate("Dialog", "Log Out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog('Heejun')
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

