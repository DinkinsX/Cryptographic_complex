# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Playfer_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PLAYFER(object):
    def setupUi(self, PLAYFER):
        PLAYFER.setObjectName("PLAYFER")
        PLAYFER.resize(1000, 737)
        PLAYFER.setMaximumSize(QtCore.QSize(1000, 1000))
        self.centralwidget = QtWidgets.QWidget(PLAYFER)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Butt1 = QtWidgets.QPushButton(self.centralwidget)
        self.Butt1.setObjectName("Butt1")
        self.gridLayout.addWidget(self.Butt1, 4, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(1000, 1000))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.Butt2 = QtWidgets.QPushButton(self.centralwidget)
        self.Butt2.setObjectName("Butt2")
        self.gridLayout.addWidget(self.Butt2, 7, 0, 1, 1)
        self.ButtCl = QtWidgets.QPushButton(self.centralwidget)
        self.ButtCl.setObjectName("ButtCl")
        self.gridLayout.addWidget(self.ButtCl, 8, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        PLAYFER.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PLAYFER)
        self.statusbar.setObjectName("statusbar")
        PLAYFER.setStatusBar(self.statusbar)

        self.retranslateUi(PLAYFER)
        QtCore.QMetaObject.connectSlotsByName(PLAYFER)

    def retranslateUi(self, PLAYFER):
        _translate = QtCore.QCoreApplication.translate
        PLAYFER.setWindowTitle(_translate("PLAYFER", "MainWindow"))
        self.Butt1.setText(_translate("PLAYFER", "Зашифровать"))
        self.label.setText(_translate("PLAYFER", "Для того чтобы зашифровать сообщение, необходимо разбить его на биграммы(группы из двух символов), например «Hello World» становится «HE LL OW OR LD»,\n"
"и отыскать эти биграммы в таблице. Два символа биграммы соответствуют углам прямоугольника в ключевой матрице.\n"
"Определяем положения углов этого прямоугольника относительно друг друга. Затем, руководствуясь следующими 4 правилами,\n"
"зашифровываем пары символов исходного текста:\n"
"1.Если два символа биграммы совпадают (или если остался один символ), добавляем после первого символа «Х»,\n"
"зашифровываем новую пару символов и продолжаем.\n"
"2.Если символы биграммы исходного текста встречаются в одной строке, то эти символы замещаются на символы,\n"
"расположенные в ближайших столбцах справа от соответствующих символов. Если символ является последним в строке,\n"
"то он заменяется на первый символ этой же строки.\n"
"3.Если символы биграммы исходного текста встречаются в одном столбце, то они преобразуются в символы того же столбца,\n"
"находящиеся непосредственно под ними.\n"
"Если символ является нижним в столбце, то он заменяется на первый символ этого же столбца.\n"
"4.Если символы биграммы исходного текста находятся в разных столбцах и разных строках,\n"
"то они заменяются на символы, находящиеся в тех же строках, но соответствующие другим углам прямоугольника."))
        self.label_4.setText(_translate("PLAYFER", "Открытый текст:"))
        self.Butt2.setText(_translate("PLAYFER", "Расшифровать"))
        self.ButtCl.setText(_translate("PLAYFER", "Очистить"))
        self.label_2.setText(_translate("PLAYFER", "Алфавиты:\n"
"Английский: [[\'A\', \'B\', \'C\', \'D\', \'E\'],\n"
"                          [\'F\', \'G\', \'H\', \'I\', \'K\'],\n"
"                          [\'L\', \'M\', \'N\', \'O\', \'P\'],\n"
"                          [\'Q\', \'R\', \'S\', \'T\', \'U\'],\n"
"                          [\'V\', \'W\', \'X\', \'Y\', \'Z\']]\n"
" Русский: [[\'А\', \'Б\', \'В\', \'Г\', \'Д\'],\n"
"                          [\'Е\', \'Ж\', \'З\', \'И\', \'К\'],\n"
"                          [\'Л\', \'М\', \'Н\', \'О\', \'П\'],\n"
"                          [\'Р\', \'С\', \'Т\', \'У\', \'Ф\'],\n"
"                          [\'Х\', \'Ц\', \'Ч\', \'Ш\', \'Щ\'],\n"
"                          [\'Ы\', \'Ь\', \'Э\', \'Ю\', \'Я\']]"))
        self.label_5.setText(_translate("PLAYFER", "Вывод:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PLAYFER = QtWidgets.QMainWindow()
    ui = Ui_PLAYFER()
    ui.setupUi(PLAYFER)
    PLAYFER.show()
    sys.exit(app.exec_())
