alphEn1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ" 
alphEn2 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
alphRu1 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphRu2 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def encriptC(encr, key):
    key = int(key)
    keyEn = 0
    keyRu = 0

    if key > 26:
    	keyEn = key % 26
    else:
    	keyEn = key

    if key > 33:
    	keyRu = key % 33
    else:
    	keyRu = key

    encred = ""
    print(encr)

    for let in encr:
        pos = alphEn1.find(let)
        newPos = pos + keyEn

        pos2 = alphEn2.find(let)
        newPos2 = pos2 + keyEn

        pos3 = alphRu1.find(let)
        newPos3 = pos3 + keyRu 

        pos4 = alphRu2.find(let)
        newPos4 = pos4 + keyRu 

        if let in alphEn1:
            encred = encred + alphEn1[newPos]

        elif let in alphEn2:
            encred = encred + alphEn2[newPos2]  

        elif let in alphRu1:
            encred = encred + alphRu1[newPos3] 

        elif let in alphRu2:
            encred = encred + alphRu2[newPos4] 

        else:
            encred = encred + let

    print(encred)
    return encred

def decriptC(encr, key):
    key = int(key)    
    encred = ""
    keyEn = 0
    keyRu = 0
    if key > 26:
    	keyEn = key % 26
    else:
    	keyEn = key

    if key > 33:
    	keyRu = key % 33
    else:
    	keyRu = key

    for let in encr:
        pos = alphEn1.find(let)
        newPos = pos - keyEn

        pos2 = alphEn2.find(let)
        newPos2 = pos2 - keyEn

        pos3 = alphRu1.find(let)
        newPos3 = pos3 - keyRu

        pos4 = alphRu2.find(let)
        newPos4 = pos4 - keyRu

        if let in alphEn1:
            encred = encred + alphEn1[newPos]

        elif let in alphEn2:
            encred = encred + alphEn2[newPos2]  

        elif let in alphRu1:
            encred = encred + alphRu1[newPos3] 

        elif let in alphRu2:
            encred = encred + alphRu2[newPos4] 

        else:
            encred = encred + let

    print(encred)
    return encred