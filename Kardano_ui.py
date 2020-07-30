# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Kardano_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KARDANO(object):
    def setupUi(self, KARDANO):
        KARDANO.setObjectName("KARDANO")
        KARDANO.resize(824, 800)
        KARDANO.setMaximumSize(QtCore.QSize(824, 800))
        self.centralwidget = QtWidgets.QWidget(KARDANO)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 7, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 6, 1, 1, 1)
        self.Butt1 = QtWidgets.QPushButton(self.centralwidget)
        self.Butt1.setObjectName("Butt1")
        self.gridLayout_2.addWidget(self.Butt1, 10, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 1, 1, 1)
        self.checkBox270 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox270.setObjectName("checkBox270")
        self.gridLayout_2.addWidget(self.checkBox270, 5, 2, 1, 1)
        self.checkBox90 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox90.setObjectName("checkBox90")
        self.gridLayout_2.addWidget(self.checkBox90, 5, 1, 1, 1)
        self.checkBox0 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox0.setObjectName("checkBox0")
        self.gridLayout_2.addWidget(self.checkBox0, 4, 1, 1, 1)
        self.Text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Text.setObjectName("Text")
        self.gridLayout_2.addWidget(self.Text, 15, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(1600, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 9, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 11, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 13, 1, 1, 1)
        self.ButtCl = QtWidgets.QPushButton(self.centralwidget)
        self.ButtCl.setObjectName("ButtCl")
        self.gridLayout_2.addWidget(self.ButtCl, 12, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 10, 1, 1, 1)
        self.Butt2 = QtWidgets.QPushButton(self.centralwidget)
        self.Butt2.setObjectName("Butt2")
        self.gridLayout_2.addWidget(self.Butt2, 15, 2, 1, 1)
        self.check180 = QtWidgets.QCheckBox(self.centralwidget)
        self.check180.setObjectName("check180")
        self.gridLayout_2.addWidget(self.check180, 4, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 12, 1, 1, 1)
        KARDANO.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(KARDANO)
        self.statusbar.setObjectName("statusbar")
        KARDANO.setStatusBar(self.statusbar)

        self.retranslateUi(KARDANO)
        QtCore.QMetaObject.connectSlotsByName(KARDANO)

    def retranslateUi(self, KARDANO):
        _translate = QtCore.QCoreApplication.translate
        KARDANO.setWindowTitle(_translate("KARDANO", "MainWindow"))
        self.label_6.setText(_translate("KARDANO", "Размерность решетки(Число составляющее квадрат NxN. Начиная от 4):"))
        self.Butt1.setText(_translate("KARDANO", "Зашифровать"))
        self.label_4.setText(_translate("KARDANO", "Поворачивать можно только при расшифровке."))
        self.checkBox270.setText(_translate("KARDANO", "270 градусов"))
        self.checkBox90.setText(_translate("KARDANO", "90 градусов"))
        self.checkBox0.setText(_translate("KARDANO", "Исходное"))
        self.label.setText(_translate("KARDANO", "Решетка Кардано.\n"
"Шифрование с добавлением «мусора»\n"
"Решётка — квадрат NxN клеток, некоторые из которых вырезаны.\n"
"Клетки должны иметь такой размер, чтобы в каждую помещалась ровно одна буква.\n"
"Вырезанные клетки должны располагаться таким образом,\n"
"чтобы никакие две из них не оказывались в одном и том же месте при поворотах решётки.\n"
"Для квадратной решётки Кардано возможны четыре способа расположить её для шифрования текста —\n"
"поворачивая её относительно центра на 90°\n"
"\n"
"\n"
"\n"
"Пример текста: пвдрыидвдевтснег\n"
"Пример ключа:  1001010101011111                                                 Расшифрованный текст:\n"
"(единицы - символы которые хотите Расшифровать)\n"
"                    \n"
"[\'1\', \'0\', \'0\', \'1\']                                                    [\'п\', \' \', \' \', \'р\']\n"
"[\'0\', \'1\', \'0\', \'1\']                                                    [\' \', \'и\', \' \', \'в\']\n"
"[\'0\', \'1\', \'0\', \'1\']                                                    [\' \', \'е\', \' \', \'т\']\n"
"[\'1\', \'1\', \'1\', \'1\']                                                    [\'с\', \'н\', \'е\', \'г\']"))
        self.label_3.setText(_translate("KARDANO", "Введите текст:\n"
"Пример:\n"
"Для размерности 4, нужно вводить по 4 символов через пробел.Всего сиволов должно быть 4х4 = 16.\n"
"Сообщение:\'\'пвдр ыидв девт снег\'\'"))
        self.label_5.setText(_translate("KARDANO", "Ключ:\n"
"Размер ключа равен колличеству символов в сообщении.\n"
"Пример:\"1001 0101 0101 1111\""))
        self.label_2.setText(_translate("KARDANO", "Вывод:"))
        self.ButtCl.setText(_translate("KARDANO", "Очистить"))
        self.Butt2.setText(_translate("KARDANO", "Расшифровать"))
        self.check180.setText(_translate("KARDANO", "180 градусов"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KARDANO = QtWidgets.QMainWindow()
    ui = Ui_KARDANO()
    ui.setupUi(KARDANO)
    KARDANO.show()
    sys.exit(app.exec_())
