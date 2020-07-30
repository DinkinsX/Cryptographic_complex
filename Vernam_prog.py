import math
import time
from itertools import cycle
class Vernam:
    def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
        bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]

        return bits.zfill(8 * ((len(bits) + 7) // 8))    

    def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
        n = int(bits, 2)

        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

    def xor(word, key):
        wordX = ''
        for a, b in zip(word, cycle(key)):
            wordX = wordX + str(int(a)^int(b))
        return wordX

    def lin_rand_arr_flxd(seed,size):
        #Реализация линейного конгруэнтного генератора псевдослучайных чисел. 
        #Возвращает массив заданного размера или случайное число, если указан единичный размер.
        m=32768
        a=23
        b=5421

        if size == 1:
            return math.ceil(math.fmod(a * math.ceil(seed) + b, m))

        r = [0 for i in range(size)]
        r[0] = math.ceil(seed)

        for i in range(1,size):
            r[i] = math.ceil(math.fmod((a * r[i - 1] + b), m))
        return r[1:size]



'''
word = 'ы'
key = Vernam.lin_rand_arr_flxd(time.time(), 10)
key2 = ''
for i in key:
    key2 = key2 + str(i)

print('ключ линейного конгруэнтного генератора', Vernam.text_to_bits(str(key)))
print('слово', Vernam.text_to_bits(word))
word = Vernam.text_to_bits(word)
key = Vernam.text_to_bits(key2)

kesa = Vernam.xor(word, key)
kesa2 = Vernam.xor(kesa, key)
print(kesa)
print(kesa2)


print(saka)
print(Vernam.text_from_bits(kesa2))
'''




    
