from Alf import *

def incrKey(key,text):
    text=text.replace(' ','')
    key *= len(text) // len(key) + 1
    if len(key) > len(text): key = key[:(len(text))]
    return key

def enc (text, key):
    result = []
    key = incrKey(key, text).lower()
    i = 0
    for ch in text:
        if ch in alf1: result.append(alf1[(alf1.index(ch)+alf1.index(key[i]))%len(alf1)])
        elif ch in alf2: result.append(alf2[(alf2.index(ch)+alf1.index(key[i]))%len(alf2)])
        elif ch in alf3: result.append(alf3[(alf3.index(ch) + alf3.index(key[i])) % len(alf3)])
        elif ch in alf4: result.append(alf4[(alf4.index(ch) + alf3.index(key[i])) % len(alf4)])
        else:
            result.append(ch)
            i-=1
        i+=1

    return ''.join(result)

def dec(text, key):
    result = []
    key = incrKey(key, text).lower()
    i = 0
    for ch in text:
        if ch in alf1: result.append(alf1[(alf1.index(ch) - alf1.index(key[i])) % len(alf1)])
        elif ch in alf2: result.append(alf2[(alf2.index(ch) - alf1.index(key[i])) % len(alf2)])
        elif ch in alf3: result.append(alf3[(alf3.index(ch) - alf3.index(key[i])) % len(alf3)])
        elif ch in alf3: result.append(alf4[(alf4.index(ch) - alf3.index(key[i])) % len(alf4)])
        else:
            result.append(ch)
            i -= 1
        i += 1

    return ''.join(result)
