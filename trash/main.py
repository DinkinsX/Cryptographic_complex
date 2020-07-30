import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from untitled import *
import Alg

class MyWin(QtWidgets.QMainWindow):
    #Почему ты работаешь через раз?

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.ButtCl.clicked.connect(self.getzero)
        self.ui.Butt1.clicked.connect(self.getEn)
        self.ui.Butt2.clicked.connect(self.getDe)

    def getzero(self):
        self.ui.lineEdit.setText(str(''))
        self.ui.lineEdit_2.setText(str(''))    
    

    def getEn(self):
        valued = str(self.ui.lineEdit.text())

        if len(valued) == 0:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода')
            msg.setText('Вы ничего не ввели и пытаетесь сломать программу \n( ͡° ͜ʖ ͡°) не получится ( ͡° ͜ʖ ͡°) ')
            msg.setIcon(msg.Warning)
            msg.exec()

        else:
            try:
                print(valued)
                value_encoded = Alg.encode_val(valued)
                print(value_encoded)
                if len(valued) != len(value_encoded):
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Ошибка ввода')
                    msg.setText('Ошибка ввода. \nМожно вводить только символы русского и английского алфавита! \nПопробуйте снова!')
                    msg.setIcon(msg.Warning)
                    msg.exec()

                else:
                    encript1 = Alg.encript(value_encoded)
                    self.ui.lineEdit_2.setText(str(''.join(encript1)))

            except:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода')
                msg.setText('Ошибка ввода \nПопробуйте снова!')
                msg.setIcon(msg.Warning)
                msg.exec()

        

    def getDe(self):
        valued2 = str(self.ui.lineEdit.text())

        if len(valued2) == 0:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода')
            msg.setText('Вы ничего не ввели и пытаетесь сломать программу \n( ͡° ͜ʖ ͡°) не получится ( ͡° ͜ʖ ͡°) ')
            msg.setIcon(msg.Warning)
            msg.exec() 

        else:
            try:
                value_encoded = Alg.encode_val(valued2)
                print(value_encoded)
                if len(valued2) != len(value_encoded):
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Ошибка ввода')
                    msg.setText('Ошибка ввода. \nМожно вводить только символы русского и английского алфавита! \nПопробуйте снова!')
                    msg.setIcon(msg.Warning)
                    msg.exec()
                else:
	                encript1 = Alg.encript(value_encoded)
                	print(encript1)
                	self.ui.lineEdit_2.setText(str(''.join(encript1)))

            except:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка ввода')
                msg.setText('Ошибка ввода \nПопробуйте снова!')
                msg.setText(' \nПопробуйте снова!')
                msg.setIcon(msg.Warning)
                msg.exec()


    def mbox(self, body, title='Error'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())