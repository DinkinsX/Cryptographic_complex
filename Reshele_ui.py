# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Reshele_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RESHELE(object):
    def setupUi(self, RESHELE):
        RESHELE.setObjectName("RESHELE")
        RESHELE.resize(900, 491)
        RESHELE.setMaximumSize(QtCore.QSize(900, 500))
        self.centralwidget = QtWidgets.QWidget(RESHELE)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)
        self.Butt1 = QtWidgets.QPushButton(self.centralwidget)
        self.Butt1.setObjectName("Butt1")
        self.gridLayout_2.addWidget(self.Butt1, 3, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 1, 1, 1)
        self.Butt2 = QtWidgets.QPushButton(self.centralwidget)
        self.Butt2.setObjectName("Butt2")
        self.gridLayout_2.addWidget(self.Butt2, 8, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(1600, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 8, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 5, 1, 1, 1)
        self.ButtCl = QtWidgets.QPushButton(self.centralwidget)
        self.ButtCl.setObjectName("ButtCl")
        self.gridLayout_2.addWidget(self.ButtCl, 5, 2, 1, 1)
        RESHELE.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RESHELE)
        self.statusbar.setObjectName("statusbar")
        RESHELE.setStatusBar(self.statusbar)

        self.retranslateUi(RESHELE)
        QtCore.QMetaObject.connectSlotsByName(RESHELE)

    def retranslateUi(self, RESHELE):
        _translate = QtCore.QCoreApplication.translate
        RESHELE.setWindowTitle(_translate("RESHELE", "MainWindow"))
        self.label_2.setText(_translate("RESHELE", "Вывод:"))
        self.label_3.setText(_translate("RESHELE", "Введите текст:"))
        self.Butt1.setText(_translate("RESHELE", "Зашифровать"))
        self.label_5.setText(_translate("RESHELE", "Ключ(вводить через пробел, пример: 213 1432):"))
        self.Butt2.setText(_translate("RESHELE", "Расшифровать"))
        self.label.setText(_translate("RESHELE", "Шифр, использовавшийся Ришелье представляет собой шифр перестановки, при котором открытый текст разбивается на отрезки,\n"
"а внутри каждого отрезка буквы переставляются в соответствии с фиксированной перестановкой.\n"
"\n"
"Ключ: 1234 654321 192837465\n"
"Открытый текст: Всем привет друзья!\n"
"Шифртекст: Всемевирп т! ядьрзу"))
        self.ButtCl.setText(_translate("RESHELE", "Очистить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RESHELE = QtWidgets.QMainWindow()
    ui = Ui_RESHELE()
    ui.setupUi(RESHELE)
    RESHELE.show()
    sys.exit(app.exec_())
