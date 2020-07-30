import re
from math import ceil,sqrt

alf1 = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
alf2 = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
alf3 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alf4 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def check_text(text):
    clear_text = text_del_symb(text)
    if clear_text == '': return False
    if clear_text[0].lower() in alf1:
        alf = add_alf_symb(alf1)
        for ch in text:
            if ch.lower() not in alf: return False
        return True
    elif clear_text[0].lower() in alf3:
        alf = add_alf_symb(alf3)
        for ch in text:
            if ch.lower() not in alf: return False
        return True
    return False

def check_key(key):
    if sqrt(len(key)).is_integer(): return True,int(sqrt(len(key)))
    return False,0

def text_del_symb(text):
    res = ''.join(re.findall('[A-Za-zА-Яа-я]', text))
    if res == None: 
    	return ''
    return res

def add_alf_symb(alf):
    new_alf = alf.copy()
    if 'д' in alf: new_alf.extend(['.',',','?',' '])
    elif 'd' in alf: new_alf.extend(['.',',',' '])
    return new_alf

def text_in_matrix(text,alf,count_stlb):
    count_str = ceil(len(text)/count_stlb)
    if len(text)!= count_stlb*count_str:text = text.ljust(count_str*count_stlb,' ')
    text = list(text)
    result = [[0 for i in range(count_stlb)] for j in range(count_str)]

    for i in range(count_str):
        for j in range(count_stlb):
            result[i][j]=alf.index(text.pop(0).lower())

    return result

def matrix_in_text(matrix,alf):
    result = ''
    for str in matrix:
        for num in str:
            result+= alf[num]

    return result.rstrip()

def mul_str_matr(str,matrix):
    result = []

    for i in range(len(matrix[0])):
        mul = 0
        for j in range(len(str)):
            mul += str[j]*matrix[j][i]
        result.append(mul)

    return result

def mod_matr(matrix, num):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < 0 :  matrix[i][j] = matrix[i][j]%num -num
            else: matrix[i][j] = matrix[i][j]%num


    return matrix

def det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def minor(matrix, i, j):
    tmp = [row for k, row in enumerate(matrix) if k != i]
    tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
    return tmp

def determ(matrix):
    size = len(matrix)
    if size == 2:return det2(matrix)
    return sum((-1) ** j * matrix[0][j] * determ(minor(matrix, 0, j))
               for j in range(size))

def egcd(a, b):
    x,y,u,v = 0,1,1,0

    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b

    return gcd, x, y

def transp_matrix(matrix):
    result = list(zip(*matrix))
    for i in range(len(result)):
        result[i] = list(result[i])
    return result

def invers_det_mod(det,x,mod):
    if det <0 and x>0: return x
    elif det>0 and x<0: return mod+x
    elif det>0 and x>0: return x
    elif det<0 and x<0: return -x

def matrix_minor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def invers_matrix_mod(matrix,inv_det,mod):
    alg_dop = []
    if len(matrix) == 2:
        alg_dop = [[matrix[1][1], -1*matrix[0][1]], [-1*matrix[1][0], matrix[0][0]]]
    else:
        for i in range(len(matrix)):
            alg_dop_row = []
            for j in range(len(matrix)):
                minor = matrix_minor(matrix,i,j)
                alg_dop_row.append(((-1)**(i+j)) * determ(minor))
            alg_dop.append(alg_dop_row)

    alg_dop = mod_matr(alg_dop, mod)

    for i in range(len(alg_dop)):
        for j in range(len(alg_dop)):
            alg_dop[i][j] = alg_dop[i][j]*inv_det

    alg_dop = mod_matr(alg_dop,mod)
    alg_dop = transp_matrix(alg_dop)

    for i in range(len(alg_dop)):
        for j in range(len(alg_dop[i])):
            if alg_dop[i][j] < 0:alg_dop[i][j] = alg_dop[i][j]+mod

    return alg_dop

def dec(text,key):

    if text_del_symb(text)[0].lower() in alf1: alf = add_alf_symb(alf1)
    else: alf = add_alf_symb(alf3)
    n = check_key(key)[1]

    matrix_text = text_in_matrix(text,alf,n)
    matrix_key = text_in_matrix(key,alf,n)

    det = determ(matrix_key)
    if det == 0: return 'Ключ не валиден'
    x = egcd(det,len(alf))[1]
    inv_det = invers_det_mod(det,x,len(alf))
    if inv_det == None: return 'Ключ не валиден'
    inv_matrix_key = invers_matrix_mod(matrix_key,inv_det,len(alf))

    matrix_mul = []

    for str in matrix_text:matrix_mul.append(mul_str_matr(str,inv_matrix_key))

    matrix_mul= mod_matr(matrix_mul,len(alf))

    result = list(matrix_in_text(matrix_mul,alf))
    for i in range(len(result)):
        if text[i].isupper(): result[i] = result[i].upper()

    return ''.join(result)


def enc(text,key):
    result = []
    matrix_mul = []

    if text_del_symb(text)[0].lower() in alf1: alf = add_alf_symb(alf1)
    else: alf = add_alf_symb(alf3)
    n = check_key(key)[1]

    matrix_text = text_in_matrix(text,alf,n)

    matrix_key = text_in_matrix(key,alf,n)

    for str in matrix_text:matrix_mul.append(mul_str_matr(str,matrix_key))

    matrix_mul= mod_matr(matrix_mul,len(alf))

    for i in range(len(matrix_mul)):
        for j in range(len(matrix_mul[0])):
            matrix_mul[i][j]=alf[matrix_mul[i][j]]

    for str in matrix_mul:
        for i in range(len(str)):
            result.append(str[i])

    for i in range(len(text)):
        if text[i].islower(): result[i] = result[i].lower()
        else: result[i] = result[i].upper()

    encText = ''.join(result)

    decText = dec(encText,key)

    if decText != text: return 'Ключ не валиден.'
    return encText


