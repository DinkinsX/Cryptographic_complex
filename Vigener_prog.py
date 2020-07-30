class Vigener:
    def __init__(self, word, key):
        self.word = word
        self.key = key
        self.alphRu = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def dictionary(self):
        d = {}
        it = 0
        for i in range(32, 122):
            d[it] = chr(i)
            it = it + 1
        for i in self.alphRu:
            d[it] = i
            it = it + 1
        return d        

    def encode(self, word):
        listCode = []
        d = self.dictionary()
        for i in range(len(word)):
            for j in d:
                if word[i] == d[j]:
                    listCode.append(j)
        return listCode

    def union(self, value, key):
        dicWord_Key = {}
        it = 0
        full = 0
        for i in value:
            dicWord_Key[full] = [i, key[it]]
            full += 1 
            it += 1
            if it >= len(key):
                it = 0

        return dicWord_Key

    def encodeAll(self, value, key):
        dicWord_Key = self.union(value, key)
        d = self.dictionary()
        encList = []
        for i in dicWord_Key:
            simple = (dicWord_Key[i][0] + dicWord_Key[i][1]) % len(d)
            encList.append(simple)
        return encList

    def decode(self,word):
        listCode = []
        d = self.dictionary()
        for i in range(len(word)):
            for j in d:
                if word[i] == j:
                    listCode.append(d[j])

        return listCode

    def decodeAll(self, value, key):
        dicWord_Key = self.union(value, key)
        #print(dicWord_Key)
        d = self.dictionary()
        decList = []
        for i in dicWord_Key:
            simple = (dicWord_Key[i][0] - dicWord_Key[i][1] + len(d)) % len(d)
            decList.append(simple)
        return decList


'''
word = 'ТБЛЖФЛГЗРЗФАИТЕЧЭЫ'
key = 'sdasddsa'
si = Vigener(word, key)

sim2 = si.encode(word)
sim3 = si.encode(key)

sim5 = si.encodeAll(sim2, sim3)
sim10 = si.decode(sim5)
sim8 = si.decodeAll(sim5, sim3)
sim9 = si.decode(sim8)

print(sim2)
print(sim3)
print('s', sim5)
print(sim9)
print(sim10)'''