import math
import time
from itertools import cycle

class Gamma:
    def dictionary(self):
        alphRu = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        d = {}
        it = 0
        for i in range(32, 122):
            d[it] = chr(i)
            it = it + 1
        for i in alphRu:
            d[it] = i
            it = it + 1
        return d       

    def lin_rand_arr_flxd(seed,size):
        #Реализация линейного конгруэнтного генератора псевдослучайных чисел. 
        #Возвращает массив заданного размера или случайное число, если указан единичный размер.
        m=155
        a=23
        b=5421

        if size == 1:
            return math.ceil(math.fmod(a * math.ceil(seed) + b, m))

        r = [0 for i in range(size)]
        r[0] = math.ceil(seed)

        for i in range(1,size):
            r[i] = math.ceil(math.fmod((a * r[i - 1] + b), m))
        return r[1:size]

    def encode(self, word):
        listCode = []
        d = self.dictionary()
        for i in range(len(word)):
            for j in d:
                if word[i] == d[j]:
                    listCode.append(j)
        return listCode

    def xorIN(word, key):
        wordX = []
        for a, b in zip(word, cycle(key)):
            wordX.append((int(a) + int(b)) % 155)
        return wordX

    def xorOUT(word, key):
        wordX = []
        for a, b in zip(word, cycle(key)):
            wordX.append((int(a) - int(b) + 155) % 155)
        return wordX

    def decode(self,word):
        listCode = []
        d = self.dictionary()
        for i in range(len(word)):
            for j in d:
                if word[i] == j:
                    listCode.append(d[j])

        return listCode
'''

word = 'чич'
clas = Gamma()
dir1 = clas.encode(word)
key = Gamma.lin_rand_arr_flxd(time.time(), len(word)+1)
print('ke',key)
print('slov', dir1)

sic = Gamma.xorIN(dir1, key)
print('ключ', sic)

sic2 = Gamma.xorOUT(sic, key)

print(sic2)

kira = clas.decode(sic2)

print(kira)'''