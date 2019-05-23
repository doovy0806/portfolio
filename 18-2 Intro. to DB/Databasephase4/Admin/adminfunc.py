# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'administrator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

from Admin.viewVisitors import Ui_viewVisitorsDialouge as uiViewVisitor
from Admin.viewStaff import Ui_viewStaffDialouge as uiViewStaff
from Admin.viewShows import  Ui_Dialog as uiViewShows
from Admin.viewAnimal import Ui_Dialog as uiViewAnimal
from Admin.addAnimal import  Ui_addAnimalView as uiAddAnimal
from Admin.addShow import Ui_addShowView as uiAddShow

class Ui_Admin(object):

    def visitorView(self):
        self.visitorDialog = QtWidgets.QDialog()
        self.ui = uiViewVisitor()
        self.ui.setupUi(self.visitorDialog)
        self.visitorDialog.show()

    def staffView(self):
        self.staffDialog = QtWidgets.QDialog()
        self.ui = uiViewStaff()
        self.ui.setupUi(self.staffDialog)
        self.staffDialog.show()

    # convert to the view staff window

    def showsView(self):
        self.showDialog = QtWidgets.QDialog()
        self.ui = uiViewShows()
        self.ui.setupUi(self.showDialog)
        self.showDialog.show()

    # convert to the view shows window

    def showsAdd(self):
        self.addShowDialog = QtWidgets.QDialog()
        self.ui = uiAddShow()
        self.ui.setupUi(self.addShowDialog)
        self.addShowDialog.show()

    # convert to the add shows window

    def animalsView(self):
        self.animalDialog = QtWidgets.QDialog()
        self.ui = uiViewAnimal()
        self.ui.setupUi(self.animalDialog)
        self.animalDialog.show()
    def addAnimalsView(self):
        self.addAnimalDialog = QtWidgets.QDialog()
        self.ui = uiAddAnimal()
        self.ui.setupUi(self.addAnimalDialog)
        self.addAnimalDialog.show()

    # convert to the view animals window

    # def logOut(self):

    #convert to the log out window




    def setupUi(self, Dialog):
        # self.login_button.clicked.connect(self.loginCheck)

        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.viewVisotrButton = QtWidgets.QPushButton(Dialog)
        self.viewVisotrButton.setGeometry(QtCore.QRect(70, 90, 101, 17))
        self.viewVisotrButton.setObjectName("viewVisotrButton")
        self.viewVisotrButton.clicked.connect(self.visitorView)


        self.viewStaffButton = QtWidgets.QPushButton(Dialog)
        self.viewStaffButton.setGeometry(QtCore.QRect(220, 90, 101, 17))
        self.viewStaffButton.setObjectName("viewStaffButton")
        self.viewStaffButton.clicked.connect(self.staffView)


        self.viewShowsButton = QtWidgets.QPushButton(Dialog)
        self.viewShowsButton.setGeometry(QtCore.QRect(70, 130, 101, 17))
        self.viewShowsButton.setObjectName("viewShowsButton")
        self.viewShowsButton.clicked.connect(self.showsView)

        self.addshowsButton = QtWidgets.QPushButton(Dialog)
        self.addshowsButton.setGeometry(QtCore.QRect(70, 170, 101, 17))
        self.addshowsButton.setObjectName("addshowsButton")
        self.addshowsButton.clicked.connect(self.showsAdd)

        self.viewAnimalsButton = QtWidgets.QPushButton(Dialog)
        self.viewAnimalsButton.setGeometry(QtCore.QRect(220, 130, 101, 17))
        self.viewAnimalsButton.setObjectName("viewAnimalsButton")
        self.viewAnimalsButton.clicked.connect(self.animalsView)

        self.addAnimalButton = QtWidgets.QPushButton(Dialog)
        self.addAnimalButton.setGeometry(QtCore.QRect(220, 170, 101, 17))
        self.addAnimalButton.setObjectName("addAnimalButton")
        self.addAnimalButton.clicked.connect(self.addAnimalsView)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 30, 71, 31))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.viewVisotrButton.setText(_translate("Dialog", "View Visitor"))
        self.viewStaffButton.setText(_translate("Dialog", "View Staff"))
        self.viewShowsButton.setText(_translate("Dialog", "View Shows"))
        self.addshowsButton.setText(_translate("Dialog", "Add Shows"))
        self.viewAnimalsButton.setText(_translate("Dialog", "View Animals"))
        self.addAnimalButton.setText(_translate("Dialog", "Add Animal"))
        self.label.setText(_translate("Dialog", "Atlanta Zoo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Admin()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

