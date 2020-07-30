# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Alberti_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ALBERTI(object):
    def setupUi(self, ALBERTI):
        ALBERTI.setObjectName("ALBERTI")
        ALBERTI.resize(824, 778)
        ALBERTI.setMaximumSize(QtCore.QSize(824, 1000))
        self.centralwidget = QtWidgets.QWidget(ALBERTI)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout_2.addWidget(self.lineEdit_1, 3, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 10, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(1600, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 6, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 8, 1, 1, 1)
        self.Butt1 = QtWidgets.QPushButton(self.centralwidget)
        self.Butt1.setObjectName("Butt1")
        self.gridLayout_2.addWidget(self.Butt1, 5, 2, 1, 1)
        self.ButtCl = QtWidgets.QPushButton(self.centralwidget)
        self.ButtCl.setObjectName("ButtCl")
        self.gridLayout_2.addWidget(self.ButtCl, 7, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 5, 1, 1, 1)
        self.Butt2 = QtWidgets.QPushButton(self.centralwidget)
        self.Butt2.setObjectName("Butt2")
        self.gridLayout_2.addWidget(self.Butt2, 10, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 7, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 1, 1, 1)
        ALBERTI.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ALBERTI)
        self.statusbar.setObjectName("statusbar")
        ALBERTI.setStatusBar(self.statusbar)

        self.retranslateUi(ALBERTI)
        QtCore.QMetaObject.connectSlotsByName(ALBERTI)

    def retranslateUi(self, ALBERTI):
        _translate = QtCore.QCoreApplication.translate
        ALBERTI.setWindowTitle(_translate("ALBERTI", "MainWindow"))
        self.label.setText(_translate("ALBERTI", "Принцип построения этого шифра заключается в следующем:\n"
"для шифрования используются не один как в простой замене, а несколько шифралфавитов.\n"
"Процесс шифрования заключался в нахождении буквы открытого текста на внешнем диске и замене её на букву\n"
"с внутреннего диска, стоящую под ней.\n"
"После этого внутренний диск сдвигался на одну позицию и шифрование второй буквы производилось уже по новому шифралфавиту.\n"
"Эквивалент внешнего диска:\n"
"                                  a b c d e f g h i j k l m n o p q r s t u v w x y z\n"
"                                0 A L B E R T I C P H D F G H J K M N O S U V W X Y Z\n"
"                                1 Z A L B E R T I C P H D F G H J K M N O S U V W X Y\n"
"                             N  2 Y Z A L B E R T I C P H D F G H J K M N O S U V W X\n"
"                             u  3 X Y Z A L B E R T I C P H D F G H J K M N O S U V W\n"
"                             m  4 W X Y Z A L B E R T I C P H D F G H J K M N O S U V\n"
"                             b  5 V W X Y Z A L B E R T I C P H D F G H J K M N O S U\n"
"                             e  6 U V W X Y Z A L B E R T I C P H D F G H J K M N O S\n"
"                             r  7 S U V W X Y Z A L B E R T I C P H D F G H J K M N O\n"
"                                8 O S U V W X Y Z A L B E R T I C P H D F G H J K M N\n"
"И так далее... \n"
"В этом случае верхний регистр букв соответствует рандомизированному внутреннему алфавиту дисков,\n"
"мы используем ALBERTICIPHER как ключевое слово, чтобы формировать алфавит.\n"
"В качестве примера этого шифра зашифруем сообщение «this is a test of alberti» с помощью приведенной выше таблицы.\n"
"Начнём с написания второго ключевого слова, CATWALK, неоднократно под текстом.\n"
"                                                   this is a test of alberti\n"
"                                                   CATW AL K CATW AL KCATWAL\n"
"Теперь замените буквы ключевого слова с их числовым эквивалентом, где А = 0, В = 1, C = 2 и т. д.\n"
"                                    t--h--i--s  i--s  a  t--e--s--t  o--f  a--l--b--e--r--t--i\n"
"                                    2  0 19 22  0 11 10  2  0 19 22  0 11 10  2  0 19 22  0 11\n"
"Следующий символ, соответствующий координатам, определяется характером текста и значением индекса,\n"
"(то есть (t, 2) = N, (h, 0) = C и т. д.)\n"
"                                                    this is a test of alberti\n"
"                                                    NCKW PC M NRZX JU MHLFVSX"))
        self.label_3.setText(_translate("ALBERTI", "Введите ключ:"))
        self.label_5.setText(_translate("ALBERTI", "Открытый текст:"))
        self.label_2.setText(_translate("ALBERTI", "Вывод:"))
        self.Butt1.setText(_translate("ALBERTI", "Зашифровать"))
        self.ButtCl.setText(_translate("ALBERTI", "Очистить"))
        self.Butt2.setText(_translate("ALBERTI", "Расшифровать"))
        self.label_6.setText(_translate("ALBERTI", "Ключ для фомирования алфавита:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ALBERTI = QtWidgets.QMainWindow()
    ui = Ui_ALBERTI()
    ui.setupUi(ALBERTI)
    ALBERTI.show()
    sys.exit(app.exec_())
