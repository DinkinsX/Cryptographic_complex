# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Atbash_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ATBASH(object):
    def setupUi(self, ATBASH):
        ATBASH.setObjectName("ATBASH")
        ATBASH.resize(824, 300)
        ATBASH.setMaximumSize(QtCore.QSize(824, 300))
        self.centralwidget = QtWidgets.QWidget(ATBASH)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 1, 1, 1)
        self.Butt1 = QtWidgets.QPushButton(self.centralwidget)
        self.Butt1.setObjectName("Butt1")
        self.gridLayout_2.addWidget(self.Butt1, 3, 2, 1, 1)
        self.ButtCl = QtWidgets.QPushButton(self.centralwidget)
        self.ButtCl.setObjectName("ButtCl")
        self.gridLayout_2.addWidget(self.ButtCl, 4, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 3, 1, 1, 1)
        self.Butt2 = QtWidgets.QPushButton(self.centralwidget)
        self.Butt2.setObjectName("Butt2")
        self.gridLayout_2.addWidget(self.Butt2, 6, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(1600, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 2)
        ATBASH.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ATBASH)
        self.statusbar.setObjectName("statusbar")
        ATBASH.setStatusBar(self.statusbar)

        self.retranslateUi(ATBASH)
        QtCore.QMetaObject.connectSlotsByName(ATBASH)

    def retranslateUi(self, ATBASH):
        _translate = QtCore.QCoreApplication.translate
        ATBASH.setWindowTitle(_translate("ATBASH", "MainWindow"))
        self.label_2.setText(_translate("ATBASH", "Вывод:"))
        self.Butt1.setText(_translate("ATBASH", "Зашифровать"))
        self.ButtCl.setText(_translate("ATBASH", "Очистить"))
        self.Butt2.setText(_translate("ATBASH", "Расшифровать"))
        self.label_3.setText(_translate("ATBASH", "Введите текст:"))
        self.label.setText(_translate("ATBASH", "Атбаш — простой шифр подстановки для алфавитного письма.\n"
"Правило шифрования состоит в замене i-й буквы алфавита буквой с номером n-i+1, где n — число букв в алфавите.\n"
"Исходный текст        ABCDEFGHIJKLMNOPQRSTUVWXYZ\n"
"Зашифрованный текст    ZYXWVUTSRQPONMLKJIHGFEDCBA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ATBASH = QtWidgets.QMainWindow()
    ui = Ui_ATBASH()
    ui.setupUi(ATBASH)
    ATBASH.show()
    sys.exit(app.exec_())
