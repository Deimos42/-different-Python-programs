import numpy
import itertools
import time
import pickle

aphav = "Абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
st = input("Введите строку: ").lower()
words = st.split()
#print(words)

# составление всех комбинаций и запись их в файлы
def func(st): 
    i = 0
    f = open('combination.dat','wb')
    file = open('combination.txt','w')

    Result = []
    for L in range(0,len(st)+1):
        for subset in itertools.permutations(st,L):
            i += 1
            res = ''
            for k in subset:
                res += k
            if res != '' and res != ' ':
                Result.append(res)

            # записываем ф файл каждые 10 000 комбинаций во избежания переполнения памяти
            if i % 10000 == 0:
                pickle.dump(Result,f)
                file.write(str(Result))
                Result = []
                #print(i)

    # дозапись в файлы всех комбинаций букв введённой строки
    pickle.dump(Result,f)
    file.write(str(Result))
    file.close()
  
    return (Result,i-1) # последние < 10 000 комбинаций

def func2():
    # считывание из файла списка слов из словаря
    Slovar = []
    file2 = open('words.txt','r')
    st2 = file2.read()
    Slovar = st2.split()
    print(Slovar)
    file2.close()


    fi = open('combination.txt')
    def read1k():
        return fi.read(2048)

    for piece in iter(read1k, ''):
        print(piece)

t1 = time.time()
Spis = func(st)
t2 = time.time()
print('...',Spis[0][0:100],'...')
t3 = time.time()
print()
print('мощность алфавита: ',len(st))
print('число вариантов: ',Spis[1])
print('время составления и записи всех комбинаций: ',t2-t1)
print('время вывода в консоль: ',t3-t2)

