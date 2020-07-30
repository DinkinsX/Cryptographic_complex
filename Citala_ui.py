# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Citala_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CITALA(object):
    def setupUi(self, CITALA):
        CITALA.setObjectName("CITALA")
        CITALA.resize(900, 340)
        CITALA.setMaximumSize(QtCore.QSize(900, 500))
        self.centralwidget = QtWidgets.QWidget(CITALA)
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
        CITALA.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CITALA)
        self.statusbar.setObjectName("statusbar")
        CITALA.setStatusBar(self.statusbar)

        self.retranslateUi(CITALA)
        QtCore.QMetaObject.connectSlotsByName(CITALA)

    def retranslateUi(self, CITALA):
        _translate = QtCore.QCoreApplication.translate
        CITALA.setWindowTitle(_translate("CITALA", "MainWindow"))
        self.label_2.setText(_translate("CITALA", "Вывод:"))
        self.label_3.setText(_translate("CITALA", "Введите текст:"))
        self.Butt1.setText(_translate("CITALA", "Зашифровать"))
        self.label_5.setText(_translate("CITALA", "Ключ:"))
        self.Butt2.setText(_translate("CITALA", "Расшифровать"))
        self.label.setText(_translate("CITALA", "Для шифрования сообщения использовались пергаментная лента и палочка цилиндрической формы с фиксированными длиной и диаметром.\n"
"Пергаментная лента наматывалась на палочку так, чтобы не было ни просветов, ни нахлёстов.\n"
"Написание сообщения производилось по намотанной пергаментной ленте по длинной стороне цилиндра.\n"
"После того, как достигался конец намотанной ленты, палочка поворачивалась на часть оборота и написание сообщения продолжалось.\n"
"После разматывания ленты на ней оказывалось зашифрованное сообщение.\n"
"Расшифрование выполнялась с использованием палочки таких же типоразмеров."))
        self.ButtCl.setText(_translate("CITALA", "Очистить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CITALA = QtWidgets.QMainWindow()
    ui = Ui_CITALA()
    ui.setupUi(CITALA)
    CITALA.show()
    sys.exit(app.exec_())
