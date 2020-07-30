# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vijener_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VIJENER(object):
    def setupUi(self, VIJENER):
        VIJENER.setObjectName("VIJENER")
        VIJENER.resize(743, 500)
        VIJENER.setMaximumSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(VIJENER)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 8, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.Butt1 = QtWidgets.QPushButton(self.centralwidget)
        self.Butt1.setObjectName("Butt1")
        self.gridLayout.addWidget(self.Butt1, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(1000, 1000))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.ButtCl = QtWidgets.QPushButton(self.centralwidget)
        self.ButtCl.setObjectName("ButtCl")
        self.gridLayout.addWidget(self.ButtCl, 10, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.Butt2 = QtWidgets.QPushButton(self.centralwidget)
        self.Butt2.setObjectName("Butt2")
        self.gridLayout.addWidget(self.Butt2, 9, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)
        VIJENER.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(VIJENER)
        self.statusbar.setObjectName("statusbar")
        VIJENER.setStatusBar(self.statusbar)

        self.retranslateUi(VIJENER)
        QtCore.QMetaObject.connectSlotsByName(VIJENER)

    def retranslateUi(self, VIJENER):
        _translate = QtCore.QCoreApplication.translate
        VIJENER.setWindowTitle(_translate("VIJENER", "MainWindow"))
        self.label_3.setText(_translate("VIJENER", "Ключ:"))
        self.Butt1.setText(_translate("VIJENER", "Зашифровать"))
        self.label.setText(_translate("VIJENER", "Исходный текст:       ATTACKATDAWN\n"
"Ключ:                 LEMONLEMONLE\n"
"Зашифрованный текст:  LXFOPVEFRNHR\n"
"\n"
"Первый символ исходного текста (\"A\") зашифрован последовательностью L, которая является первым символом ключа.\n"
"Первый символ зашифрованного текста (\"L\") находится на пересечении строки L и столбца A в таблице Виженера.\n"
"очно так же для второго символа исходного текста используется второй символ ключа;\n"
"то есть второй символ зашифрованного текста (\"X\") получается на пересечении строки E и столбца T.\n"
"Остальная часть исходного текста шифруется подобным способом."))
        self.ButtCl.setText(_translate("VIJENER", "Очистить"))
        self.label_4.setText(_translate("VIJENER", "Открытый текст:"))
        self.Butt2.setText(_translate("VIJENER", "Расшифровать"))
        self.label_5.setText(_translate("VIJENER", "Вывод:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VIJENER = QtWidgets.QMainWindow()
    ui = Ui_VIJENER()
    ui.setupUi(VIJENER)
    VIJENER.show()
    sys.exit(app.exec_())
