#!/usr/bin/python3
# -*- coding: utf-8 -*-

# в файле имеется некоторое количество чисел, необходимо сгенерировать Nзначное число,
# отсутствующее в файле, потом это число записывается в файл и игра продолжается

# TODO: подправить алгоритм выбора случайного числа, нужно чтобы следующее
# сгенерированное число было непохоже на предыдущее. Так же нужно позволить юзеру самому вводить
# данные( количество цифр в числе ).

#TODO: когда все числа в заданном диапазоне сгенерированы программа должна вывести сообщение
#(когда остаётся последнее число в заданном диапазоне прога не хочет его генерировать и выдает ошибку)

def rand_dop(min=0,max=9) : # функция для генерации цифр в заданном диапазоне
    import time
    s = ''
    global srez
    while True :
        t = time.time()
        time.sleep(0.01)
        t = str(t)
        f = t.find('.')
        if( len(t[f+1:len(t)]) == 6 ) : # если количество цифр после точки = 6 то в конце стоял не 0
            srez = t[-1]
        else :                        # если же количество цифр = 5 то в конце стоял 0
            srez = 0
        srez = int(srez)
        if(min<=srez<=max) : # если srez принадлежит данному диапазону
            break
    return ''

f = open('text_1.txt','r+')
F = f.read()
L = []
Result = []
res = ''
i = 0

vvod = int(input('Введите длину чисел, которые будут генерироваться: '))

for k in F :
    if not k == ' ' :
        res = res + k
    else :
        L.append(res)
        res = ''       
        
V = []
for k in L :            # создаём список чисел заданной длины сгенерированных которые уже есть в файле
    if len(k) == vvod :
        g = int(k)
        V.append(g)
print(V)

if vvod == 1 :            # start - начальныйй диапазон генерируемых чисел
    start = 0               
else :
    start = 10**(vvod-1) 
        
for k in range(start,10**vvod) : # 10**vvod - конечный диапазон генерируемых чисел 
    if not k in V :
        Result.append(k)
        
le = len(Result)
le1 = str(le)
d = le1[0]
d = int(d)
print(rand_dop(max=d)) # генерируем первую цифру числа
end = str(srez) # здесь из цифр будет собираться число

def recars(le,le1,i) : # рекурсивная функция для генерации цифр из которых составляется число
    global srez,end
    end = end + str(srez)
    le_end = len(end)
    
    if str(srez) == le1[i] :
        del_1 = int(le[0:le_end])
        del_2 = int(end)
        if del_1 == del_2 :
            print(rand_dop(max=int(le[i+1])))
        elif del_1 > del_2 :    
            print(rand_dop())
    else :
        print(rand_dop())
        
    
if le == i+1 :    
    print(recars(le,le1,i))
    i = i + 1
    
while len(end) > 1 :
    if end[0] == '0' :
        del end[0] 
    else :
        break
        
end = int(end)
res = Result[end]           
f.write(str(res) + ' ')
f.close()

print(res)     

                