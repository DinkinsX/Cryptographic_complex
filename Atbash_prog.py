def form_dict():
    d1 = {0: 'а', 1: 'б', 2: 'в', 3: 'г', 4: 'д', 5: 'е', 6: 'ё', 7: 'ж', 8: 'з', 9: 'и', 10: 'й', 11: 'к', 12: 'л', 13: 'м', 14: 'н', 15: 'о', 16: 'п', 17: 'р', 18: 'с', 19: 'т', 20: 'у', 
     21: 'ф', 22: 'х', 23: 'ц', 24: 'ч', 25: 'ш', 26: 'щ', 27: 'ъ', 28: 'ы', 29: 'ь', 30: 'э', 31: 'ю', 32: 'я'}
    d2 = {33: 'А', 34: 'Б', 35: 'В', 36: 'Г', 37: 'Д', 38: 'Е', 39: 'Ё', 40: 'Ж', 41: 'З', 42: 'И', 43: 'Й', 44: 'К', 45: 'Л', 46: 'М', 47: 'Н', 48: 'О', 49: 'П',
     50: 'Р', 51: 'С', 52: 'Т', 53: 'У', 54: 'Ф', 55: 'Х', 56: 'Ц', 57: 'Ч', 58: 'Ш', 59: 'Щ', 60: 'Ъ', 61: 'Ы', 62: 'Ь', 63: 'Э', 64: 'Ю', 65: 'Я'}
    d3 = {67: 'a', 68: 'b', 69: 'c', 70: 'd', 71: 'e', 72: 'f', 73: 'g', 74: 'h', 75: 'i', 76: 'j', 77: 'k', 78: 'l', 79: 'm', 80: 'n', 81: 'o',
     82: 'p', 83: 'q', 84: 'r', 85: 's', 86: 't', 87: 'u', 88: 'v', 89: 'w', 90: 'x', 91: 'y', 92: 'z'}
    d4 = {93: 'A', 94: 'B', 95: 'C', 96: 'D', 97: 'E', 98: 'F', 99: 'G', 100: 'H', 101: 'I', 102: 'J', 103: 'K', 104: 'L', 105: 'M', 106: 'N', 107: 'O',
     108: 'P', 109: 'Q', 110: 'R', 111: 'S', 112: 'T', 113: 'U', 114: 'V', 115: 'W', 116: 'X', 117: 'Y', 118: 'Z'} 
    d5 = {119: ' ', 120: '!', 121: '?', 122: '1', 123: '2', 131: '3', 124: '4', 125: '5', 126: '6', 127: '7', 128: '8', 129: '9', 130: '0'}
    return d1, d2, d3, d4, d5

def encode_val(word):
    list_code = []
    lent = len(word)
    print(len(word))
    d = form_dict()
    d1 = d[0]
    d2 = d[1]
    d3 = d[2]
    d4 = d[3]
    d5 = d[4]

    for w in range(lent):
        for value in d1:
            if word[w] == d1[value]:
               list_code.append(value)
        for value in d2:
            if word[w] == d2[value]:
               list_code.append(value)    
        for value in d3:
            if word[w] == d3[value]:
               list_code.append(value)
        for value in d4:
            if word[w] == d4[value]:
               list_code.append(value)
        for value in d5:
            if word[w] == d5[value]:
                list_code.append(value)
        


    print(list_code)
    return list_code

def reversedict(dic):
	d = dic
	dict_as_list = list(d.values())
	dict_as_list.reverse()
	dict_keys = list(d.keys())

	list_as_dict = {dict_keys[i] : dict_as_list[i] for i in range(0, len(dict_as_list))}
	#print(d)
	#print(dict_keys)
	return list_as_dict

def encript(value_encoded):
    list_code = []
    lent = len(value_encoded)
    d = form_dict()
    d1 = d[0]
    d2 = d[1]
    d3 = d[2]
    d4 = d[3]
    d5 = d[4]


    d1 = reversedict(d1)
    d2 = reversedict(d2)
    d3 = reversedict(d3)
    d4 = reversedict(d4)


    for i in range(lent):
        for value in d1:
            if value_encoded[i] == value:
                list_code.append(d1[value])
        for value in d2:
            if value_encoded[i] == value:
                list_code.append(d2[value])
        for value in d3:
            if value_encoded[i] == value:
                list_code.append(d3[value])
        for value in d4:
            if value_encoded[i] == value:
                list_code.append(d4[value])
        for value in d5:
            if value_encoded[i] == value:
                list_code.append(d5[value])

    #print(list_code)
    return list_code



'''
word = "абвгд^*"
value_encoded = encode_val(word)
encript1 = encript(value_encoded)

#encript = "tрнянцюцюлдкядкzMhjtмэяог"
value_encoded = encode_val(encript1)
encript1 = encript(value_encoded)
'''


'''
def listToString(s):  
    # initialize an empty string 
    str1 = ""  
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    # return string   
    return str1  
s = ['t', 'р', 'н', 'я', 'н', 'ц', 'ю', 'ц', 'ю', 'л', 'д', 'к', 'я', 'д', 'к', 'z', 'M', 'h', 'j', 't', 'м', 'э', 'я', 'о', 'г']
print(listToString(s))          
'''      
'''
    for w in range(lent):
        for value in d1:
            if word[w] == d1[value]:
               list_code.append(value)
        for value in d2:
            if word[w] == d2[value]:
               list_code.append(value)    
        for value in d3:
            if word[w] == d3[value]:
               list_code.append(value)
        for value in d4:
            if word[w] == d4[value]:
               list_code.append(value)
'''
'''
N = 84
Nt = ((((N-1) // 3) // 3) // 6) % 12+1
Nc = (((N-1) // 3) // 3) % 6+1
Nm = ((N-1) // 3) % 3+1
Nu = (N-1) % 3+1

print('Nt', Nt)
print('Nc', Nc)
print('Nm', Nm)
print('Nu', Nu)

word = "hell1252fasd1865!#$@#&^#%$o%_world"
word2 = list(word)

print(word2)
k = len(word)
print(k)
key = 4
cher = [""] * k
index = k-1
n = (k - 1) // key + 1

for i in range(k):
    ind = key * (i % n) + (i // n)
    cher[i] = ind 


    

print(cher)
print(len(cher))
'''
