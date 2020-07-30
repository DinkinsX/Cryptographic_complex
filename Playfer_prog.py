class Playfer:
    def __init__(self, word):
        self.word = word
        #self.key = key
        self.word = self.word.upper()
        self.word = [i for i in self.word]

        for i in range(len(self.word)):
            if self.word[i] == "J":
                self.word[i] = "I"

        for i in range(len(self.word)):
            if self.word[i] == "Ё":
                self.word[i] = "Е"
            elif self.word[i] == "Й":
                self.word[i] = "И"
            elif self.word[i] == "Ъ":
                self.word[i] = "Ь"


        if 65 <= min([ord(i) for i in self.word]) <= 122:
            self.matrix = [['A', 'B', 'C', 'D', 'E'],
                          ['F', 'G', 'H', 'I', 'K'],
                          ['L', 'M', 'N', 'O', 'P'],
                          ['Q', 'R', 'S', 'T', 'U'],
                          ['V', 'W', 'X', 'Y', 'Z']]

            for i in range(1, len(self.word)):
                if self.word[i] == self.word[i-1]:
                    self.word.insert(i,"X")

            if len(self.word) % 2 != 0:
                self.word.append("X")
                 
            print('s', self.word)

        elif 1025 <= min([ord(i) for i in self.word]) <= 1105:
            self.matrix = [['А', 'Б', 'В', 'Г', 'Д'],
                          ['Е', 'Ж', 'З', 'И', 'К'],
                          ['Л', 'М', 'Н', 'О', 'П'],
                          ['Р', 'С', 'Т', 'У', 'Ф'],
                          ['Х', 'Ц', 'Ч', 'Ш', 'Щ'],
                          ['Ы', 'Ь', 'Э', 'Ю', 'Я']]

            for i in range(1, len(self.word)):
                if self.word[i] == self.word[i-1]:
                    self.word.insert(i,"Х")

            if len(self.word) % 2 != 0:
                self.word.append("Х")

    def encrypt(self):
        twoSimb = []
        count = ""
        for i in self.word:
            count += i

            if len(count) == 2:
                twoSimb.append(count)
                count = ""

        self.encript = ""
        switchMode = False
        for i in range(len(twoSimb)):
            for count in range(2):
                for x in range(len(self.matrix)):
                    for y in range(len(self.matrix[x])): #Если равен символу из откр сообщ
                        if self.matrix[x][y] == twoSimb[i][count]:
                            if twoSimb[i][0] in self.matrix[x] and twoSimb[i][1] in self.matrix[x]:
                                if self.matrix[x][y] != self.matrix[x][-1]:   
                                    self.encript += self.matrix[x][y+1]
                                else:   
                                    self.encript += self.matrix[x][y-4]

                            else:
                                for a in range(len(self.matrix)):
                                    for b in range(len(self.matrix[a])):
                                        if self.matrix[a][b] == twoSimb[i][0]:
                                            coordinate1 = a
                                        if self.matrix[a][b] == twoSimb[i][1]:
                                            coordinate2 = a

                                if switchMode == False:
                                    self.encript += self.matrix[coordinate2][y]
                                    switchMode = True
                                else:
                                    self.encript += self.matrix[coordinate1][y]
                                    switchMode = False
        return self.encript

    def decrypt(self):
        twoSimb = []
        count = ""
        for i in self.word:
            count += i
            if len(count) == 2:
                twoSimb.append(count)
                count = ""

        print(twoSimb)
        decript = []
        switchMode = False

        for i in range(len(twoSimb)):
            for count in range(2):
                for x in range(len(self.matrix)):
                    for y in range(len(self.matrix[x])): #Если равен символу из откр сообщ
                        if self.matrix[x][y] == twoSimb[i][count]:
                            if twoSimb[i][0] in self.matrix[x] and twoSimb[i][1] in self.matrix[x]:
                                if self.matrix[x][y] != self.matrix[x][0]:   
                                    decript.append(self.matrix[x][y - 1])
                                else:   
                                    decript.append(self.matrix[x][y + 4])

                            else:
                                for a in range(len(self.matrix)):
                                    for b in range(len(self.matrix[a])):
                                        if self.matrix[a][b] == twoSimb[i][0]:
                                            coordinate1 = a
                                        if self.matrix[a][b] == twoSimb[i][1]:
                                            coordinate2 = a

                                if switchMode == False:
                                    decript.append(self.matrix[coordinate2][y])
                                    switchMode = True
                                else:
                                    decript.append(self.matrix[coordinate1][y])
                                    switchMode = False

        print(decript)
        print(len(decript))
        print(decript[-1])
        #print(decript[19])
        decript2 = ''.join(decript)

        print("ss", decript2)

        for i in range(len(decript)-1):
            print(i)
            if 65 <= min([ord(i) for i in self.word]) <= 122:
                if decript[i] == "X":
                    if decript[i] != decript[-1]:
                        if decript[i-1] == decript[i+1]:
                            decript.remove(decript[i])
                    else:
                        decript.remove(decript[i])
                if decript[-1] == "X":
                    decript.remove(decript[-1])

            elif 1025 <= min([ord(i) for i in self.word]) <= 1105:
                if decript[i] == "Х":
                    if decript[i] != decript[-1]:
                        if decript[i-1] == decript[i+1]:
                            decript.remove(decript[i])

                    else:
                        decript.remove(decript[i])

                if decript[-1] == "Х":
                    decript.remove(decript[-1])

        decriptOUT = ''.join(decript)
        return decriptOUT
'''
s = Playfer('ммама')
sac = s.encrypt()
print('ВЫВОД', sac)


si = Playfer('ТБЛЖФЛГЗРЗФАИТЕЧЭЫ')
sim = si.decrypt()
print(sim)
'''
'''
Matrix_Key = []
k = 0 # просто начальное значение, может быть любым
for r in range(2): # 5 строк
    Matrix_Key.append([]) # создаем пустую строку
    for c in range(2): # в каждой строке - 5 элементов
        Matrix_Key[r].append(key[k]) # добавляем очередной элемент в строку
        k += 1 # увеличиваем значение счетчика'''
'''

massSimb = []
massSimbCount = []
for i in range(len(word)):
    if 32 <= ord(word[i]) < 65:
        massSimbCount.append(i)
        massSimb.append(word[i])

print('sas', massSimb)
print('sas', massSimbCount)
print('ssss', word[8])
wordNext = []

for i in range(len(word)):
    for j in range(len(massSimb)):
        if word[i] == massSimb[j]:
            word.remove(word[i])


print(massSimbCount)'''
"""
twoSimb = []
count = ""

for i in word:
    count += i

    if len(count) == 2:
        twoSimb.append(count)
        count = ""

print(word)
print(twoSimb)

matrix = [['A', 'B', 'C', 'D', 'E'],
          ['F', 'G', 'H', 'I', 'K'],
          ['L', 'M', 'N', 'O', 'P'],
          ['Q', 'R', 'S', 'T', 'U'],
          ['V', 'W', 'X', 'Y', 'Z']]


matrix = [['А', 'Б', 'В', 'Г', 'Д'],
          ['Е', 'Ж', 'З', 'И', 'К'],
          ['Л', 'М', 'Н', 'О', 'П'],
          ['Р', 'С', 'Т', 'У', 'Ф'],
          ['Х', 'Ц', 'Ч', 'Ш', 'Щ'],
          ['Ы', 'Ь', 'Э', 'Ю', 'Я']]

encript = ""
switchMode = False

for i in range(len(twoSimb)):
    for count in range(2):
        for x in range(len(matrix)):
            for y in range(len(matrix[x])): #Если равен символу из откр сообщ
                if matrix[x][y] == twoSimb[i][count]:
                    if twoSimb[i][0] in matrix[x] and twoSimb[i][1] in matrix[x]:
                        if matrix[x][y] != matrix[x][-1]:   
                            encript += matrix[x][y+1]
                        else:   
                            encript += matrix[x][y-4]

                    else:
                        for a in range(len(matrix)):
                            for b in range(len(matrix[a])):
                                if matrix[a][b] == twoSimb[i][0]:
                                    coordinate1 = a
                                if matrix[a][b] == twoSimb[i][1]:
                                    coordinate2 = a

                        if switchMode == False:
                            encript += matrix[coordinate2][y]
                            switchMode = True
                        else:
                            encript += matrix[coordinate1][y]
                            switchMode = False
print('sssss', encript)


twoSimb = []
count = ""
for i in encript:
    count += i
    if len(count) == 2:
        twoSimb.append(count)
        count = ""

print(twoSimb)
decript = []
switchMode = False

for i in range(len(twoSimb)):
    for count in range(2):
        for x in range(len(matrix)):
            for y in range(len(matrix[x])): #Если равен символу из откр сообщ
                if matrix[x][y] == twoSimb[i][count]:
                    if twoSimb[i][0] in matrix[x] and twoSimb[i][1] in matrix[x]:
                        if matrix[x][y] != matrix[x][0]:   
                            decript.append(matrix[x][y - 1])
                        else:   
                            decript.append(matrix[x][y + 4])

                    else:
                        for a in range(len(matrix)):
                            for b in range(len(matrix[a])):
                                if matrix[a][b] == twoSimb[i][0]:
                                    coordinate1 = a
                                if matrix[a][b] == twoSimb[i][1]:
                                    coordinate2 = a

                        if switchMode == False:
                            decript.append(matrix[coordinate2][y])
                            switchMode = True
                        else:
                            decript.append(matrix[coordinate1][y])
                            switchMode = False

print(decript)
print(len(decript))
print(decript[-1])
#print(decript[19])
decript2 = ''.join(decript)

print("ss", decript2)

for i in range(len(decript)-1):
    print(i)
    if decript[i] == "Х":
        if decript[i] != decript[-1]:
            if decript[i-1] == decript[i+1]:
                decript.remove(decript[i])
        else:
            decript.remove(decript[i])

decriptOUT = ''.join(decript)
"""
'''word = 'ПривеТандрей'
d = Playfer(word)
ar = d.encrypt()
print(ar)

gd = d.decrypt()
print(gd)'''