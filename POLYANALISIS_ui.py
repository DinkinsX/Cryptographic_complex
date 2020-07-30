# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'POLYANALISIS_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_POLYANALISIS(object):
    def setupUi(self, POLYANALISIS):
        POLYANALISIS.setObjectName("POLYANALISIS")
        POLYANALISIS.resize(760, 485)
        POLYANALISIS.setMinimumSize(QtCore.QSize(730, 485))
        POLYANALISIS.setMaximumSize(QtCore.QSize(760, 500))
        self.centralwidget = QtWidgets.QWidget(POLYANALISIS)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 2, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 4, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 1, 1, 1)
        POLYANALISIS.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(POLYANALISIS)
        self.statusbar.setObjectName("statusbar")
        POLYANALISIS.setStatusBar(self.statusbar)

        self.retranslateUi(POLYANALISIS)
        QtCore.QMetaObject.connectSlotsByName(POLYANALISIS)

    def retranslateUi(self, POLYANALISIS):
        _translate = QtCore.QCoreApplication.translate
        POLYANALISIS.setWindowTitle(_translate("POLYANALISIS", "POLIANALISIS"))
        self.pushButton.setText(_translate("POLYANALISIS", "Ключ"))
        self.label_2.setText(_translate("POLYANALISIS", "Вывод:"))
        self.label_3.setText(_translate("POLYANALISIS", "Введите ключ:"))
        self.pushButton_2.setText(_translate("POLYANALISIS", "Расшифровать"))
        self.label.setText(_translate("POLYANALISIS", "Введите текст:"))
        self.pushButton_3.setText(_translate("POLYANALISIS", "Очистить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    POLYANALISIS = QtWidgets.QMainWindow()
    ui = Ui_POLYANALISIS()
    ui.setupUi(POLYANALISIS)
    POLYANALISIS.show()
    sys.exit(app.exec_())
