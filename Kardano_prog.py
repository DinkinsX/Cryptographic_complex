class Kardano:
    def __init__(self, word, key, SIZE):
        self.word = word
        self.key = key
        self.SIZE = SIZE

        '''СОЗДАНИЕ МАТРИЦЫ ИЗ КЛЮЧА'''
        self.Matrix_Key = []
        k = 0 # просто начальное значение, может быть любым
        for r in range(self.SIZE): # 5 строк
            self.Matrix_Key.append([]) # создаем пустую строку
            for c in range(self.SIZE): # в каждой строке - 5 элементов
                self.Matrix_Key[r].append(self.key[k]) # добавляем очередной элемент в строку
                k += 1 # увеличиваем значение счетчика
         
        print('Матрица в строку: ', self.Matrix_Key,'\n')
        for r in self.Matrix_Key:
            print(r)

        '''СОЗДАНИЕ МАТРИЦЫ ИЗ СЛОВА'''
        self.Matrix_Word = []
        s = 0
        for i in range(self.SIZE):
            self.Matrix_Word.append([])
            for c in range(self.SIZE):
                self.Matrix_Word[i].append(self.word[s])
                s += 1
        print('\n')
        print('Матрица в строку: ', self.Matrix_Word, '\n')
        for r in self.Matrix_Word:
            print(r)
        print('\n')


    def Matrix(self):
        Matrix = self.Matrix_Word
        return Matrix

    def Mass_0(self, word, key):     #исходдное положение
        self.Mass_0 = []
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if int(self.Matrix_Key[i][j]) == 1:
                    self.Mass_0.append(self.Matrix_Word[i][j])
                else:
                    self.Mass_0.append('-')
        #print(self.Mass_0)

        self.Matrix_0 = []
        k = 0 # просто начальное значение, может быть любым
        for r in range(self.SIZE): # size строк
            self.Matrix_0.append([]) # создаем пустую строку
            for c in range(self.SIZE): # в каждой строке - size элементов
                self.Matrix_0[r].append(self.Mass_0[k]) # добавляем очередной элемент в строку
                k += 1 # увеличиваем значение счетчика

        print('Матрица 0 в строку: ', self.Matrix_0, '\n')
        for r in self.Matrix_0:
            print(r)

        return self.Matrix_0

    def Mass_90(self, word, key):       #поворот на 90г
        self.Mass_90 = []
        for i in range(self.SIZE):
            for j in  range(self.SIZE):
                if int(self.Matrix_Key[self.SIZE-j-1][i]) == 1:
                    self.Mass_90.append(self.Matrix_Word[i][j])
                else:
                    self.Mass_90.append('-')
        #print(self.Mass_90)

        print('\n')
        self.Matrix_90 = []
        k = 0 # просто начальное значение, может быть любым
        for r in range(self.SIZE): # size строк
            self.Matrix_90.append([]) # создаем пустую строку
            for c in range(self.SIZE): # в каждой строке - size элементов
                self.Matrix_90[r].append(self.Mass_90[k]) # добавляем очередной элемент в строку
                k += 1 # увеличиваем значение счетчика

        print('Матрица 90 в строку: ', self.Matrix_90, '\n')
        for r in self.Matrix_90:
            print(r)  
        return self.Matrix_90      

    def Mass_180(self, word, key):  #поворот на 180г
        self.Mass_180 = []
        for i in range(self.SIZE):
            for j in  range(self.SIZE):
                if int(self.Matrix_Key[self.SIZE-i-1][self.SIZE-j-1]) == 1:
                    self.Mass_180.append(self.Matrix_Word[i][j])
                else:
                    self.Mass_180.append('-')
        #print(self.Mass_180)

        print('\n')
        self.Matrix_180 = []
        k = 0 # просто начальное значение, может быть любым
        for r in range(self.SIZE): # # size строк
            self.Matrix_180.append([]) # создаем пустую строку
            for c in range(self.SIZE): # в каждой строке - size элементов
                self.Matrix_180[r].append(self.Mass_180[k]) # добавляем очередной элемент в строку
                k += 1 # увеличиваем значение счетчика

        print('Матрица 180 в строку: ', self.Matrix_180, '\n')
        for r in self.Matrix_180:
            print(r)
        return self.Matrix_180        

    def Mass_270(self, word, key):   #поворот на 270г
        self.Mass_270 = []
        for i in range(self.SIZE):
            for j in  range(self.SIZE):
                if int(self.Matrix_Key[j][self.SIZE-i-1]) == 1:
                    self.Mass_270.append(self.Matrix_Word[i][j])
                else:
                    self.Mass_270.append('-')
        #print(self.Mass_270)

        print('\n')
        self.Matrix_270 = []
        k = 0 # просто начальное значение, может быть любым
        for r in range(self.SIZE): # size строк
            self.Matrix_270.append([]) # создаем пустую строку
            for c in range(self.SIZE): # в каждой строке - size элементов
                self.Matrix_270[r].append(self.Mass_270[k]) # добавляем очередной элемент в строку
                k += 1 # увеличиваем значение счетчика

        print('Матрица 270 в строку: ', self.Matrix_270, '\n')
        for r in self.Matrix_270:
            print(r)
        return self.Matrix_270

'''
   cout << "180:" << endl;
   for (int i = 0; i < SIZE; i++)
      for (int j = 0; j < SIZE; j++)
         if (grid[SIZE-i-1][SIZE-j-1] == 1)
            cout << buf[i][j];
   cout << endl;

   cout << "270:" << endl;
   for (int i = 0; i < SIZE; i++)
      for (int j = 0; j < SIZE; j++)
         if (grid[j][SIZE-i-1] == 1)
            cout << buf[i][j];
   cout << endl;


'''
'''
keyOld = '1001 0101 0101 1111 0101'
wordOld = 'пвдр ыидв девт снег девт'
SIZE = 5
word = wordOld.replace(" ", "")
key = keyOld.replace(" ", "")  
print(key)
print(word)
f = Kardano(word, key, SIZE)
A = f.Mass_0(word, key)

B = f.Matrix()
print(B)
'''

'''S = []
for i in range(len(A)):
    for j in range(len(A[i])):
        S.append(A[i][j])
    S.append('\n')
    print(S)
'''


#S.pop(S[1])

'''for r in A:
    print((str(''.join(str(r)))))
'''

