# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HILL_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HILL(object):
    def setupUi(self, HILL):
        HILL.setObjectName("HILL")
        HILL.resize(736, 588)
        HILL.setMinimumSize(QtCore.QSize(736, 588))
        HILL.setMaximumSize(QtCore.QSize(736, 588))
        self.centralwidget = QtWidgets.QWidget(HILL)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 4, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 9, 0, 1, 1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 8, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 5, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(714, 274))
        self.label_4.setMaximumSize(QtCore.QSize(714, 274))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        HILL.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(HILL)
        self.statusbar.setObjectName("statusbar")
        HILL.setStatusBar(self.statusbar)

        self.retranslateUi(HILL)
        QtCore.QMetaObject.connectSlotsByName(HILL)

    def retranslateUi(self, HILL):
        _translate = QtCore.QCoreApplication.translate
        HILL.setWindowTitle(_translate("HILL", "MainWindow"))
        self.pushButton_3.setText(_translate("HILL", "Очистить"))
        self.label_3.setText(_translate("HILL", "Зашифрованный текст:"))
        self.label.setText(_translate("HILL", "Введите текст:"))
        self.label_2.setText(_translate("HILL", "Введите ключ(длина должна быть равна квадрату целого числа 9, 16, 25...):"))
        self.pushButton_1.setText(_translate("HILL", "Зашифровать"))
        self.pushButton_2.setText(_translate("HILL", "Расшифровать"))
        self.label_4.setText(_translate("HILL", "<html><head/><body><p>Криптосистема Хилла.</p><p>Пример: используются латинские буквы от A до Z, соответствующие им численные значения приведены в таблице.</p><p>A B C D E F...</p><p>0 1 2 3 4 5...</p><p><span style=\" font-family:\'sans-serif\'; font-size:14px; color:#202122; background-color:#ffffff;\">Шифруем сообщение «ACT» и представленный ниже ключ (GYBNQKURP в буквенном виде).</span></p><p><span style=\" font-family:\'sans-serif\'; font-size:14px; color:#202122; background-color:#ffffff;\">Key = [6 24 1][13 16 10][20 17 15]</span></p><p><span style=\" font-family:\'sans-serif\'; font-size:14px; color:#202122; background-color:#ffffff;\">Так как букве «A» соответствует число 0, «C» — 2, «T» — 19, то сообщение — это вектор</span></p><p><span style=\" font-family:\'sans-serif\'; font-size:14px; color:#202122; background-color:#ffffff;\">Vec = [0][2][19]</span></p><p><span style=\" font-family:\'sans-serif\'; font-size:14px; color:#202122; background-color:#ffffff;\">Тогда зашифрованный вектор будет:</span></p><p><span style=\" font-family:\'sans-serif\'; font-size:14px; color:#202122; background-color:#ffffff;\">Cryp = KeyVec(mod 26) = вектор [15][14][7] = текст &quot;РОН&quot;</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HILL = QtWidgets.QMainWindow()
    ui = Ui_HILL()
    ui.setupUi(HILL)
    HILL.show()
    sys.exit(app.exec_())
