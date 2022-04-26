#!/usr/bin/python3
# -*- coding: utf-8 -*-

# в файле имеется некоторое количество чисел, необходимо сгенерировать двухзначное число,
# отсутствующее в файле, потом это число записывается в файл и игра продолжается

# программа работает с количеством чисел не более 100

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

f = open('I:\\WORK\\MY_PROGRAMS\\russian\\text_1.txt','r+')
F = f.read()
L = []
Result = []
res = ''

for k in F :
    if not k == ' ' :
        res = res + k
    else :
        L.append(res)
        res = ''       
        
V = []
for k in L :
    if len(k) == 2 :
        g = int(k)
        V.append(g)
print(V)        
for k in range(10,100) :
    if not k in V :
        Result.append(k)
le = len(Result)
#del_1 = le // 10
#del_2 = le % 10
le1 = str(le)
d = le1[0]
d = int(d)
print(rand_dop(max=d))
end = str(srez)
if str(srez) == le1[0] :
    print(rand_dop(max=int(le1[-1])))
else :
    print(rand_dop())
end = end + str(srez)
end = int(end)
res = Result[end]           
f.write(str(res) + ' ')
f.close()

print(res)     

                