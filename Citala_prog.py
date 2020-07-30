import math

def Scitala_encrypt(text, n):
	n = int(n)
	ciphertext =''
	for i in range(n):
		for j in range(i,len(text), n):
			ciphertext += text[j]
	return ciphertext


def Scitala_decrypt(ciphertext, n):
	n = int(n)
	k = 0
	text = [''] * len(ciphertext)
	for i in range(n):
		for j in range(i, len(ciphertext), n):
			text[j] = ciphertext[k]
			k += 1
	text = ''.join(text)
	return text
