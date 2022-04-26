#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Игра в города

def end( d ) :
    f = open( 'text.txt', 'w' )
    for index in d :
        f.write(index + '\n')
    f.close()
    
def star( m ) :  
    print( m ) 
    unit = str( input( ': ' ) )
    if( unit == 'stop' ) :
        print( end( d ) )
    else :
        print( town( d, Lost, unit ) )

f = open( 'text.txt', 'r' ) # открываем файл
C = []                                             # список известных городов
x = 0
g = 0
while not( x == '' ) :                             
    x = f.read()
    y = list( x )
    if( g == 0 ) :
        C = y
    else :
        C = C + y
    g = g + 1
a = 0
i1 = 0
g = []
for k in range( 0,len(C) ) :
    if( C[k] == '\n' ) :
        a = a + 1
        if( a % 2 == 0 ) :
            i1 = k
            y = C[i2:i1]
            if( y[0] == '\n' ) :
                del y[0]
            g.append( y )
        else :
            i2 = k
            y = C[i1:i2]
            if( y[0] == '\n' ) :
                del y[0]
            g.append( y )
if( i2 > i1 ) :
    y = C[i2:] 
else :
    y = C[i1:]
if( y[0] == '\n' ) :
    del y[0]
g.append( y )
f1 = ''
d = [] 
for k in range( 0,len(g) ) :
    h = g[k]
    for i in range( 0,len(h) ) :
        f1 = f1 + h[i]
    d.append( f1 )
    f1 = ''
Lost = [] # список "использованных" городов
f.close()
 
def town( d, Lost, unit ) :
    elem = unit[-1]
    if( elem == 'ь' or elem == 'ъ' ) :
        elem = unit[-2:-1]
    if not( d.count(unit) == 0 ) : # если этого города программа не знает то она его добавляет в список
        d.append(unit)
        print( unit )        
    for k in range( 0,len(d) ) :
        s = d[k]
        if( s[0] == elem ) :
            m = d[k]
            if( Lost.count(m) == 0 ) :
                if( Lost.count(unit) == 0 ) :
                    Lost.append( unit )
                else :
                    print( 'этот город уже был' )
                Lost.append( m )
                print( Lost )
                print( star( m ) )
                            
    print( end( d ) )
    return 'Вы выиграли!' # программа напечатает это только в том случае, если не найдёт города на нужную букву
m = ''
print( star( m ) )

    
    
    
    
    
    
    
    
    
    
    
    