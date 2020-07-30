import sys
import Atbash_prog
import Cezar_prog
import Reshele_prog
import time
import Hill_prog
import AnalysisFreq_prog
import AnalysisPolyAlf
import Vigenere

from Alf import *
from Analysis_ui import Ui_Analysis
from Gamma_prog import *
from Vernam_prog import * 
from Polibi_prog import *
from Kardano_prog import Kardano
from Alberti_prog import Alberti
from Gronsfeld_prog import Gronsfeld
from Playfer_prog import Playfer
from Vigener_prog import Vigener

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from mainUI import *
from POLYANALISIS_ui import Ui_POLYANALISIS
from Gamma_ui import Ui_GAMMA
from Playfer_ui import Ui_PLAYFER
from Atbash_ui import Ui_ATBASH
from Citala_ui import Ui_CITALA
from Cezar_ui import Ui_CEZAR
from POLIBI_ui import Ui_POLIBI
from Kardano_ui import Ui_KARDANO
from Reshele_ui import Ui_RESHELE
from Alberti_ui import Ui_ALBERTI
from Gronsfeld_ui import Ui_GRONSFELD
from Vijener_ui import Ui_VIJENER
from Vernam_ui import Ui_VERNAM
from HILL_ui import Ui_HILL

class ATBASH_CL(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_ATBASH()
        self.ui.setupUi(self)
        self.ui.ButtCl.clicked.connect(self.getzero)
        self.ui.Butt1.clicked.connect(self.getEn)
        self.ui.Butt2.clicked.connect(self.getDe)

    def getzero(self):
        self.ui.lineEdit.setText(str(''))
        self.ui.lineEdit_2.setText(str(''))
        

    def getEn(self):
        try:
            valued = str(self.ui.lineEdit_2.text())
            print('значение', valued)
            if len(valued) == 0:
                self.mbox('Вы ничего не ввели и пытаетесь сломать программу \n( ͡° ͜ʖ ͡°) не получится ( ͡° ͜ʖ ͡°) ')
            else:
                try:
                    print(valued)
                    value_encoded = Atbash_prog.encode_val(valued)
                    print(value_encoded)
                    if len(valued) != len(value_encoded):
                        self.mbox('Ошибка ввода. \nМожно вводить только символы русского и английского алфавита! \nПопробуйте снова!')
                    else:
                        encript1 = Atbash_prog.encript(value_encoded)
                        self.ui.lineEdit.setText(str(''.join(encript1)))
                except:
                    self.mbox('Ошибка ввода \nПопробуйте снова!')
        except:
            self.mbox('Ошибка ввода. №000')

    def getDe(self):
        try:
            valued2 = str(self.ui.lineEdit_2.text())
            if len(valued2) == 0:
                self.mbox('Вы ничего не ввели и пытаетесь сломать программу \n( ͡° ͜ʖ ͡°) не получится ( ͡° ͜ʖ ͡°) ')
            else:
                try:
                    value_encoded = Atbash_prog.encode_val(valued2)
                    print(value_encoded)
                    if len(valued2) != len(value_encoded):
                        self.mbox('Ошибка ввода. \nМожно вводить только символы русского и английского алфавита! \nПопробуйте снова!')
                    else:
                        encript1 = Atbash_prog.encript(value_encoded)
                        self.ui.lineEdit.setText(str(''.join(encript1)))

                except:
                    self.mbox('Ошибка ввода \nПопробуйте снова!')
        except:
            self.mbox('Ошибка ввода. №000')

    def mbox(self, body, title='Ошибка'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()

class CITALA_CL(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_CITALA()
        self.ui.setupUi(self)
        self.ui.ButtCl.clicked.connect(self.getzero)
        self.ui.Butt1.clicked.connect(self.getEn)
        self.ui.Butt2.clicked.connect(self.getDe)

    def getzero(self):
        self.ui.lineEdit.setText(str(''))
        self.ui.lineEdit_2.setText(str(''))    
        self.ui.lineEdit_3.setText(str(''))  

    def getEn(self):
        try:
            text = str(self.ui.lineEdit.text())
            n = int(str(self.ui.lineEdit_2.text()))
            cipher =''
            for i in range(n):
                for j in range(i,len(text), n):
                    cipher += text[j]
                    print(cipher)
                    self.ui.lineEdit_3.setText(str(''.join(cipher)))
            #return cipher
        except:
            self.mbox('Ошибка ввода. №000')

    def getDe(self):
        try:
            text1 = str(self.ui.lineEdit.text())
            n = int(str(self.ui.lineEdit_2.text()))
            cipher =''
            text = [''] * len(text1)
            k = 0
            for i in range(n):
                for j in range(i, len(text1), n):
                    text[j] = text1[k]
                    k += 1
                    print(text)
            text = ''.join(text)

            self.ui.lineEdit_3.setText(str(''.join(text)))
            #return text
        except:
            self.mbox('Ошибка ввода. №000')

    def mbox(self, body, title='Error'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()

class CEZAR_CL(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_CEZAR()
        self.ui.setupUi(self)
        self.ui.ButtCl.clicked.connect(self.getzero)
        self.ui.Butt1.clicked.connect(self.getEn)
        self.ui.Butt2.clicked.connect(self.getDe)

    def getzero(self):
        self.ui.lineEdit.setText(str(''))
        self.ui.lineEdit_2.setText(str(''))    
        self.ui.lineEdit_3.setText(str(''))  

    def getEn(self):
        valued = str(self.ui.lineEdit.text())
        key = str(self.ui.lineEdit_2.text())
        if len(valued) == 0 or len(key) == 0:
            self.mbox('Вы ничего не ввели и пытаетесь сломать программу \n( ͡° ͜ʖ ͡°) не получится ( ͡° ͜ʖ ͡°) ')
        else:
            try:
                print(valued)
                value_encoded = Cezar_prog.encriptC(valued, key)
                print(value_encoded)
                self.ui.lineEdit_3.setText(str(''.join(value_encoded)))
            except:
                self.mbox('Можно ввести буквы только русского и английского алфавита. \nПопробуйте снова!')

    def getDe(self):
        valued2 = str(self.ui.lineEdit.text())
        key2 = str(self.ui.lineEdit_2.text())
        if len(valued2) == 0 or len(key2) == 0:
            self.mbox('Вы ничего не ввели и пытаетесь сломать программу \n( ͡° ͜ʖ ͡°) не получится ( ͡° ͜ʖ ͡°) ')
        else:
            try:
                value_encoded = Cezar_prog.decriptC(valued2, key2)
                print(value_encoded)
                self.ui.lineEdit_3.setText(str(''.join(value_encoded)))
            except:
                self.mbox('Можно ввести буквы только русского и английского алфавита. \nПопробуйте снова!')

    def mbox(self, body, title='Error'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()

class POLIB_CL(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_POLIBI()
        self.ui.setupUi(self)
        self.ui.ButtCl.clicked.connect(self.getzero)
        self.ui.Butt1.clicked.connect(self.getEn)
        self.ui.Butt2.clicked.connect(self.getDe)


    def getzero(self):
        self.ui.lineEdit.setText(str(''))
        self.ui.lineEdit_2.setText(str(''))    

    def getEn(self):
        try:
            word = str(self.ui.lineEdit_2.text())
            print('значение', word)

            if len(word) == 0:
                self.mbox('Ввести можно только буквы предложенных алфавитов.\n( ͡° ͜ʖ ͡°)')

            elif 65 <= min([ord(i) for i in word]) <= 122 or 1025 <= min([ord(i) for i in word]) <= 1105 or [i for i in word if i =='x' or i == 'X']:
                if 65 <= min([ord(i) for i in word]) <= 122 and 1025 <= max([ord(j) for j in word]) <= 1105:
                    self.mbox('Ввести можно только буквы предложенных алфавитов.\n( ͡° ͜ʖ ͡°)')
                else:    
                    print(ord('ё'))
                    polybius = Polibi(word)
                    poli1 = polybius.coordinate(word)
                    self.ui.lineEdit.setText(str(''.join(polybius.encrypting(word).upper())))
                    #print('{}'.format(bla.decrypting().upper()))
                    #print('Введенное слово: {}\nЗашифованое слово Методом 1: {}\n'.format(word.upper(), polybius.encrypting(word).upper()))

            else:
                self.mbox('Ввести можно только буквы предложенных алфавитов.\n( ͡° ͜ʖ ͡°)')
        except:
            self.mbox('Ошибка ввода. №000')


    def getDe(self):
        try:
            word = str(self.ui.lineEdit_2.text())
            print('значение', word)

            if len(word) == 0:
                self.mbox('Ввести можно только буквы предложенных алфавитов.\n( ͡° ͜ʖ ͡°)')

            elif 65 <= min([ord(i) for i in word]) <= 122 or 1025 <= min([ord(i) for i in word]) <= 1105 or [i for i in word if i =='x' or i == 'X'] or len(word) > 1:
                print(min([ord(i) for i in word]), min([ord(j) for j in word]))
                if 65 <= min([ord(i) for i in word]) <= 122 and 1025 <= max([ord(j) for j in word]) <= 1105:
                    self.mbox('Ввести можно только буквы предложенных алфавитов.\n( ͡° ͜ʖ ͡°)')
                else:
                    polybius = Polibi(word)
                    poli1 = polybius.coordinate(word)
                    self.ui.lineEdit.setText(str(''.join(polybius.decrypting(word).upper())))
                    #print('{}'.format(bla.decrypting().upper()))
                    #print('Введенное слово: {}\nЗашифованое слово Методом 1: {}\n'.format(word.upper(), polybius.encrypting(word).upper()))

            else:
                self.mbox('Ввести можно только буквы предложенных алфавитов.\n( ͡° ͜ʖ ͡°)')
        except:
            self.mbox('Ошибка ввода. №000')

    def mbox(self, body, title='Error'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()

class KARDANO_CL(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_KARDANO()
        self.ui.setupUi(self)
        self.ui.ButtCl.clicked.connect(self.getzero)
        self.ui.Butt1.clicked.connect(self.getEn)
        self.ui.Butt2.clicked.connect(self.getDe)
        '''        self.ui.checkBox0.stateChanged.connect(self.getCheck0)
        self.ui.checkBox90.stateChanged.connect(self.getCheck90)
        self.ui.check180.stateChanged.connect(self.getCheck180)
        self.ui.checkBox270.stateChanged.connect(self.getCheck270)'''

    def getzero(self):
        self.ui.lineEdit.setText(str(''))
        self.ui.lineEdit_2.setText(str('')) 
        self.ui.lineEdit_3.setText(str('')) 
        self.ui.Text.setPlainText(str(''))

    def getEn(self):
        try:
            SIZE = int(self.ui.lineEdit.text())
            wordOld = str(self.ui.lineEdit_2.text())
            keyOld = str(self.ui.lineEdit_3.text())
            word = wordOld.replace(" ", "")
            key = keyOld.replace(" ", "")
            if len(word) == len(key) and SIZE >= 4 and len(word) // SIZE == SIZE:
                kardanos = Kardano(word, key, SIZE)
                A = kardanos.Matrix()
                self.AnswerEn = []
                for i in range(len(A)):
                    for j in range(len(A[i])):
                        self.AnswerEn.append(A[i][j])
                        self.AnswerEn.append(' ')
                    self.AnswerEn.append('\n')
                    print(self.AnswerEn)

                self.ui.Text.setPlainText(str(''.join(self.AnswerEn)))
            else:
                self.mbox('Колличество букв в ключе и в тексте должны\nбыть равны.\nТакже размерность должна быть числом\nот 4 до N')
        except:
            self.mbox('Ошибка ввода. №000')



    def getDe(self):
        try:
            SIZE = int(self.ui.lineEdit.text())
            wordOld = str(self.ui.lineEdit_2.text())
            keyOld = str(self.ui.lineEdit_3.text())
            word = wordOld.replace(" ", "")
            key = keyOld.replace(" ", "")  

            if len(word) == len(key) and SIZE >= 4 and len(word) // SIZE == SIZE:
                kardanos = Kardano(word, key, SIZE)
                print(key)
                print(word)
                A = kardanos.Mass_0(word, key)
                print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaa', A)
                B = kardanos.Mass_90(word, key)
                C = kardanos.Mass_180(word, key)
                D = kardanos.Mass_270(word, key)

                AnswerA = []
                AnswerB = []
                AnswerC = []
                AnswerD = []

                for i in range(len(A)):
                    for j in range(len(A[i])):
                        AnswerA.append(A[i][j])
                        AnswerA.append(' ')
                    AnswerA.append('\n')
                    print(AnswerA)
                for i in range(len(B)):
                    for j in range(len(B[i])):
                        AnswerB.append(B[i][j])
                        AnswerB.append(' ')
                    AnswerB.append('\n')
                    print(AnswerB)
                for i in range(len(C)):
                    for j in range(len(C[i])):
                        AnswerC.append(C[i][j])
                        AnswerC.append(' ')
                    AnswerC.append('\n')
                    print(AnswerC)
                for i in range(len(D)):
                    for j in range(len(D[i])):
                        AnswerD.append(D[i][j])
                        AnswerD.append(' ')
                    AnswerD.append('\n')
                    print(AnswerD)

                if self.ui.checkBox0.isChecked():
                    self.ui.Text.setPlainText(str(''.join(AnswerA)))
                elif self.ui.checkBox90.isChecked(): 
                    self.ui.Text.setPlainText(str(''.join(AnswerB)))
                elif self.ui.check180.isChecked():
                    self.ui.Text.setPlainText(str(''.join(AnswerC)))
                elif self.ui.checkBox270.isChecked():
                    self.ui.Text.setPlainText(str(''.join(AnswerD)))
                else: 
                    self.ui.Text.setPlainText(str(''.join(AnswerA)))
            else:
                self.mbox('Колличество букв в ключе и в тексте должны\nбыть равны.\nТакже размерность должна быть числом\nот 4 до N')
        except:
            self.mbox('Ошибка ввода. №000')

    def mbox(self, body, title='Error'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()

class RESHELE_CL(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_RESHELE()
        self.ui.setupUi(self)
        self.ui.ButtCl.clicked.connect(self.getzero)
        self.ui.Butt1.clicked.connect(self.getEn)
        self.ui.Butt2.clicked.connect(self.getDe)
    
    def getzero(self):
        self.ui.lineEdit.setText(str(''))
        self.ui.lineEdit_2.setText(str('')) 
        self.ui.lineEdit_3.setText(str('')) 

    def getEn(self):
        try:
            word = str(self.ui.lineEdit.text())
            key = str(self.ui.lineEdit_2.text())
            keySplit = key.replace(' ', '')

            if len(word) == 0 or len(keySplit) == 0 or len(word) != len(keySplit):
                self.mbox('Ошибка ввода. \n Слово и ключ должны быть одной длины.')
            else:

                value = Reshele_prog.ResheleEn(word, key)
                self.ui.lineEdit_3.setText(str(''.join(value)))  
        except:
            self.mbox('Ошибка ввода. №000')

    def getDe(self):
        try:
            word = str(self.ui.lineEdit.text())
            key = str(self.ui.lineEdit_2.text())
            keySplit = key.replace(' ', '')

            if len(word) == 0 or len(keySplit) == 0 or len(word) != len(keySplit):
                self.mbox('Ошибка ввода. \nСлово и ключ должны быть одной длины.\nИ не пустыми')
            else:

                value = Reshele_prog.ResheleDe(word, key)
                self.ui.lineEdit_3.setText(str(''.join(value)))  
        except:
            self.mbox('Ошибка ввода. №000')

    def mbox(self, body, title='Error'):
            dialog = QMessageBox(QMessageBox.Information, title, body)
            dialog.exec_()

class ALBERTI_CL(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_ALBERTI()
        self.ui.setupUi(self)
        self.ui.ButtCl.clicked.connect(self.getzero)
        self.ui.Butt1.clicked.connect(self.getEn)
        self.ui.Butt2.clicked.connect(self.getDe)

    def getzero(self):
        self.ui.lineEdit_1.setText(str(''))
        self.ui.lineEdit_2.setText(str('')) 
        self.ui.lineEdit_3.setText(str(''))   
        self.ui.lineEdit_4.setText(str(''))  

    def getEn(self):
        try:
            word = str(self.ui.lineEdit_3.text())
            keyIn1 = str(self.ui.lineEdit_1.text())
            keyIn2 = str(self.ui.lineEdit_2.text())
            key1 = keyIn1.upper()
            key2 = keyIn2.upper()

            if 65 <= min([ord(i) for i in word]) <= 122:
                albert = Alberti(word, key1, key2)
                a = albert.EncodeEN()
                if len(a) != len(word):
                    self.mbox('Могут использоваться только\nсимволы одного из алфавитов.')

                else:
                    self.ui.lineEdit_4.setText(str(''.join(a)))

            elif 1025 <= min([ord(i) for i in word]) <= 1105:
                albert = Alberti(word, key1, key2)
                a = albert.EncodeRU()
                if len(a) != len(word):
                    self.mbox('Могут использоваться только\nсимволы одного из алфавитов.')

                else:
                    self.ui.lineEdit_4.setText(str(''.join(a)))
            else:
                self.mbox('Могут использоваться только\nсимволы одного из алфавитов.')
        except:
            self.mbox('Ошибка ввода. №000')

    def getDe(self):
        try:
            word = str(self.ui.lineEdit_3.text())
            keyIn1 = str(self.ui.lineEdit_1.text())
            keyIn2 = str(self.ui.lineEdit_2.text())
            key1 = keyIn1.upper()
            key2 = keyIn2.upper()
            
            if 65 <= min([ord(i) for i in word]) <= 122:
                albert = Alberti(word, key1, key2)
                a = albert.DecodeEN()
                if len(a) != len(word):
                    self.mbox('Могут использоваться только\nсимволы одного из алфавитов.')

                else:
                    self.ui.lineEdit_4.setText(str(''.join(a)))

            elif 1025 <= min([ord(i) for i in word]) <= 1105:
                albert = Alberti(word, key1, key2)
                a = albert.DecodeRU()
                if len(a) != len(word):
                    self.mbox('Могут использоваться только\nсимволы одного из алфавитов.')

                else:
                    self.ui.lineEdit_4.setText(str(''.join(a)))

            else:
                self.mbox('Могут использоваться только\nсимволы одного из алфавитов.')
        except:
            self.mbox('Ошибка ввода. №000')

    def mbox(self, body, title='Error'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()

class GRONSFELD_CL(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_GRONSFELD()
        self.ui.setupUi(self)
        self.ui.ButtCl.clicked.connect(self.getzero)
        self.ui.Butt1.clicked.connect(self.getEn)
        self.ui.Butt2.clicked.connect(self.getDe)

    def getzero(self):
        self.ui.lineEdit.setText(str(''))
        self.ui.lineEdit_2.setText(str('')) 
        self.ui.lineEdit_3.setText(str(''))

    def getEn(self):
        try:
            word = str(self.ui.lineEdit.text())
            key1 = str(self.ui.lineEdit_2.text())
            key = key1.split(" ")
            print(key)
            #f = encriptC(encr, key)
            keyArr = []
            for i in range(len(key)):
                keyInt = int(key[i])
                keyArr.append(keyInt)

            keyArrFull = []
            print(len(keyArr))
            for i in range(0, len(word), len(keyArr)):
                for j in range(len(keyArr)):
                    keyArrFull.append(keyArr[j])

            keyArrFullFull = []
            for i in range(len(word)):
                keyArrFullFull.append(keyArrFull[i])

            print(keyArr)
            enc = Gronsfeld(word, keyArrFullFull)
            encer = enc.encriptC()
            self.ui.lineEdit_3.setText(str(''.join(encer)))
        except:
            self.mbox('Ошибка ввода. №000')

    def getDe(self):
        try:
            word = str(self.ui.lineEdit.text())
            key1 = str(self.ui.lineEdit_2.text())
            key = key1.split(" ")
            print(key)
            #f = encriptC(encr, key)
            keyArr = []
            for i in range(len(key)):
                keyInt = int(key[i])
                keyArr.append(keyInt)

            keyArrFull = []
            print(len(keyArr))
            for i in range(0, len(word), len(keyArr)):
                for j in range(len(keyArr)):
                    keyArrFull.append(keyArr[j])

            keyArrFullFull = []
            for i in range(len(word)):
                keyArrFullFull.append(keyArrFull[i])

            enc2 = Gronsfeld(word, keyArrFullFull)
            encer2 = enc2.decriptC()
            self.ui.lineEdit_3.setText(str(''.join(encer2)))
        except:
            self.mbox('Ошибка ввода. №000')
    def mbox(self, body, title='Error'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()

class PLAYFER_CL(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_PLAYFER()
        self.ui.setupUi(self)
        self.ui.ButtCl.clicked.connect(self.getzero)
        self.ui.Butt1.clicked.connect(self.getEn)
        self.ui.Butt2.clicked.connect(self.getDe) 

    def getzero(self):
        self.ui.lineEdit_1.setText(str(''))
        self.ui.lineEdit_2.setText(str('')) 

    def getEn(self):
        try:
            word = str(self.ui.lineEdit_2.text())

            s = Playfer(word)
            sac = s.encrypt()
            self.ui.lineEdit_1.setText(str(''.join(sac)))
        except:
            self.mbox('Ошибка ввода. №000')

    def getDe(self):
        try:
            word = str(self.ui.lineEdit_2.text())

            s = Playfer(word)
            sac = s.decrypt()
            self.ui.lineEdit_1.setText(str(''.join(sac)))
        except:
            self.mbox('Ошибка ввода. №000')

    def mbox(self, body, title='Error'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()

class VIJENER_CL(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_VIJENER()
        self.ui.setupUi(self)
        self.ui.ButtCl.clicked.connect(self.getzero)
        self.ui.Butt1.clicked.connect(self.getEn)
        self.ui.Butt2.clicked.connect(self.getDe)  

    def getzero(self):
        self.ui.lineEdit_1.setText(str(''))
        self.ui.lineEdit_2.setText(str('')) 
        self.ui.lineEdit_3.setText(str(''))

    def getEn(self):
        try:
            word = str(self.ui.lineEdit_1.text())
            key = str(self.ui.lineEdit_2.text())  
            si = Vigener(word, key)
            sim2 = si.encode(word)
            sim3 = si.encode(key)
            sim5 = si.encodeAll(sim2, sim3)
            sim9 = si.decode(sim5)            
            self.ui.lineEdit_3.setText(str(''.join(sim9)))

        except:
            self.mbox('Ошибка ввода. №000')

    def getDe(self):
        try:
            word = str(self.ui.lineEdit_1.text())
            key = str(self.ui.lineEdit_2.text())
            si = Vigener(word, key)             
            sim2 = si.encode(word)
            sim3 = si.encode(key)
            sim8 = si.decodeAll(sim2, sim3)
            sim9 = si.decode(sim8)
            self.ui.lineEdit_3.setText(str(''.join(sim9)))

        except:
            self.mbox('Ошибка ввода. №000')

    def mbox(self, body, title='Error'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()

class VERNAM_CL(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_VERNAM()
        self.ui.setupUi(self)
        self.ui.ButtCl.clicked.connect(self.getzero)
        self.ui.Butt1.clicked.connect(self.getEn)
        self.ui.Butt2.clicked.connect(self.getDe)
        self.ui.Butt3.clicked.connect(self.getGamma)  

    def getzero(self):
        self.ui.lineEdit_1.setText(str(''))
        self.ui.lineEdit_2.setText(str('')) 
        self.ui.lineEdit_3.setText(str(''))

    def getGamma(self):
        try:
            key = Vernam.lin_rand_arr_flxd(time.time(), 10)
            key2 = ''
            for i in key:
                key2 = key2 + str(i)
            key = Vernam.text_to_bits(key2)
            print(key)
            self.ui.lineEdit_2.setText(str(''.join(key)))

        except:
            self.mbox('Ошибка ввода. №000')

    def getEn(self):
        try:
            word = str(self.ui.lineEdit_1.text())
            key = str(self.ui.lineEdit_2.text())
            word = Vernam.text_to_bits(word)
            kesa = Vernam.xor(word, key)
            self.ui.lineEdit_3.setText(str(''.join(kesa)))

        except:
            self.mbox('Ошибка ввода. №000')

    def getDe(self):
        try:
            word = str(self.ui.lineEdit_1.text())
            key = str(self.ui.lineEdit_2.text())
            kesa2 = Vernam.xor(word, key) 
            self.ui.lineEdit_3.setText(str(''.join(Vernam.text_from_bits(kesa2))))
        except:
            self.mbox('Ошибка ввода. №000')
            
    def mbox(self, body, title='Error'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()

class GAMMA_CL(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_GAMMA()
        self.ui.setupUi(self)
        self.ui.ButtCl.clicked.connect(self.getzero)
        self.ui.Butt1.clicked.connect(self.getEn)
        self.ui.Butt2.clicked.connect(self.getDe)
        self.ui.Butt3.clicked.connect(self.getGamma)  

    def getzero(self):
        self.ui.lineEdit_1.setText(str(''))
        self.ui.lineEdit_2.setText(str('')) 
        self.ui.lineEdit_3.setText(str(''))

    def getGamma(self):
        try:
            word = str(self.ui.lineEdit_1.text())
            if len(word) == 0:
                self.mbox('Ошибка ввода. Введите текст.')
            else:
                gamm = Gamma()
                key = Gamma.lin_rand_arr_flxd(time.time(), len(word) + 1)
                kira = gamm.decode(key)
                self.ui.lineEdit_2.setText(str(''.join(kira)))

        except:
            self.mbox('Ошибка ввода. №000')

    def getEn(self):
        try:
            word = str(self.ui.lineEdit_1.text())
            key = str(self.ui.lineEdit_2.text())
            Gamm = Gamma()
            word = Gamm.encode(word)
            key = Gamm.encode(key)
            kira = Gamma.xorIN(word, key)
            kira = Gamm.decode(kira)
            self.ui.lineEdit_3.setText(str(''.join(kira)))

        except:
            self.mbox('Ошибка ввода. №000')

    def getDe(self):
        try:
            word = str(self.ui.lineEdit_1.text())
            key = str(self.ui.lineEdit_2.text())
            Gamm = Gamma()
            word = Gamm.encode(word)
            key = Gamm.encode(key)
            kira = Gamma.xorOUT(word, key)
            kira = Gamm.decode(kira)
            self.ui.lineEdit_3.setText(str(''.join(kira)))
        except:
            self.mbox('Ошибка ввода. №000')
            
    def mbox(self, body, title='Error'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()

class HILL_CL(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_HILL()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.getzero)
        self.ui.pushButton_1.clicked.connect(self.getEn)
        self.ui.pushButton_2.clicked.connect(self.getDe)


    def getzero(self):
        self.ui.lineEdit_1.setText(str(''))
        self.ui.lineEdit_2.setText(str(''))
        self.ui.lineEdit_2.setText(str(''))

    def getEn(self):
        word = str(self.ui.lineEdit_1.text())
        key = str(self.ui.lineEdit_2.text())
        if word =='':self.mbox('Введите данные')
        elif Hill_prog.check_text(word) == False: self.mbox('Введите символы из алфавита: '+'\n'
                                                     'для англ: a-z A-Z, а также доп символы ".", ",", " " '+'\n'
                                                     'для русского: а-я А-Я, а также доп символы ".", ",", "?", " "')
        else:
            key = self.ui.lineEdit_2.text()
            check = Hill_prog.check_key(key)
            if key.isalpha()!=True or key == '': self.mbox("Ключ должен быть текстом")
            elif check[1] != 2 and check[0] == True:
                result = Hill_prog.enc(word,key)
                if result == 'Ключ не валиден': self.mbox("К сожалению шифрование с этим ключом невозможно. Поменяйте ключ.")
                else: self.ui.lineEdit_3.setText(result)
            else: self.mbox('Длина ключа должна быть 9, 16, 25 и т.д.')

    def getDe(self):
        word = self.ui.lineEdit_1.text()
        if word == '':self.mbox('Введите данные')
        else:
            key = self.ui.lineEdit_2.text()
            if key.isalpha() != True or key == '':self.mbox("Ключ должен быть текстом")
            elif Hill_prog.check_key(key)[0]:self.ui.lineEdit_3.setText(Hill_prog.dec(word, key))
            else:self.mbox('Длина ключа должна быть квадратом целого числа')


    def mbox(self, body, title='Error'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()

class FREG_CL(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Analysis()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self,name="Freq")
        self.ui.pushButton.clicked.connect(self.OpenAnalysisFreq)
        self.ui.pushButton_2.hide()
        self.ui.lineEdit.hide()

    def OpenAnalysisFreq(self):
        text = self.ui.textEdit.toPlainText()
        if text == '':self.mbox("Введите или загрузите текст для дешифровки")
        else:
            self.addWin = AddWindowForFreq()
            self.addWin.show()
            AddWindowForFreq.AnalysisFr(self,text)
            self.addWin.pushButton_3.clicked.connect(self.Freq_decrypt)

    def Freq_decrypt(self):
        text = self.ui.textEdit.toPlainText()
        if text == '':self.mbox("Введите или загрузите текст для дешифровки")
        else:
            array_ch1 = AnalysisFreq_prog.table_to_text(self.addWin.tableWidget,0)
            array_ch2 = AnalysisFreq_prog.table_to_text(self.addWin.tableWidget,1)
            self.ui.textEdit_2.setText(AnalysisFreq_prog.decrypt(text,array_ch1,array_ch2))

    def mbox(self, body, title='Error'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()

class AddWindowForFreq(QMainWindow, AnalysisFreq_prog.Ui_AnalysisFreq):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def AnalysisFr(self,text):
        freq_text = AnalysisFreq_prog.sort_freq(AnalysisFreq_prog.freq_ch(text))
        if len(freq_text) == 26: standart_freq = AnalysisFreq_prog.sort_freq(standart_freq_en)
        else: standart_freq = AnalysisFreq_prog.sort_freq(standart_freq_rus)
        self.addWin.tableWidget.setColumnCount(len(freq_text))
        self.addWin.tableWidget.setRowCount(2)
        AnalysisFreq_prog.text_to_table(self.addWin.tableWidget, list(freq_text.keys()), 0)
        self.addWin.tableWidget.resizeColumnsToContents()

        def Standart():
            AnalysisFreq_prog.text_to_table(self.addWin.tableWidget, list(standart_freq.keys()), 1)

        self.addWin.paintPlot(self.addWin.formLayout, list(freq_text.keys()), list(freq_text.values()))
        #self.addWin.paintPlot(self.addWin.formLayout_2, list(standart_freq.keys()), list(standart_freq.values()))
        self.addWin.pushButton.clicked.connect(Standart)

    def decrypt(self):
        self.ui.textEdit_2.setText(AnalysisFreq_prog.text_to_table())


class FREGPOLY_CL(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_POLYANALISIS()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.getzero)
        self.ui.pushButton.clicked.connect(self.OpenPolyAlfAnalysis)
        #self.ui.pushButton_2.clicked.connect(self.getDe)

    def getzero(self):
        self.ui.textEdit.setText(str(''))
        self.ui.textEdit_2.setText(str(''))
        self.ui.lineEdit_3.setText(str(''))

    def OpenPolyAlfAnalysis(self):
        try:
            text = self.ui.textEdit.toPlainText()
            if text == '':self.mbox("Введите текст для дешифровки")
            else:
                self.addWin = AddWindowForPolyAlf()
                self.addWin.show()
                self.addWin.pushButton_2.clicked.connect(self.MethIndTabl)
                self.addWin.pushButton.clicked.connect(self.PrintKeys1)
                #self.addWin.pushButton_3.clicked.connect(self.MethKasiski)
                AddWindowForPolyAlf.PrintPlotAutoCorel(self, text)
                self.addWin.pushButton_4.clicked.connect(self.MethAutoCorrel)
                self.addWin.pushButton_5.clicked.connect(self.PrintKeys2)
                self.ui.pushButton_2.clicked.connect(self.VigDec)
        except:
            self.mbox('Ошибка ввода данных')

    def MethIndTabl(self):
        try:
            min_ic = self.addWin.lineEdit.text()
            text = self.ui.textEdit.toPlainText()
            if min_ic == '':self.mbox('Введите значение с которого будут учитываться индексы')
            else: AddWindowForPolyAlf.MethIC(self,text,min_ic)
        except:
            self.mbox('Ошибка ввода данных')

    def VigDec(self):

        text = self.ui.textEdit.toPlainText()
        if text == '': self.mbox('Ввеждте текст для расшифровывания')
        else:
            key = self.ui.lineEdit_3.text()
            if key == '':self.mbox('Введите ключ для расшифровывания')
            else: self.ui.textEdit_2.setText(Vigenere.dec(text,key))


    def PrintKeys1(self):
        try:
            AddWindowForPolyAlf.PrintKeysFor1(self)
        except:
            self.mbox('Ошибка ввода данных')

    def PrintKeys2(self):
        try:
            AddWindowForPolyAlf.PrintKeysFor2(self)
        except:
            self.mbox('Ошибка ввода данных')
    def MethAutoCorrel(self):
        try:
            text = self.ui.textEdit.toPlainText()
            AddWindowForPolyAlf.MethAutoCorrel(self,text)
        except:
            self.mbox('Ошибка ввода данных')
    '''
    def MethKasiski(self):
        text = self.ui.textEdit.toPlainText()
        count_symb = self.addWin.lineEdit_2.text()
        if count_symb == '':self.mbox('Введите количество символов, с которого нужно начать поиск повторов.')
        elif count_symb.isdigit(): AddWindowForPolyAlf.MethKasis(self,text,int(count_symb))
        else: self.mbox('Введите число не больше 10 ')'''

    def mbox(self, body, title='Error'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()



class AddWindowForPolyAlf(QMainWindow, AnalysisPolyAlf.Ui_AnalysisPolyAlf):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def MethIC(self,text,min_ic):
        try:
            forTable = (AnalysisPolyAlf.methodIndex(text,float(min_ic)))

            self.addWin.tableWidget.setRowCount(len(forTable[0]))
            for i in range(len(forTable[0])):
                item = QTableWidgetItem(str(i+1))
                item2 = QTableWidgetItem(str(forTable[0][i]))
                item3 = QTableWidgetItem(str(forTable[1][i]))
                item4 = QTableWidgetItem(str(forTable[2][i]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.addWin.tableWidget.setItem(i, 0, item)
                self.addWin.tableWidget.setItem(i, 1, item2)
                self.addWin.tableWidget.setItem(i, 2, item3)
                self.addWin.tableWidget.setItem(i, 3, item4)
                #self.addWin.tableWidget.resizeColumnsToContents()
        except:
            self.mbox('Ошибка ввода данных')
            return


    def PrintKeysFor1(self):
        try:
            text = self.ui.textEdit.toPlainText()
            indexes = []
            for i in range(self.addWin.tableWidget.rowCount()):
                indexes.append(self.addWin.tableWidget.model().index(i,3).data())
            indexes[0] = 0
            keys = AnalysisPolyAlf.printKeyFor1(text,indexes)
            self.addWin.tableWidget_2.setRowCount(len(keys))
            for i in range(len(keys)):
                item = QTableWidgetItem(str(keys[i]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.addWin.tableWidget_2.setItem(i, 0, item)
        except:
            self.mbox('Ошибка ввода данных')
            return

    def PrintKeysFor2(self):
        try:
            text = self.ui.textEdit.toPlainText()
            indexes = []
            for i in range(self.addWin.tableWidget_6.rowCount()):
                indexes.append(self.addWin.tableWidget_6.model().index(i, 0).data())

            keys = AnalysisPolyAlf.printKeyFor2(text, indexes)
            self.addWin.tableWidget_5.setRowCount(len(keys))
            for i in range(len(keys)):
                item = QTableWidgetItem(str(keys[i]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.addWin.tableWidget_5.setItem(i, 0, item)
        except:
            self.mbox('Ошибка ввода данных')
            return
    '''
    def MethKasis(self,text,count_symb):
        result = AnalysisPolyAlf.methodKasiski(text,count_symb)
        len_keys, freq_keys = list(result[1].keys()),list(result[1].values())
        double, count_double = list(result[0].keys()),list(result[0].values())
    
        self.addWin.tableWidget_3.setRowCount(len(double))
        for i in range(len(double)):
            doub = QTableWidgetItem(str(double[i]))
            count_doub = QTableWidgetItem(str(count_double[i]))
            doub.setFlags(QtCore.Qt.ItemIsEnabled)
            count_doub.setFlags(QtCore.Qt.ItemIsEnabled)
            self.addWin.tableWidget_3.setItem(i, 0, doub)
            self.addWin.tableWidget_3.setItem(i, 1, count_doub)

        self.addWin.tableWidget_4.setRowCount(len(len_keys))
        for i in range(len(len_keys)):
            len_key = QTableWidgetItem(str(len_keys[i]))
            freq_key = QTableWidgetItem(str(freq_keys[i]))
            len_key.setFlags(QtCore.Qt.ItemIsEnabled)
            freq_key.setFlags(QtCore.Qt.ItemIsEnabled)
            self.addWin.tableWidget_4.setItem(i, 0, len_key)
            self.addWin.tableWidget_4.setItem(i, 1, freq_key)
        return
    '''
    def PrintPlotAutoCorel(self,text):
        try:
            x = AnalysisPolyAlf.plot(text)
            AnalysisPolyAlf.paintPlot(self,self.addWin.gridLayout,x)
            return
        except:
            self.mbox('Ошибка ввода данных')
            return

    def MethAutoCorrel(self,text):
        try:
            len_key = self.addWin.lineEdit_3.text()
            if len_key  == '' or len_key .isdigit() == False: self.mbox("Введите предполагаемую длину ключа")
            else:
                indexes = AnalysisPolyAlf.methodAutoCorrel(text,int(len_key))
                self.addWin.tableWidget_6.setRowCount(len(indexes))
                for i in range(len(indexes)):
                    item = QTableWidgetItem(str(indexes[i]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.addWin.tableWidget_6.setItem(0, i, item)
        except:
            self.mbox('Ошибка ввода данных')
            return

    def mbox(self, body, title='Error'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()


'''МЕЙН ОКНО С ВЫБОРОМ АЛГОРИТМОВ'''
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_KMZI()
        self.ui.setupUi(self)
        self.ui.b1.clicked.connect(self.attbash)
        self.ui.b2.clicked.connect(self.citala)
        self.ui.b3.clicked.connect(self.cezar)
        self.ui.b4.clicked.connect(self.polib)
        self.ui.b5.clicked.connect(self.kardan)
        self.ui.b6.clicked.connect(self.reshele)
        self.ui.b7.clicked.connect(self.alberti)
        self.ui.b8.clicked.connect(self.gronsfeld)
        self.ui.b9.clicked.connect(self.vijener)
        self.ui.b10.clicked.connect(self.playfer)
        self.ui.b11.clicked.connect(self.hill)
        self.ui.b12.clicked.connect(self.vernam)
        self.ui.b13.clicked.connect(self.gamma)
        self.ui.b14.clicked.connect(self.freg)
        self.ui.b15.clicked.connect(self.fregPoly)

    def attbash(self):
        self.untitled = ATBASH_CL()
        self.untitled.show()
    def citala(self):
        self.untitled = CITALA_CL()
        self.untitled.show()
    def cezar(self):
        self.untitled = CEZAR_CL()
        self.untitled.show()
    def polib(self):
        self.untitled = POLIB_CL()
        self.untitled.show()
    def kardan(self):
        self.untitled = KARDANO_CL()
        self.untitled.show()
    def alberti(self):
        self.untitled = ALBERTI_CL()
        self.untitled.show()
    def gronsfeld(self):
        self.untitled = GRONSFELD_CL()
        self.untitled.show()    
    def reshele(self):
        self.untitled = RESHELE_CL()
        self.untitled.show()
    def playfer(self):
        self.untitled = PLAYFER_CL()
        self.untitled.show()
    def vijener(self):
        self.untitled = VIJENER_CL()
        self.untitled.show()
    def vernam(self):
        self.untitled = VERNAM_CL()
        self.untitled.show()       
    def gamma(self):
        self.untitled = GAMMA_CL()
        self.untitled.show()           
    def hill(self):
        self.untitled = HILL_CL()
        self.untitled.show()          
    def freg(self):
        self.untitled = FREG_CL()
        self.untitled.show()
    def fregPoly(self):
        self.untitled = FREGPOLY_CL()
        self.untitled.show()  


    def mbox(self, body, title='Error'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())