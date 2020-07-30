# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gamma_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GAMMA(object):
    def setupUi(self, GAMMA):
        GAMMA.setObjectName("GAMMA")
        GAMMA.resize(925, 532)
        GAMMA.setMaximumSize(QtCore.QSize(1000, 1000))
        self.centralwidget = QtWidgets.QWidget(GAMMA)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 3, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 9, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(1000, 1000))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.Butt1 = QtWidgets.QPushButton(self.centralwidget)
        self.Butt1.setObjectName("Butt1")
        self.gridLayout.addWidget(self.Butt1, 7, 0, 1, 1)
        self.ButtCl = QtWidgets.QPushButton(self.centralwidget)
        self.ButtCl.setObjectName("ButtCl")
        self.gridLayout.addWidget(self.ButtCl, 11, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.Butt2 = QtWidgets.QPushButton(self.centralwidget)
        self.Butt2.setObjectName("Butt2")
        self.gridLayout.addWidget(self.Butt2, 10, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 5, 0, 1, 1)
        self.Butt3 = QtWidgets.QPushButton(self.centralwidget)
        self.Butt3.setObjectName("Butt3")
        self.gridLayout.addWidget(self.Butt3, 6, 0, 1, 1)
        GAMMA.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(GAMMA)
        self.statusbar.setObjectName("statusbar")
        GAMMA.setStatusBar(self.statusbar)

        self.retranslateUi(GAMMA)
        QtCore.QMetaObject.connectSlotsByName(GAMMA)

    def retranslateUi(self, GAMMA):
        _translate = QtCore.QCoreApplication.translate
        GAMMA.setWindowTitle(_translate("GAMMA", "MainWindow"))
        self.label_5.setText(_translate("GAMMA", "Вывод:"))
        self.label.setText(_translate("GAMMA", "Принцип шифрования гаммированием заключается в генерации гаммы шифра с помощью датчика псевдослучайных чисел\n"
"и наложении полученной гаммы шифра на открытые данные обратимым образом\n"
"Процесс дешифрования сводится к повторной генерации гаммы шифра при известном ключе\n"
"и наложении такой же гаммы на зашифрованные данные.\n"
"Ключ генерируется алгоритмом генерации ПСЧ(выбран линейно-конгуэртный метод, гамма сразу преобразуется в символы алфавита).\n"
"Метод представляет собой алгоритм, который дает последовательность чисел псевдослучайного рандомизировано,\n"
"вычисленным с разрывным кусочно линейного уравнением:\n"
" Xn+1 = (a * Xn + c) mod m\n"
"где m — модуль. a — множитель  (0 <= a < m),\n"
"c — приращение (0 <= c < m), X0 — начальное значение (0 <= X0 < m)."))
        self.Butt1.setText(_translate("GAMMA", "Зашифровать"))
        self.ButtCl.setText(_translate("GAMMA", "Очистить"))
        self.label_4.setText(_translate("GAMMA", "Открытый текст:"))
        self.Butt2.setText(_translate("GAMMA", "Расшифровать"))
        self.label_3.setText(_translate("GAMMA", "Ключ:"))
        self.Butt3.setText(_translate("GAMMA", "Сгенерировать ключ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GAMMA = QtWidgets.QMainWindow()
    ui = Ui_GAMMA()
    ui.setupUi(GAMMA)
    GAMMA.show()
    sys.exit(app.exec_())
