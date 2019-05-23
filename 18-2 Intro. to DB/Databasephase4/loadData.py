from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtSql import *

def loadTable(table, querydata, header, attNo):
    table.setRowCount(0)
    table.setColumnCount(attNo)
    table.setHorizontalHeaderLabels(header)
    for row_number, row_data in enumerate(querydata):
        # first we insert a row then the data is inserted
        table.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

def loadExhibit(combobox, querydata):
    for row_number, row_data in enumerate(querydata):
        for column_number, data in enumerate(row_data):
            combobox.addItem(str(data))

def loadRow(querydata):
    rowList = []
    for row_number, row_data in enumerate(querydata):
        for column_number, data in enumerate(row_data):
            rowList.append(str(data))

    return rowList

