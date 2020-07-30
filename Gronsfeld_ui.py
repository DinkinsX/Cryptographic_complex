# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gronsfeld_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GRONSFELD(object):
    def setupUi(self, GRONSFELD):
        GRONSFELD.setObjectName("GRONSFELD")
        GRONSFELD.resize(900, 404)
        GRONSFELD.setMaximumSize(QtCore.QSize(900, 500))
        self.centralwidget = QtWidgets.QWidget(GRONSFELD)
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
        GRONSFELD.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(GRONSFELD)
        self.statusbar.setObjectName("statusbar")
        GRONSFELD.setStatusBar(self.statusbar)

        self.retranslateUi(GRONSFELD)
        QtCore.QMetaObject.connectSlotsByName(GRONSFELD)

    def retranslateUi(self, GRONSFELD):
        _translate = QtCore.QCoreApplication.translate
        GRONSFELD.setWindowTitle(_translate("GRONSFELD", "MainWindow"))
        self.label_2.setText(_translate("GRONSFELD", "Вывод:"))
        self.label_3.setText(_translate("GRONSFELD", "Введите текст:"))
        self.Butt1.setText(_translate("GRONSFELD", "Зашифровать"))
        self.label_5.setText(_translate("GRONSFELD", "Ключ(ключ вводится через пробел для каждой шифруемой буквы. Пример: 2 9 33 23 22 1):"))
        self.Butt2.setText(_translate("GRONSFELD", "Расшифровать"))
        self.label.setText(_translate("GRONSFELD", "Шифр Гронсфельда.\n"
"Этот шифр сложной замены, называемый шифром Гронсфельда, представляет собой модификацию шифра Цезаря числовым ключом.\n"
"Для этого под буквами исходного сообщения записывают цифры числового ключа.\n"
"Если ключ короче сообщения, то его запись циклически повторяют.\n"
"Шифртекст получают примерно, как в шифре Цезаря, но отсчитывают по алфавиту не третью букву (как это делается в шифре Цезаря),\n"
"а выбирают ту букву, которая смещена по алфавиту на соответствующую цифру ключа.\n"
"\n"
"Сообщение     ВОСТОЧНЫЙ\n"
"Ключ                 27182718271\n"
"Шифртекст     ДХТЬРЮОГЛ"))
        self.ButtCl.setText(_translate("GRONSFELD", "Очистить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GRONSFELD = QtWidgets.QMainWindow()
    ui = Ui_GRONSFELD()
    ui.setupUi(GRONSFELD)
    GRONSFELD.show()
    sys.exit(app.exec_())
