
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Analysis(object):

    def setupUi(self, Analysis):
        Analysis.setObjectName("Analysis")
        Analysis.setWindowModality(QtCore.Qt.NonModal)
        Analysis.resize(730, 430)
        Analysis.setMinimumSize(QtCore.QSize(730, 430))
        Analysis.setMaximumSize(QtCore.QSize(730, 430))

        self.centralwidget = QtWidgets.QWidget(Analysis)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 180, 231, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 30, 120, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 180, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 571, 161))
        self.textEdit.setObjectName("textEdit")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 230, 571, 161))
        self.textEdit_2.setObjectName("textEdit_2")


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QtCore.QRect(10, 10, 100, 15))

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QtCore.QRect(10, 200, 100, 15))

        Analysis.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Analysis)
        self.statusbar.setObjectName("statusbar")
        Analysis.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(Analysis)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")

        Analysis.setMenuBar(self.menuBar)
        self.action = QtWidgets.QAction(Analysis)
        self.action.setCheckable(False)
        self.action.setEnabled(True)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(Analysis)
        self.action_2.setObjectName("action_2")
        #self.action_3 = QtWidgets.QAction(Analysis)
        #self.action_3.setObjectName("action_3")
        #self.menu.addAction(self.action)
        #self.menu.addAction(self.action_2)
        ##self.menuBar.addAction(self.menu.menuAction())
        #self.menuBar.addAction(self.action_3)

        #self.retranslateUi(Analysis)
        QtCore.QMetaObject.connectSlotsByName(Analysis)

    def retranslateUi(self, Analysis, name):
        _translate = QtCore.QCoreApplication.translate
        if name == "Freq":  Analysis.setWindowTitle(_translate("Analysis", "Частотный криптоанализ"))
        else: Analysis.setWindowTitle(_translate("Analysis", "Polyalphabetic analysis"))
        self.pushButton.setText(_translate("Analysis", "Дешифровать"))
        self.pushButton_2.setText(_translate("Analysis", "Расшифровать"))
        #self.menu.setTitle(_translate("Analysis", "Файл"))
        self.label_2.setText(_translate("Analysis", "Введите текст:"))
        self.label_3.setText(_translate("Analysis", "Вывод:"))
        self.action.setText(_translate("Analysis", "Загрузить "))
        self.action_2.setText(_translate("Analysis", "Сохранить "))
        #self.action_3.setText(_translate("Analysis", "Назад"))
