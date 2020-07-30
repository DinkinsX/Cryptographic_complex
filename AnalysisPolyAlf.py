# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnalysisPolyAlf.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import re
from Alf import *
from math import gcd,sqrt
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_AnalysisPolyAlf(object):
    def setupUi(self, AnalysisPolyAlf):
        AnalysisPolyAlf.setObjectName("AnalysisPolyAlf")
        AnalysisPolyAlf.resize(950, 550)
        AnalysisPolyAlf.setMinimumSize(QtCore.QSize(950, 550))
        AnalysisPolyAlf.setMaximumSize(QtCore.QSize(950, 550))
        self.centralwidget = QtWidgets.QWidget(AnalysisPolyAlf)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 0, 221, 31))
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 520, 180))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(650, 40, 230, 180))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.verticalHeader().hide()
        self.tableWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 230, 230, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 240, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        font = QtGui.QFont()
        font.setPointSize(9)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 5, 51, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 5, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        AnalysisPolyAlf.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AnalysisPolyAlf)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 22))
        self.menubar.setObjectName("menubar")
        AnalysisPolyAlf.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AnalysisPolyAlf)
        self.statusbar.setObjectName("statusbar")
        AnalysisPolyAlf.setStatusBar(self.statusbar)

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 270, 261, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 240, 91, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 240, 21, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_5.setGeometry(QtCore.QRect(650, 280, 230, 190))
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(1)
        self.tableWidget_5.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 240, 141, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_6.setGeometry(QtCore.QRect(280, 280, 250, 190))
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(1)
        self.tableWidget_6.setRowCount(0)


        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignTop)
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(650, 480, 230, 25))
        self.pushButton_5.setObjectName("pushButton_5")



        self.retranslateUi(AnalysisPolyAlf)
        QtCore.QMetaObject.connectSlotsByName(AnalysisPolyAlf)

    def retranslateUi(self, AnalysisPolyAlf):
        _translate = QtCore.QCoreApplication.translate
        AnalysisPolyAlf.setWindowTitle(_translate("AnalysisPolyAlf", "Криптоанализ"))
        self.label.setText(_translate("AnalysisPolyAlf", "Метод индекса совпадений:"))
        self.label_2.setText(_translate("AnalysisPolyAlf", "Учет начинается с: "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AnalysisPolyAlf", "Строка"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AnalysisPolyAlf", "ИС"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AnalysisPolyAlf", "ВИС"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("AnalysisPolyAlf", "Сдвиг"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("AnalysisPolyAlf", "Варианты ключа"))
        self.pushButton.setText(_translate("AnalysisPolyAlf", "Вывести варианты ключа"))
        self.label_4.setText(_translate("AnalysisPolyAlf", "Автокорреляционный метод:"))

        self.lineEdit.setText(_translate("AnalysisPolyAlf", "0.05"))
        self.pushButton_2.setText(_translate("AnalysisPolyAlf", "Рассчитать"))

        self.label_3.setText(_translate("AnalysisPolyAlf", "Длина ключа: "))
        self.lineEdit_3.setText(_translate("AnalysisPolyAlf", "1"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("AnalysisPolyAlf", "Варианты ключа"))
        self.pushButton_4.setText(_translate("AnalysisPolyAlf", "Вывести варианты"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("AnalysisPolyAlf", "Варианты ключа"))
        self.pushButton_4.setText(_translate("AnalysisPolyAlf", "Рассчитать смещения"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("AnalysisPolyAlf", "Сдвиг"))
        self.pushButton_5.setText(_translate("AnalysisPolyAlf", "Вывести варианты ключа"))

def text_del_symb(text):
    return ''.join(re.findall('[A-Za-zА-Яа-яёЁ]', text))

def choice_alf (text):
    res = text_del_symb(text)
    if res[0].lower() in alf1: return alf1,len(res)
    elif res[0].lower() in alf3: return alf3,len(res)

def ic (text):
    alf , lenText = choice_alf(text)
    text = list(text_del_symb(text))
    index = 0
    for ch in alf:
        count_ch = text.count(ch.lower())+text.count(ch.upper())
        index += (count_ch*(count_ch-1))/(lenText*(lenText-1))
    return round(index,4)

def mi(row1,row2):
    alf = choice_alf(row1)[0]
    index = 0
    for ch in alf:
        count_ch_row1 = row1.count(ch.lower())+row1.count(ch.upper())
        count_ch_row2 = row2.count(ch.lower()) + row2.count(ch.upper())
        index += (count_ch_row1*count_ch_row2)/(len(row1)*len(row2))
    return round(index,4)

def text_to_array(text,count_row):
    array = []
    text = text_del_symb(text)

    while len(text)>0:
        array.append(text[:count_row])
        text = text[count_row:]

    if len(array[len(array)-1]) < len(array[0]): array[len(array)-1] = array[len(array)-1].ljust(len(array[0]))
    result = []
    for i in range(count_row):
        str = ''
        for j in range(len(array)):str += array[j][i]
        result.append(str)

    return result

def len_key(text,min_ic):
    for i in range(1, len(text)//2):
        inArray = text_to_array(text, i)
        icArray = []
        for row in inArray:icArray.append(ic(row.rstrip()))
        for index in icArray:
            if index < min_ic:
                find = False
                break
            else: find = True
        if find: return icArray
    return 0

def shift_ch(row):
    new_row = []
    alf = choice_alf(row)[0]
    for ch in row: new_row.append(alf[(alf.index(ch.lower())+1)%len(alf)])

    return ''.join(new_row)

def printKeyFor1(text,array_indexes):
    keys = []
    alf = choice_alf(text)[0]
    for ch in alf:
        row = ''
        for ind in array_indexes:
            index = alf.index(ch)
            row += alf[(index-int(ind))%len(alf)]
        keys.append(row)
    return keys

def printKeyFor2(text,array_indexes):

    keys = []
    alf = choice_alf(text)[0]

    for i in range(len(alf)):
        row = ''
        for ind in array_indexes:
            row += alf[(int(ind)+i)%len(alf)]
        keys.append(row)
    return keys

def methodIndex(text,min_ic):
    result = []
    alf,len_text = choice_alf(text)
    icArr = len_key(text,min_ic)
    result.append(icArr)
    if icArr == 0: return 'ic not found'

    rows = text_to_array(text, len(icArr))
    shift = ['-']
    arr_mi = ['-']
    for i in range(1,len(rows)):
        arr_full_mi=[]

        row1, row2 = rows[0].rstrip(), rows[i].rstrip()
        for ch in range(len(alf)):
            row2 = shift_ch(row2)
            arr_full_mi.append(mi(row1,row2))

        shift.append(arr_full_mi.index(max(arr_full_mi))+1)
        arr_mi.append(max(arr_full_mi))
    result.append(arr_mi)
    result.append(shift)
    return result

def create_dict_double(text,count_symb):
    double = dict([])
    for len_window in range(count_symb, 20):
        for i in range(len(text) - len_window):
            window = text[i:i + len_window]
            if text.count(window) > 2 and window not in double.keys():double.update({window: text.count(window)})
    return double

def index_double_row(text,count_symb):
    double = create_dict_double(text,count_symb)
    array_index = []
    for key in double.keys():
        indexes = []
        index = text.index(key)
        while index != -1:
            indexes.append(index)
            index = text.find(key, index + 1)
        if indexes not in array_index:array_index.append(indexes)

    return array_index


def FindAllDivisors(x):
    divList = []
    y = 1
    while y <= sqrt(x):
        if x % y == 0:
            divList.append(y)
            divList.append(int(x / y))
        y += 1
    return divList

def count_diff_div(array_divis):
    array_diff_div = dict([])
    for div in array_divis:
        if div not in array_diff_div.keys():array_diff_div.update({div:array_divis.count(div)})
    return array_diff_div

def sort(dict):
    return{key: value for key, value in sorted(dict.items(), key=lambda item: item[1], reverse=True)}

def freq_len_key (array_len_key):
    freq = dict([])
    for ch in set(array_len_key):
        freq.update({ch:round(array_len_key.count(ch)*99/len(array_len_key),2)})
    return sort(freq)

def get_coef(text):
    array_coef = []
    for t in range(1, 100):
        count = 0
        for i in range(len(text) - t):
            if text[i] == text[i + t]: count += 1
        array_coef.append(count / (len(text) - t))

    return array_coef


def freq_ch(row):

    sum = 0
    alf,len_text = choice_alf(row)

    if 'b' in alf : standart_freq = standart_freq_en
    else: standart_freq = standart_freq_rus

    for i in range(len(alf)):
        count_ch = row.count(alf[i].lower())+row.count(alf[i].upper())
        sum += (((count_ch/len(row))*100 - standart_freq.get(alf[i]))**2)/standart_freq.get(alf[i])


    return round(sum*len(row),2)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

def paintPlot(self, Layout ,x):
       import matplotlib
       matplotlib.rcParams.update({'font.size': 5.5})
       self.figure = plt.figure(figsize=(3,3))
       self.canvas = FigureCanvas(self.figure)

       Layout.addWidget(self.canvas)
       ax = self.figure.add_subplot()
       ax.plot(x)
       plt.grid()
       plt.xticks(range(0,100,5))

       self.canvas.draw()

def plot(text):
    text = text_del_symb(text)
    coefs = get_coef(text)
    return coefs


def methodAutoCorrel(text,count_row):
    text = text_del_symb(text)
    alf = choice_alf(text)[0]
    positions = []

    array_text = text_to_array(text,count_row)
    for row in array_text:
        coef_for_row = []
        for i in range(len(alf)):
            row = shift_ch(row.rstrip())
            coef_for_row.append(freq_ch(row))

        positions.append(coef_for_row.index(min(coef_for_row)))

    return positions



