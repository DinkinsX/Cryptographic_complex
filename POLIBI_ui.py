# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'POLIBI_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_POLIBI(object):
    def setupUi(self, POLIBI):
        POLIBI.setObjectName("POLIBI")
        POLIBI.resize(824, 400)
        POLIBI.setMaximumSize(QtCore.QSize(824, 400))
        self.centralwidget = QtWidgets.QWidget(POLIBI)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 6, 1, 1, 1)
        self.ButtCl = QtWidgets.QPushButton(self.centralwidget)
        self.ButtCl.setObjectName("ButtCl")
        self.gridLayout_2.addWidget(self.ButtCl, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(1600, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 1, 1, 1)
        self.Butt1 = QtWidgets.QPushButton(self.centralwidget)
        self.Butt1.setObjectName("Butt1")
        self.gridLayout_2.addWidget(self.Butt1, 3, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 3, 1, 1, 1)
        self.Butt2 = QtWidgets.QPushButton(self.centralwidget)
        self.Butt2.setObjectName("Butt2")
        self.gridLayout_2.addWidget(self.Butt2, 6, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)
        POLIBI.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(POLIBI)
        self.statusbar.setObjectName("statusbar")
        POLIBI.setStatusBar(self.statusbar)

        self.retranslateUi(POLIBI)
        QtCore.QMetaObject.connectSlotsByName(POLIBI)

    def retranslateUi(self, POLIBI):
        _translate = QtCore.QCoreApplication.translate
        POLIBI.setWindowTitle(_translate("POLIBI", "MainWindow"))
        self.ButtCl.setText(_translate("POLIBI", "Очистить"))
        self.label.setText(_translate("POLIBI", "Квадрат полибия - для шифрования на квадрате находили букву текста и вставляли в шифровку нижнюю от неё в том же столбце.\n"
"Если буква была в нижней строке, то брали верхнюю из того же столбца.\n"
"Алфавиты использованные в данной работе:\n"
" Русский: [\'А\', \'Б\', \'В\', \'Г\', \'Д\', \'Е\'] Английский: [\'A\', \'B\', \'C\', \'D\', \'E\']\n"
"              [\'Ё\', \'Ж\', \'З\', \'И\', \'Й\', \'К\']                    [\'F\', \'G\', \'H\', \'I\', \'K\']\n"
"              [\'Л\', \'М\', \'Н\', \'О\', \'П\', \'Р\']                    [\'L\', \'M\', \'N\', \'O\', \'P\']\n"
"              [\'С\', \'Т\', \'У\', \'Ф\', \'Х\', \'Ц\']                    [\'Q\', \'R\', \'S\', \'T\', \'U\']\n"
"              [\'Ч\', \'Ш\', \'Щ\', \'Ъ\', \'Ы\', \'Ь\']                    [\'V\', \'W\', \'X\', \'Y\', \'Z\']\n"
"              [\'Э\', \'Ю\', \'Я\', \'x1\', \'x2\', \'x3\']"))
        self.label_3.setText(_translate("POLIBI", "Введите текст:"))
        self.label_2.setText(_translate("POLIBI", "Вывод:"))
        self.Butt1.setText(_translate("POLIBI", "Зашифровать"))
        self.Butt2.setText(_translate("POLIBI", "Расшифровать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    POLIBI = QtWidgets.QMainWindow()
    ui = Ui_POLIBI()
    ui.setupUi(POLIBI)
    POLIBI.show()
    sys.exit(app.exec_())
