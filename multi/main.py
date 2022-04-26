#!/usr/bin/python3
# -*- coding: utf-8 -*-

class multimethod( object ) :
    
    def __init__( self, default ) :
        self.__Default = default
        self.__Methods = []
        
    def interval( self, a, b ) :
        def add( function ) :
            self.__Methods.append( ( (a,b), function ) )
            return self
        return add
        
    def __get__( self, instance, owner ) :
        self.__Instance = instance 
        self.__Owner = owner
        return self
    
    def __call__( self, x ) :
        for ( (a,b), function ) in self.__Methods :
            if a <= x and x < b :
                return function( self.__Instance, x )
        return self.__Default( self.__Instance, x )
    
class MyFunc( object ) :
    
    def __init__( self, max ) :
        self.__Max = max
    
    @multimethod
    def __call__( self, x ) :
        return 0.0
  
    @__call__.interval(-1.0,0.0)
    def __call__( self, x ) :
        return self.__Max*x + self.__Max 

    @__call__.interval( 0.0, 1.0 )    
    def __call__( self, x ) :
        return - self.__Max*x + self.__Max    
    
F = MyFunc( max = 3.0 )
x = -1.5
while x < 1.5 :
    print( x, F(x) )
    x += 0.1
    