#!/usr/bin/python3
# -*- coding: utf-8 -*-

# программа для поиска слов в тексте
def find_word( vved=[],vvod=[] ) : # значения по умолчанию
    import os  
    
    if( len(vved) == 0 ) : # если vved раньше не использовался( TODO: через вызов file() )
        print( 'Введите полный путь к файлу и его расширение. Вводить нужно таким образом - ' )
        print( 'D:\\\WORK\\\MY_PROGRAMS\\\pext.txt' )
        file = input( 'Введите путь к файлу: ' )
        f = open( file, 'r' )
        vved = input( 'Введите слово которое вы хотите найти: ' )
        vved = vved.lower()
        vvod = f.readlines()
    
    Result = [] # список слов в строке
    x = 0       # счётчик определяющий в какой строке было найдено слово
    l = 0       # счётчик определяющий количество слов vved в тексте
    Head = []   # список глав где найдены были слова vved
    Stri = []   # список строк в которых были найдены слова vved
    chapter = 0 # глава в тексте    
    
    for strict in vvod :
        x = x + 1
        strict = strict.lower()    # TODO: через вызов word_change
        strict = list( strict )
        add = ''
        znak = '!`~@"№#$;%:^&?*()-_=+{}][|\/,.?>< '
        strict.append('.')
        while( strict.count('\n') > 0 ) : # заменяем символы конца строки на пустые строки
            a = strict.index('\n')
            strict[a] = ''
        for k in strict :
            if not( k in znak ) : # если k это буква
                add = add + k
            else :
                Result.append(add)
                add = ''
        while( Result.count('') > 0 ) : # удаляем пустые строки
            Result.remove('')           
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
                скорре всего res - это число.( изменить когда буду писать защиту от дурака )
            '''
            res = int(res)
            res = res - 1
            if( res > -1 and res < l ) :        
                print( 'ГЛАВА', Head[res] )
                print( 'СТРОКА', Stri[res] )
            else :
                print( 'ОШИБКА! ТАКОЙ ПОЗИЦИИ НЕТ!' )
        else :  # если юзер ввёл слово - перезапускаем функцию
            vved = res
            vved = vved.lower()            
            print( find_word(vved,vvod) )
                     
print( find_word() )



    
    
    