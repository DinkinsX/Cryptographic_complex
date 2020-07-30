# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 160)
        MainWindow.setMinimumSize(QtCore.QSize(470, 160))
        MainWindow.setMaximumSize(QtCore.QSize(470, 160))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 91, 31))
        self.label.setObjectName("label")
        self.Butt1 = QtWidgets.QPushButton(self.centralwidget)
        self.Butt1.setGeometry(QtCore.QRect(340, 30, 111, 31))
        self.Butt1.setObjectName("Butt1")
        self.Butt2 = QtWidgets.QPushButton(self.centralwidget)
        self.Butt2.setGeometry(QtCore.QRect(340, 100, 111, 31))
        self.Butt2.setObjectName("Butt2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 91, 31))
        self.label_2.setObjectName("label_2")
        self.ButtCl = QtWidgets.QPushButton(self.centralwidget)
        self.ButtCl.setGeometry(QtCore.QRect(340, 70, 111, 23))
        self.ButtCl.setObjectName("ButtCl")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 311, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 100, 311, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Введите текст:"))
        self.Butt1.setText(_translate("MainWindow", "Зашифровать"))
        self.Butt2.setText(_translate("MainWindow", "Расшифровать"))
        self.label_2.setText(_translate("MainWindow", "Вывод:"))
        self.ButtCl.setText(_translate("MainWindow", "Очистить"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
