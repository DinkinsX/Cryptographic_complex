class Critpta:
    def __init__(self):
        #self.encr = word
        #self.keyWord = key
        self.keyEn = []
        self.keyRu = []
        self.alphEn1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ" 
        self.alphEn2 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        self.alphRu1 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        self.alphRu2 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"


        self.standart_freq_en = dict([('a',8.17),('b',1.49),('c',2.78),('d',4.25),('e',12.7),('f',2.23),('g',2.02),('h',6.09),('i',6.97),
                ('j',0.15),('k',0.77),('l',4.03),('m',2.41),('n',6.75),('o',7.51),('p',1.93),('q',0.1),('r',5.99),
                ('s',6.33),('t',9.06),('u',2.76),('v',0.98),('w',2.36),('x',0.15),('y',1.97),('z',0.05)])

        self.standart_freq_rus = dict([('а',8.01),('б',1.59),('в',4.54),('г',1.70),('д',2.98),('е',8.45),('ё',0.04),('ж',0.94),('з',1.65),('и',7.35),
                        ('й',1.21),('к',3.49),('л',4.40),('м',3.21),('н',6.70),('о',10.97),('п',2.81),('р',4.73),('с',5.47),
                        ('т',6.26),('у',2.62),('ф',0.26),('х',0.97),('ц',0.48),('ч',1.44),('ш',0.73),('щ',0.36),('ь',1.74),
                         ('ы',1.90),('ъ',0.04),('э',0.32),('ю',0.64),('я',2.01)])

        print(self.standart_freq_rus)


    def paintPlot(self, Layout ,x, y):
        import matplotlib
        matplotlib.rcParams.update({'font.size': 5.5})

        self.figure = plt.figure(figsize=(6.6,1.9))
        self.canvas = FigureCanvas(self.figure)

        Layout.addWidget(self.canvas)

        ax = self.figure.add_subplot()
        ax.bar(x,y)
        ax.grid()
        yticks = []
        last = 0
        for y in y:
            if abs(y_ - last) > 0.6:
                yticks.append(y)
                last = y_
        plt.yticks(y_ticks)
        self.canvas.draw()

G = Critpta()

s = G.paintPlot(5, 1, 1)
print(s)