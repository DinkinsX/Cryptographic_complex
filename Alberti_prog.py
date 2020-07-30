class Alberti:
    def __init__(self, word, keyAl, key):
        self.key = keyAl
        self.word = word
        self.keyW = key
        self.wordUP = self.word.upper()
        self.alphEn1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
        self.alphEn2 = "abcdefghijklmnopqrstuvwxyz"
        self.alphRu1 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        self.alphRu2 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


    def EncodeEN(self):
        listAlph = list(self.alphEn1)
        alphExtend = []
        alphDisk = []
        wordUPArr = []
        wordUP = self.word.upper()

        for i in wordUP:
            for j in range(len(self.alphEn1)):
                if i == self.alphEn1[j]:
                    wordUPArr.append(j)
        print(wordUPArr)


        for i in self.key:
            for j in range(len(self.alphEn1)):
                if self.alphEn1[j] == i:
                    try:
                        Sym = listAlph.remove(i)
                        alphExtend.append(i)
                    except:
                        print('Одинаковые символы в ключе диска')
        alphExtend.extend(listAlph)
        print('Эквивалент внешнего диска:', alphExtend)
        print(list(self.alphEn1))


        for i in range(len(self.alphEn1)):
            for j in range(len(alphExtend)):
                s = alphExtend[(j-i+len(self.alphEn1)) % len(self.alphEn1)] 
                alphDisk.append(s)


        self.Matrix_Key = []
        k = 0 # просто начальное значение, может быть любым
        for r in range(len(self.alphEn1)): # 26 строк
            self.Matrix_Key.append([]) # создаем пустую строку
            for c in range(len(self.alphEn1)): # в каждой строке - 5 элементов
                self.Matrix_Key[r].append(alphExtend[(c-r+len(self.alphEn1)) % len(self.alphEn1)]) # добавляем очередной элемент в строку
                k += 1 # увеличиваем значение счетчика
        #print('Матрица в строку: ', self.Matrix_Key,'\n')
        for r in self.Matrix_Key:
            print(r)


        keyWposit = []
        for i in self.keyW:
            for j in range(len(self.alphEn1)):
                if i == self.alphEn1[j]:
                    keyWposit.append(j)
        wordWposit = []
        for i in self.word:
            for j in keyWposit:
                if len(wordWposit) < len(self.word):
                    wordWposit.append(j)
        print(wordWposit)

        Xword = []
        for i in range(len(wordWposit)):
            Xword.append(self.Matrix_Key[wordWposit[i]][wordUPArr[i]])
            print(self.Matrix_Key[wordWposit[i]][wordUPArr[i]])
        return Xword


    def EncodeRU(self):
        listAlph = list(self.alphRu1)
        alphExtend = []
        alphDisk = []
        wordUPArr = []
        wordUP = self.word.upper()

        for i in wordUP:
            for j in range(len(self.alphRu1)):
                if i == self.alphRu1[j]:
                    wordUPArr.append(j)
        print(wordUPArr)


        for i in self.key:
            for j in range(len(self.alphRu1)):
                if self.alphRu1[j] == i:
                    try:
                        Sym = listAlph.remove(i)
                        alphExtend.append(i)
                    except:
                        print('Одинаковые символы в ключе диска')
        alphExtend.extend(listAlph)
        print('Эквивалент внешнего диска:', alphExtend)
        print(list(self.alphRu1))


        for i in range(len(self.alphRu1)):
            for j in range(len(alphExtend)):
                s = alphExtend[(j-i+len(self.alphRu1)) % len(self.alphRu1)] 
                alphDisk.append(s)


        self.Matrix_Key = []
        k = 0 # просто начальное значение, может быть любым
        for r in range(len(self.alphRu1)): # 26 строк
            self.Matrix_Key.append([]) # создаем пустую строку
            for c in range(len(self.alphRu1)): # в каждой строке - 5 элементов
                self.Matrix_Key[r].append(alphExtend[(c-r+len(self.alphRu1)) % len(self.alphRu1)]) # добавляем очередной элемент в строку
                k += 1 # увеличиваем значение счетчика
        #print('Матрица в строку: ', self.Matrix_Key,'\n')
        for r in self.Matrix_Key:
            print(r)


        keyWposit = []
        for i in self.keyW:
            for j in range(len(self.alphRu1)):
                if i == self.alphRu1[j]:
                    keyWposit.append(j)
        wordWposit = []
        for i in self.word:
            for j in keyWposit:
                if len(wordWposit) < len(self.word):
                    wordWposit.append(j)
        print(wordWposit)

        Xword = []
        for i in range(len(wordWposit)):
            Xword.append(self.Matrix_Key[wordWposit[i]][wordUPArr[i]])
            print(self.Matrix_Key[wordWposit[i]][wordUPArr[i]])
        return Xword


    def DecodeRU(self):
        listAlph = list(self.alphRu1)
        alphExtend = []
        alphDisk = []
        wordUPArr = []
        wordUP = self.word.upper()

        for i in wordUP:
            for j in range(len(self.alphRu1)):
                if i == self.alphRu1[j]:
                    wordUPArr.append(j)
        print(wordUPArr)


        for i in self.key:
            for j in range(len(self.alphRu1)):
                if self.alphRu1[j] == i:
                    try:
                        Sym = listAlph.remove(i)
                        alphExtend.append(i)
                    except:
                        print('Одинаковые символы в ключе диска')
        alphExtend.extend(listAlph)
        print('Эквивалент внешнего диска:', alphExtend)
        print(list(self.alphRu1))


        for i in range(len(self.alphRu1)):
            for j in range(len(alphExtend)):
                s = alphExtend[(j-i+len(self.alphRu1)) % len(self.alphRu1)] 
                alphDisk.append(s)


        self.Matrix_Key = []
        k = 0 # просто начальное значение, может быть любым
        for r in range(len(self.alphRu1)): # 26 строк
            self.Matrix_Key.append([]) # создаем пустую строку
            for c in range(len(self.alphRu1)): # в каждой строке - 5 элементов
                self.Matrix_Key[r].append(alphExtend[(c-r+len(self.alphRu1)) % len(self.alphRu1)]) # добавляем очередной элемент в строку
                k += 1 # увеличиваем значение счетчика
        #print('Матрица в строку: ', self.Matrix_Key,'\n')
        for r in self.Matrix_Key:
            print(r)


        keyWposit = []
        for i in self.keyW:
            for j in range(len(self.alphRu1)):
                if i == self.alphRu1[j]:
                    keyWposit.append(j)
        wordWposit = []
        for i in self.word:
            for j in keyWposit:
                if len(wordWposit) < len(self.word):
                    wordWposit.append(j)
        Xword = []
        for i in range(len(wordWposit)):
            for j in range(len(self.Matrix_Key[i])):
                if self.wordUP[i] == self.Matrix_Key[wordWposit[i]][j]:
                    Xword.append(self.alphRu2[j])
        return Xword

    def DecodeEN(self):
        listAlph = list(self.alphEn1)
        alphExtend = []
        alphDisk = []
        wordUPArr = []
        wordUP = self.word.upper()

        for i in wordUP:
            for j in range(len(self.alphEn1)):
                if i == self.alphEn1[j]:
                    wordUPArr.append(j)
        print(wordUPArr)


        for i in self.key:
            for j in range(len(self.alphEn1)):
                if self.alphEn1[j] == i:
                    try:
                        Sym = listAlph.remove(i)
                        alphExtend.append(i)
                    except:
                        print('Одинаковые символы в ключе диска')
        alphExtend.extend(listAlph)
        print('Эквивалент внешнего диска:', alphExtend)
        print(list(self.alphEn1))


        for i in range(len(self.alphEn1)):
            for j in range(len(alphExtend)):
                s = alphExtend[(j-i+len(self.alphEn1)) % len(self.alphEn1)] 
                alphDisk.append(s)


        self.Matrix_Key = []
        k = 0 # просто начальное значение, может быть любым
        for r in range(len(self.alphEn1)): # 26 строк
            self.Matrix_Key.append([]) # создаем пустую строку
            for c in range(len(self.alphEn1)): # в каждой строке - 5 элементов
                self.Matrix_Key[r].append(alphExtend[(c-r+len(self.alphEn1)) % len(self.alphEn1)]) # добавляем очередной элемент в строку
                k += 1 # увеличиваем значение счетчика
        #print('Матрица в строку: ', self.Matrix_Key,'\n')
        for r in self.Matrix_Key:
            print(r)


        keyWposit = []
        for i in self.keyW:
            for j in range(len(self.alphEn1)):
                if i == self.alphEn1[j]:
                    keyWposit.append(j)
        wordWposit = []
        for i in self.word:
            for j in keyWposit:
                if len(wordWposit) < len(self.word):
                    wordWposit.append(j)
        print(wordWposit)

        Xword = []
        for i in range(len(wordWposit)):
            for j in range(len(self.Matrix_Key[i])):
                if self.wordUP[i] == self.Matrix_Key[wordWposit[i]][j]:
                    Xword.append(self.alphEn2[j])
        return Xword

'''word = 'МАМОЧКА'
key = 'АЛИК'
key2 = 'МИР'

s = Alberti(word, key, key2)

print(s.EncodeRU())

word2 = 'АЧЬИОЪУ'
key4 = 'АЛИК'
key5 = 'МИР'


d = Alberti(word2, key4, key5)
print(d.DecodeRU())'''

'''
word = 'mama рипа mia'
print(word)

key1 = 'sad'
key2 = 'SAC'  
key1UP = key1.upper()
key2UP = key2.upper()

wordlist = list(word)
wordlistRecc = list(word)
specSymbPos = []
specSymb = []
symEn = []
symEnPos = []
symRu = []
symRuPos = []
wordEn = ''
wordRu = ''

for i in range(len(word)):
    if 65 <= ord(word[i]) <= 122:
        symEn.append(word[i])
        wordlist.remove(word[i])
        print(symEn)
        symEnPos.append(i)

    elif 1025 <= ord(word[i]) <= 1105:
        symRu.append(word[i])
        wordlist.remove(word[i])
        symRuPos.append(i)

    else:
        specSymb.append(word[i])
        wordlist.remove(word[i])
        specSymbPos.append(i)
        print(specSymb)

wordEn.join(symEn)
wordRu.join(symRu)
albertEn = Alberti(wordEn, key1UP, key2UP)
enW = albertEn.EncodeEN()

albertRu = Alberti(wordEn, key1UP, key2UP)
enW2 = albertRu.EncodeRU()

for i in range(len(symEn)):
    wordlistRecc[symEnPos[i]] = enW[i]

for i in range(len(specSymbPos)):
    wordlistRecc[specSymbPos[i]] = specSymb[i]



print(wordlistRecc)
print(wordEn.join(symEn))

'''
