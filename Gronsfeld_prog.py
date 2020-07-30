class Gronsfeld:
    def __init__(self, word, key):
        self.encr = word
        self.keyWord = key
        self.keyEn = []
        self.keyRu = []
        self.alphEn1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ" 
        self.alphEn2 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        self.alphRu1 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        self.alphRu2 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        for key in self.keyWord:
            if key > 26:
                self.keyEn.append(key % 26)
            else:
                self.keyEn.append(key)

            if key > 33:
                self.keyRu.append(key % 33)
            else:
                self.keyRu.append(key)
        print('Eng', self.keyEn)
        print('Rus', self.keyRu)

    def encriptC(self):
        encred = ""
        keyChar = 0
        for let in self.encr:
            pos = self.alphEn1.find(let)
            newPos = pos + self.keyEn[keyChar]

            pos2 = self.alphEn2.find(let)
            newPos2 = pos2 + self.keyEn[keyChar]

            pos3 = self.alphRu1.find(let)
            newPos3 = pos3 + self.keyRu[keyChar] 

            pos4 = self.alphRu2.find(let)
            newPos4 = pos4 + self.keyRu[keyChar] 

            if let in self.alphEn1:
                encred = encred + self.alphEn1[newPos]

            elif let in self.alphEn2:
                encred = encred + self.alphEn2[newPos2]  

            elif let in self.alphRu1:
                encred = encred + self.alphRu1[newPos3] 

            elif let in self.alphRu2:
                encred = encred + self.alphRu2[newPos4] 

            else:
                encred = encred + let

            keyChar += 1

            print(keyChar)
        print(encred)
        return encred

    def decriptC(self):  
        encred = ""
        keyChar = 0
        for let in self.encr:
            pos = self.alphEn1.find(let)
            newPos = pos - self.keyEn[keyChar]

            pos2 = self.alphEn2.find(let)
            newPos2 = pos2 - self.keyEn[keyChar]

            pos3 = self.alphRu1.find(let)
            newPos3 = pos3 - self.keyRu[keyChar]

            pos4 = self.alphRu2.find(let)
            newPos4 = pos4 - self.keyRu[keyChar]

            if let in self.alphEn1:
                encred = encred + self.alphEn1[newPos]

            elif let in self.alphEn2:
                encred = encred + self.alphEn2[newPos2]  

            elif let in self.alphRu1:
                encred = encred + self.alphRu1[newPos3] 

            elif let in self.alphRu2:
                encred = encred + self.alphRu2[newPos4] 

            else:
                encred = encred + let

            keyChar += 1
            print(keyChar)
        print(encred)
        return encred


'''
encr1 = 'abc'
key1 = '1 2 3 6 67 72614'


key = key1.split(" ")

print(key)

#f = encriptC(encr, key)
keyArr = []
for i in range(len(key)):
    keyInt = int(key[i])
    keyArr.append(keyInt)

keyArrFull = []
print(len(keyArr))
for i in range(0, len(encr1), len(keyArr)):
    for j in range(len(keyArr)):
        keyArrFull.append(keyArr[j])

keyArrFullFull = []
for i in range(len(encr1)):
    keyArrFullFull.append(keyArrFull[i])


print('aaa', keyArrFull)       
print(keyArr)
enc = Gronsfeld(encr1, keyArrFullFull)
encer = enc.encriptC()
print(encer)
enc2 = Gronsfeld(encer, keyArrFullFull)

encer2 = enc2.decriptC()

'''