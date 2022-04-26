#!/usr/bin/python3
# -*- coding: utf-8 -*-

#def spravka() : # справка по всем функциям
    #TODO - написать эту функцию
'''
Необходимо полностью переделать структуру программы( взаимодействие функций и модулей ). 
На первое время можно написать функцию stop
'''
import os
    
def file(vvod) :
    # TODO : избавиться от глобальной переменной и заменить её аргументом функции. это упростит код
    # и позволит вызывать эту функцию несколько раз подряд
    print( 'Введите полный путь к файлу и его расширение. вводить нужно таким образом - ' ) 
    print( 'I:\\\WORK\\\MY_PROGRAMS\\\pext.txt' )
    file = input( 'Введите путь к файлу: ' )
    if( file == 'стоп' or file == 'stop' ) :
        print( stop() )
    f = open( file, 'r' )    
    vvod = f.read() # f.readlines()    
    return ''

def word_change(vvod,Result) :
    vvod = vvod.lower() # переводит строку в нижний регистр
    vvod = list(vvod)
    add = ''            # здесь будут храниться отдельные слова
    znak = '!`~@"№#$;%:^&?*()-_=+{}][|\/,.?>< '
    vvod.append('.')    # чтобы программа работала в конце должен быть знак
    while( vvod.count('\n') > 0 ) : # заменяем символы конца строки на пустые строки
        a = vvod.index('\n')
        vvod[a] = ''
    for k in vvod :
        if not( k in znak ) : # если k это буква
            add = add + k
        else :
            Result.append(add)
            add = ''
    while( Result.count('') > 0 ) : # удаляем пустые строки
        Result.remove('')
    return ''   

# --------------------------------------------------------------------------------------------------------------

# программа для поиска слов в тексте( позже нужно будет присоединить её к проекту )
def find_word( vved=[],vvod=[] ) : # значения по умолчанию  
    
    if( len(vved) == 0 ) : # если vved раньше не использовался
        print( file(vvod) )        
        vved = input( 'Введите слово которое вы хотите найти: ' )
        vved = vved.lower()
    
    Result = [] # список слов в строке
    x = 0       # счётчик определяющий в какой строке было найдено слово
    l = 0       # счётчик определяющий количество слов vved в тексте
    Head = []   # список глав где найдены были слова vved
    Stri = []   # список строк в которых были найдены слова vved
    chapter = 0 # глава в тексте    
 
    for strict in vvod :
        x = x + 1
        print( word_change(strict,Result) )              
        if( Result == [] ) :  # КОСТЫЛЬ: специально добавляем в Result пустую строку чтобы не вылетела ошибка
            Result.append('')    
            
        if( Result[0] == 'глава' ) :
            chapter = Result[1]
            x = 0  # обнуляем счётчик строк
        for g in Result :    
            if( g == vved ) : # если это то слово которое мы ищем
                l = l + 1                           
                os.system('cls')
                Head.append(chapter)
                Stri.append(x)            
        Result = []

    print( 'Найдено слов:', l )
    # TODO: если не найдено слов - перезапустить со строки 11( функция или цикл )
    n = 0     # счётчик показывающий количество найденных определенных слов в главе
    Chap = [] # список строк где найдены были слова из vved в указанной юзером главе
    zifr = '0123456789'
    
    while True :
        res = input( 'Введите команду: ' ) 
        res = res.lower()        
                
        if( res[0:5] == 'глава') :       
            res = res[5:]          
            res = int(res) # номер главы
            for k in range(0,len(Head)) : # находим нужную главу, изымаем индексы       
                if( int(Head[k]) == res ) : # получаем номера строк где есть слово из vved
                    n = n + 1
                    s = Stri[k]
                    Chap.append(s)                                                                                      
            print( 'Найдено слов:', n )            
            if( n == 0 ) :
                continue   # выполняется переход в начало цикла                
            res = input( 'Введите команду: ' ) 
            res = res.lower()          
            if( res == 'назад' ) : # возвращает юзера к выбору комманд( к циклу while true )
                n = 0
                Chap = []
                res = ''
                print( 'Найдено слов:', l )
                continue
            res = int(res)
            res = res - 1                       
            if( res > -1 and res < n ) :
                print( 'СТРОКА', Chap[res] )
            else :
                print( 'ОШИБКА! ТАКОЙ ПОЗИЦИИ НЕТ!' )
                      
        elif( res == 'назад' ) : 
            n = 0
            Chap = []
            res = ''
            print( 'Найдено слов:', l )
            continue
        
        elif( len(Chap) > 0 ) :  # если юзер работает сейчас с главой а не со всем текстом
            res = int(res)
            res = res - 1
            if( res > -1 and res < n ) : # в зависимости от того где работает юзер используем разные переменные
                print( 'СТРОКА', Stri[res] )
            else :
                print( 'ОШИБКА! ТАКОЙ ПОЗИЦИИ НЕТ!' )
        elif( len(Chap) == 0 ) and ( res[0] and res[-1] in zifr ) :
            ''' если первый и последний элемент введеного числа - цифры следовательно
                скорее всего res - это число.( изменить когда буду писать защиту от дурака )
            '''
            res = int(res)
            res = res - 1
            if( res > -1 and res < l ) :        
                print( 'ГЛАВА', Head[res] )
                print( 'СТРОКА', Stri[res] )
            else :
                print( 'ОШИБКА! ТАКОЙ ПОЗИЦИИ НЕТ!' )
        else :  # если юзер ввёл слово - перезапускаем функцию( TODO: написать защиту от дурака )
            vved = res
            vved = vved.lower()            
            print( find_word(vved,vvod) )
                        
def chet() :  # функция по подсчёту определённых букв в тексте
    i = 0
    print( 'Что вы хотите ввести - текст или путь к файлу?( введите "текст" или "путь" )' )
    text = input( ': ' )
    #global vvod
    vvod = []
    if( text == 'текст' ) :    
        vvod = str( input( 'Введите любой текст: ' ) )
    elif( text == 'путь' ) :
        print( file(vvod) )
    elif( text == 'стоп' or text == 'stop' ) :
        print( stop() )
    else : # если пользователь вводить абракадабру то функция выполняется заново
        return chet()
    print( vvod )
    vvod = vvod.lower() # теперь буквы "В" и "в" или "М" и "м" будут считаться одинаковыми
    bykv = str( input( 'Введите букву : ' ) )  
    for k in range( 0,len(vvod) ) :
        if( vvod[k] == bykv ) :
            i = i + 1    
    print( 'Количество букв', bykv, ' в тексте :', i )

def word() : # функция выводящая общее количество слов в тексте   
    print( 'Что вы хотите ввести - текст или путь к файлу?( введите "текст" или "путь" ) ' )
    vved = input( ': ' )
    vvod = ''    
    #global vvod
    if( vved == 'текст' ) : 
        vvod = str( input( 'Введите любой текст: ' ) )
    elif( vved == 'путь' ) :
        print( file(vvod) )
    elif( vved == 'стоп' or vved == 'stop' ) :
        print( stop() )
    else :
        return word() 
    Result = [] # список в который будут добавляться готовые слова
    print( word_change(vvod,Result) ) # вызываем функцию по обработке слов
    print( 'количество слов в тексте: ', len(Result) )
    return ''
    '''
    переменная vvod которая выводится в конце функции не была изменена, так как она не была объявлена
    глобальной в функции которая её изменяет( word_change() ) при попытке объявить её в той функции
    глобальной, возникает ошибка, так как одна переменная не может быть одновременно локальной и глобальной
    ( она есть в заголовке функции word_change() )     
    '''

def text() :
    '''
    TODO : сделать считывание текста не из списка, а из файла. Не надо запихивать всю книгу в список слов!!!
    буду считывать файл построчно и по достижении 10(15) строк выполнять над списком слов из этих строк все эти операции
    потом тоже самое но с другими строками и так до тех пор пока строки не кончатся. 
    '''
    vvod = []
    print( file(vvod) )
    #global vvod
    vved = input( 'Введите словосочетание или предложение которое нужно найти: ' )
    if( vved == 'стоп' or vved == 'stop' ) :
        print( stop() )
    Result_vved = [] # список в который будут добавляться слова из vved
    Result_vvod = [] # список в который будут добавляться слова из vvod
    print( word_change(vved,Result_vved) )       
    print( word_change(vvod,Result_vvod) )    
    for k in range( 0,len(Result_vvod) ) :
        if( Result_vvod[k] == Result_vved[0] ) :
            le = k + len(Result_vved)
            if( Result_vvod[k:le] == Result_vved ) :
                print( 'Фраза найдена!'.upper() )
                print( '-' * 79 )
                print( 'Если вы хотите узнать в каком месте текста находится эта фраза вы можете ввести ', end = '' )
                print( 'команды "до" или "после" а потом указать количество слов которое нужно вывести. ', end = '' )
                print( 'т.е если вы введёте "до 20" то на экран выведутся 20 слов стоящих до найденного выражения' )
                end = str( input( 'Введите команду: ' ) )
                zifr = '0123456789'
                n = ''
                for i in range( 0,len(end) ) : # находим первую цифру в строке
                    if( end[i] in zifr ) :
                        n = end[i:] # цифра которую ввёл юзер
                        n = int(n)
                        break                        
                if( end[0:2] == 'до' ) : # сначала выводим текст, а потом фразу которую ввёл юзер
                    L = Result_vvod[k-n:k]
                    print( '' )
                    for k in L :
                        print( k, end = ' ' )
                    for k in Result_vved :
                        k = k.upper()
                        print( k, end = ' ' )    
                if( end[0:5] == 'после' ) : # сначала выводи фразу которую ввёл юзер, а потом текст
                    L = Result_vvod[le:le+n]
                    print( '' )
                    for k in Result_vved :
                        k = k.upper()
                        print( k, end = ' ' )
                    for k in L :
                        print( k, end = ' ' )                
                return ''
    print( 'Фраза не найдена!'.upper() ) # запустится если не обнаружит совпадений
    print( '-' * 79 )
    return( '' )

def chislo_static() :
    vvod = []
    print( file(vvod) )
    bykv = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz'
    add = 0
    #global vvod
    chislo = []
    vvod = vvod.lower()
    for k in bykv :
        for i in range(0,len(vvod)) :
            if( vvod[i] == k ) :
                add = add + 1
        chislo.append(add)
        add = 0
    chislo = list(chislo)
    bykv = list(bykv)
    while( chislo.count(0) > 0 ) :
        j = chislo.index(0)
        chislo.pop(j)
        bykv.pop(j)
    
    for k in range(0,len(bykv)) :
        print( bykv[k], '-', chislo[k] )
    return ''

def word_static() : # выводит 10 самых частопреминимых слов в тексте и их количество
    vvod = []    
    print( file(vvod) )
    #global vvod
    Result = []                     # список слов
    print( word_change(vvod,Result) )
    vved = set( Result )
    vved = list( vved ) # теперь здесь нет повторяющихся слов
    numbers = []
    add = 0
    for k in vved :
        for i in Result :
            if( k == i ) :
                add = add + 1
        numbers.append(add)
        add = 0
    y = 0
    v = -1
    while( y <= 9 ) : # находит 10 наибольших слов
        g = -1
        v = v + 1
        for k in range( 0,len(numbers)-v ) : # ограничиваем область видимости цикла 
            if( numbers[k] > g ) :
                g = numbers[k] # наибольшое число
                i = k          # индекс наибольшого числа
        del numbers[i]    # удаляем максимальное число с той позиции
        numbers.append(g) # и вставляем его в конец
        x = vved[i] # слово которое будет добавляться в конец
        del vved[i]
        vved.append(x)
        y = y + 1
    Result_numbers = numbers[-10:] # срез 10 последних элементов
    Result_vved = vved[-10:]
   
    for k in range(0,10) :
        print( Result_vved[k], '-', Result_numbers[k] )
    return ''
        
    
    
    
    

    
    
    
