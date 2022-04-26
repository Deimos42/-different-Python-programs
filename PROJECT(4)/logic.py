#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import main
import copy

def logic() :
    os.system('cls')
    print( 'С помощью этой программы вы можете решить квадратное уравнение, найти строку в файле и многое другое. ' )
    print( 'Справку по всем доступным функциям вы найдёте, если введёте в программу "справка" ' )
    
    L = { 'text': main.text, 'текст': main.text, 'word': main.word, 'слово': main.word,
    'chet': main.chet, 'счёт': main.chet, 'chislo': main.chislo_static, 'число': main.chislo_static,    
    'static': main.word_static, 'статистика': main.word_static, 'find': main.find_word, 
    'поиск': main.find_word } 
    
    star = input( ': ' )
    Result = []
    print( main.word_change(star,Result) )
    print( Result )
    for k in Result :
        if( k in L ) :
            break
    else :                       # перехватить исключением
        print( 'Такой функции нет' )
        return
    i = L[k]         # доступ к значению словаря 
    print( i() ) # вызов функции из main   
 
 
print( logic() )