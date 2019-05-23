# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitoranimalDetail.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
class Ui_animalDetail(object):
    def __init__(self, animalItems):
        self.animalItems = animalItems
        # self.connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='garlic93')

    def setLabel(self):
        self.animalName = self.animalItems[0]
        self.animalSpecies = self.animalItems[1]
        self.animalAge = self.animalItems[2]
        self.animaltype = self.animalItems[3]
        self.exhibit = self.animalItems[4]

        self.nameItem.setText(self.animalName)
        self.speciesItem.setText(self.animalSpecies)
        self.ageItem.setText(str(self.animalAge)+" month(s)")
        self.typeItem.setText(self.animaltype)
        self.exhibitItem.setText(self.exhibit)
    def setupUi(self, animalDetail):
        animalDetail.setObjectName("animalDetail")
        animalDetail.resize(611, 503)
        animalDetail.setStyleSheet("background:rgb(237, 212, 0)")
        self.gridLayout = QtWidgets.QGridLayout(animalDetail)
        self.gridLayout.setObjectName("gridLayout")
        self.nameLabel = QtWidgets.QLabel(animalDetail)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout.addWidget(self.nameLabel, 4, 1, 1, 1)
        self.zooLabel = QtWidgets.QLabel(animalDetail)
        self.zooLabel.setObjectName("zooLabel")
        self.gridLayout.addWidget(self.zooLabel, 2, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 7, 0, 1, 1)
        self.label = QtWidgets.QLabel(animalDetail)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 6, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.speciesLabel = QtWidgets.QLabel(animalDetail)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.speciesLabel.setFont(font)
        self.speciesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.speciesLabel.setObjectName("speciesLabel")
        self.gridLayout.addWidget(self.speciesLabel, 4, 4, 1, 1)
        self.typeItem = QtWidgets.QLabel(animalDetail)
        self.typeItem.setAlignment(QtCore.Qt.AlignCenter)
        self.typeItem.setObjectName("typeItem")
        self.gridLayout.addWidget(self.typeItem, 5, 5, 1, 1)
        self.speciesItem = QtWidgets.QLabel(animalDetail)
        self.speciesItem.setAlignment(QtCore.Qt.AlignCenter)
        self.speciesItem.setObjectName("speciesItem")
        self.gridLayout.addWidget(self.speciesItem, 4, 5, 1, 1)
        self.detailLabel = QtWidgets.QLabel(animalDetail)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.detailLabel.setFont(font)
        self.detailLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.detailLabel.setObjectName("detailLabel")
        self.gridLayout.addWidget(self.detailLabel, 1, 1, 1, 5)
        self.ageItem = QtWidgets.QLabel(animalDetail)
        self.ageItem.setAlignment(QtCore.Qt.AlignCenter)
        self.ageItem.setObjectName("ageItem")
        self.gridLayout.addWidget(self.ageItem, 6, 2, 1, 1)
        self.exhibitItem = QtWidgets.QLabel(animalDetail)
        self.exhibitItem.setAlignment(QtCore.Qt.AlignCenter)
        self.exhibitItem.setObjectName("exhibitItem")
        self.gridLayout.addWidget(self.exhibitItem, 5, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 3, 1, 1)
        self.exhibitLabel = QtWidgets.QLabel(animalDetail)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.exhibitLabel.setFont(font)
        self.exhibitLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.exhibitLabel.setObjectName("exhibitLabel")
        self.gridLayout.addWidget(self.exhibitLabel, 5, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        self.typeLabel = QtWidgets.QLabel(animalDetail)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.typeLabel.setFont(font)
        self.typeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.typeLabel.setObjectName("typeLabel")
        self.gridLayout.addWidget(self.typeLabel, 5, 4, 1, 1)
        self.nameItem = QtWidgets.QLabel(animalDetail)
        self.nameItem.setAlignment(QtCore.Qt.AlignCenter)
        self.nameItem.setObjectName("nameItem")
        self.gridLayout.addWidget(self.nameItem, 4, 2, 1, 1)
        self.backButton = QtWidgets.QPushButton(animalDetail)
        self.backButton.setStyleSheet("background:rgb(186, 189, 182)")
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 6, 4, 1, 2)

        self.retranslateUi(animalDetail)
        QtCore.QMetaObject.connectSlotsByName(animalDetail)
        self.setLabel()

    def retranslateUi(self, animalDetail):
        _translate = QtCore.QCoreApplication.translate
        animalDetail.setWindowTitle(_translate("animalDetail", "Dialog"))
        self.nameLabel.setText(_translate("animalDetail", "Name:"))
        self.zooLabel.setText(_translate("animalDetail", "Atlanta Zoo"))
        self.label.setText(_translate("animalDetail", "Age:"))
        self.speciesLabel.setText(_translate("animalDetail", "Species:"))
        self.typeItem.setText(_translate("animalDetail", "needitem"))
        self.speciesItem.setText(_translate("animalDetail", "needitem"))
        self.detailLabel.setText(_translate("animalDetail", "Animal Detail"))
        self.ageItem.setText(_translate("animalDetail", "needitem"))
        self.exhibitItem.setText(_translate("animalDetail", "needitem"))
        self.exhibitLabel.setText(_translate("animalDetail", "Exhibit:"))
        self.typeLabel.setText(_translate("animalDetail", "Type:"))
        self.nameItem.setText(_translate("animalDetail", "needitem"))
        self.backButton.setText(_translate("animalDetail", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    animalDetail = QtWidgets.QDialog()
    ui = Ui_animalDetail(['Amy', 'Giraffe', 12, 'Mammal', 'Grass'])
    ui.setupUi(animalDetail)
    animalDetail.show()
    sys.exit(app.exec_())

