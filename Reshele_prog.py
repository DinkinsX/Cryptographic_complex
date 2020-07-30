def ResheleEn(word, key):
    keySplit = key.split()
    Xword = []
    wordPart = []
    for i in range(len(keySplit)):
        lenPart = len(keySplit[i])
        wordPart.append(word[:lenPart])
        word = word[lenPart:]
        for j in keySplit[i]:
            Xword.append(wordPart[i][int(j) - 1])
    print(Xword)
    return Xword

def ResheleDe(word, key):
    keySplit = key.split()
    Xword = []
    wordPart = []
    for i in range(len(keySplit)):
        lenPart = len(keySplit[i])
        wordPart.append(word[:lenPart])
        word = word[lenPart:]
        wordPartPromo = list(wordPart[i])

        for j in range(len(keySplit[i])):
            wordPartPromo[int(keySplit[i][j]) - 1] = wordPart[i][j]
            print(wordPartPromo)

        for e in wordPartPromo:
            Xword.append(e)

    print(Xword)        
    return Xword

'''

key = '15243 123456'
key2 = '15243 123456'

word = 'Всем!привет'
Xword = ResheleEn(word, key)
print('1', ''.join(Xword))

word2 = 'В!смепривет'
Xword2 = ResheleDe(word2, key2)
print(''.join(Xword2))'''
