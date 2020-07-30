from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QAbstractScrollArea, QVBoxLayout, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from Alf import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import re
import matplotlib.pyplot as plt



class Ui_AnalysisFreq(object):

    def setupUi(self, AnalysisFreq):
        AnalysisFreq.setObjectName("AnalysisFreq")
        AnalysisFreq.resize(1000, 550)
        AnalysisFreq.setMinimumSize(QtCore.QSize(1000, 550))
        AnalysisFreq.setMaximumSize(QtCore.QSize(1000, 550))
        self.centralwidget = QtWidgets.QWidget(AnalysisFreq)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 215, 151, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(161, 215, 151, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 260, 990, 150))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QtCore.QRect(10, 420, 800, 100))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QtCore.QRect(500, 430, 800, 100))

        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 10, 990, 200))
        self.formLayoutWidget.setObjectName("formLayoutWidget")

        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        #self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        #self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        #self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 210, 990, 200))
        #self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")

        #self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        #self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        #self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        #self.formLayout_2.setObjectName("formLayout_2")

        AnalysisFreq.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AnalysisFreq)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 672, 22))
        self.menubar.setObjectName("menubar")
        AnalysisFreq.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AnalysisFreq)
        self.statusbar.setObjectName("statusbar")
        AnalysisFreq.setStatusBar(self.statusbar)

        self.retranslateUi(AnalysisFreq)
        QtCore.QMetaObject.connectSlotsByName(AnalysisFreq)

    def retranslateUi(self, AnalysisFreq):
        _translate = QtCore.QCoreApplication.translate
        AnalysisFreq.setWindowTitle(_translate("AnalysisFreq", "Частотный криптоанализ"))
        self.pushButton.setText(_translate("AnalysisFreq", "Замена стандартными\nчастотами"))
        self.pushButton_3.setText(_translate("AnalysisFreq", "Заменить"))
        self.label_2.setText(_translate("AnalysisFreq", "Стандартные частоты для английского алфавита:\n"
        "a:8.17|b:1.49|c:2.78|d:4.25|e:12.7|f:2.23|g:2.02|h:6.09|i:6.97\n"
        "j:0.15|k:0.77|l:4.03|m:2.41|n:6.75|o:7.51|p:1.93|q:0.10|r:5.99\n"
        "s:6.33|t:9.06|u:2.76|v:0.98|w:2.36|x:0.15|y:1.97|z:0.05\n"))

        self.label_3.setText(_translate("AnalysisFreq", "Стандартные частоты для русского алфавита:\n"
        "а:8.01|б:1.59|в:4.54|г:1.70|д:2.98|е:8.450|ё:0.04|ж:0.94|з:1.65|и:7.35\n"
        "й:1.21|к:3.49|л:4.40|м:3.21|н:6.70|о:10.97|п:2.81|р:4.73|с:5.47\n"
        "т:6.26|у:2.62|ф:0.26|х:0.97|ц:0.48|ч:1.440|ш:0.73|щ:0.36|ь:1.74\n"
        "ы:1.90|ъ:0.04|э:0.32|ю:0.64|я:2.01\n"))

    def paintPlot(self, Layout ,x, y):
        import matplotlib
        matplotlib.rcParams.update({'font.size': 5.5})
        self.figure = plt.figure(figsize=(6.6,1.9))
        self.canvas = FigureCanvas(self.figure)
        Layout.addWidget(self.canvas)
        ax = self.figure.add_subplot()
        ax.bar(x,y)
        ax.grid()
        y_ticks = []
        last = 0
        for y_ in y:
            if abs(y_ - last) > 0.6:
                y_ticks.append(y_)
                last = y_
        plt.yticks(y_ticks)
        self.canvas.draw()



def choice_alf (text):
    res = ''.join(re.findall('[A-Za-zА-Яа-яёЁ]', text))
    if res[0].lower() in alf1: return alf1,len(res)
    elif res[0].lower() in alf3: return alf3,len(res)

def freq_ch(text):
    array = dict([])
    alf,len_text = choice_alf(text)
    text = list(text)
    for ch in alf:
        array.update([(ch, round((text.count(ch.lower())+text.count(ch.upper()))/len_text*100,2))])
    return array


def sort_freq(freq_text):
    return({key: value for key, value in sorted(freq_text.items(), key=lambda item: item[1], reverse=True)})

def text_to_table(table,text,str):
    i=0
    for ch in text:
        item = QTableWidgetItem(ch)
        if str == 0:item.setFlags(QtCore.Qt.ItemIsEnabled)
        table.setItem(str, i, item)
        i+=1

def table_to_text(table,str):
    array = []
    for i in range(table.columnCount()):
        array.append(table.model().index(str,i).data())
    return array

def decrypt(text,array_ch,new_ch):
    result = []
    for ch in text:
        if ch.lower() in array_ch and new_ch[array_ch.index(ch.lower())] != None:
            if ch.islower():result.append(new_ch[array_ch.index(ch.lower())])
            else: result.append(new_ch[array_ch.index(ch.lower())].upper())
        else: result.append(ch)

    return ''.join(result)
