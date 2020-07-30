class Polibi:
    def __init__(self, word):
        self.word = word
        if 65 <= min([ord(i) for i in self.word]) <= 122:
            self.b = [['A', 'B', 'C', 'D', 'E'],
                      ['F', 'G', 'H', 'I', 'K'],
                      ['L', 'M', 'N', 'O', 'P'],
                      ['Q', 'R', 'S', 'T', 'U'],
                      ['V', 'W', 'X', 'Y', 'Z']]
        elif 1025 <= min([ord(i) for i in self.word]) <= 1105 or [i for i in self.word if i == 'X' or i == 'X']:
            self.b = [['А', 'Б', 'В', 'Г', 'Д', 'Е'],
                      ['Ё', 'Ж', 'З', 'И', 'Й', 'К'],
                      ['Л', 'М', 'Н', 'О', 'П', 'Р'],
                      ['С', 'Т', 'У', 'Ф', 'Х', 'Ц'],
                      ['Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь'],
                      ['Э', 'Ю', 'Я', 'x1', 'x2', 'x3']]

        self.matri_Height, self.matri_Width = len(self.b), len(self.b[0])
        print(len(self.b[0]))
        self.coor_horizontal, self.coor_vertical = [], []
        self.answer = []
        self.len = len(self.word)
        self.non_repeat_word = str()
        
        for i in range(len(self.word)):
            if not self.word[i] in self.word[0:i]:
                self.non_repeat_word += (self.word[i])

        print(self.non_repeat_word)

    def encrypting(self, word):
            for i in range(len(self.coor_horizontal)):
                if self.coor_vertical[i] + 1 <= self.matri_Height:
                    self.coor_vertical[i] += 1
                else:
                    self.coor_vertical[i] = 1
                self.answer.append(
                                  self.b
                                  [self.coor_vertical[i] - 1]
                                  [self.coor_horizontal[i] - 1]
                                  )
            return ''.join(self.answer)

    def decrypting(self, word):
        self.answer = []

        for i in range(len(self.coor_horizontal)):
            if self.coor_vertical[i] - 1 <= self.matri_Height:
                self.coor_vertical[i] -= 1
            else:
                self.coor_vertical[i] = self.matri_Height
            self.answer.append(
                               self.b
                               [self.coor_vertical[i] - 1]
                               [self.coor_horizontal[i] - 1]
                               )
        return ''.join(self.answer)    


    def enumeration_encrypting(self, b, symbol, word):
        flag = False
        for j in range(self.matri_Height):
            for i in range(self.matri_Width):
                if b[i][j].count(symbol.upper()) == 1:
                    self.coor_horizontal.append(j + 1)
                    self.coor_vertical.append(i + 1)
                    flag = True
                    break
            if flag:
                flag = False
                break
        return (self.coor_vertical, self.coor_horizontal)

    def coordinate(self, word):
        for k in range(len(word)):
            symbol = word[k:len(word) - (len(word) - 1 - k)]
            if symbol.lower() != 'j':
                self.coor_vertical, self.coor_horizontal = self.enumeration_encrypting(self.b, symbol, word)
            else:
                self.coor_vertical, self.coor_horizontal = self.enumeration_encrypting(self.b, 'i', word)
 

'''
word = 'sagh'
print(ord('ё'))
polybius = Polibi()
poli1 = polybius.coordinate()

#print('{}'.format(bla.decrypting().upper()))
print('Введенное слово: {}\nЗашифованое слово Методом 1: {}\n'.format(word.upper(), polybius.decrypting().upper()))
print(ord('я'))  
'''

#print(ord('Ё'))