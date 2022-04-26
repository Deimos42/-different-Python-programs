#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

class altern ( object ) :
    
    def __init__( self, main ) :
        self.__Main = main
    
    def alt( self, method ) :
        self.__Alt = method
        return self
      
    def __get__( self, instance, owner ) :
        self.__Instance = instance
        self.__Owner = owner
        return self
     
    def __call__ ( self, other ) :
        if isinstance( other, self.__Owner ) :
            return self.__Main( self.__Instance, other )
        else :
            return self.__Alt( self.__Instance, float(other) )

class quat( object ) :
    
    def __init__( self, x, y, z, a=0.0 ) :
        self.__Data = ( float(a), float(x), float(y), float(z) )

    _data = property( lambda self : self.__Data )        
    
    def __abs__( self ) :
        ( a, x, y, z ) = self.__Data
        return math.sqrt( a*a + x*x + y*y + z*z )
    
    @property    
    def conj( self ) :
        ( a, x, y, z ) = self.__Data
        return quat( -x, -y, -z, a )
    
    @property
    def abs2( self ) :
        ( a, x, y, z ) = self.__Data
        return  a*a + x*x + y*y + z*z 
    
    @property
    def inv( self ) :
        return self.conj / self.abs2
    
    @altern    
    def __add__( self, other ) :
        ( a1, x1, y1, z1 ) = self.__Data
        return quat( x=x1+x2, y=y1+y2, z=z1+z2, a=a1+a2 )
     
    @__add__.alt
    def __add__( self, other ) :
        ( a, x, y, z ) = self.__Data
        return quat( x, y, z, a+other )
        
    def __radd__( self, other ) : # функция складывающая число с кватернионом
        return self + other
    
    @altern    
    def __mul__( self, other ) :
        a1, x1, y1, z1 = self.__Data
        a2, x2, y2, z2 = other.__Data
        a = a1*a2 - x1*x2 - y1*y2 - z1*z2
        x = a1*x2 + x1*a2 + y1*z2 + z1*y2
        y = a1*y2 + y1*a2 - x1*y2 + z1*x2
        z = a1*z2 + z1*a2 + x1*y2 - y1*x2
        return quat( x, y, z, a )
    
    @__mul__.alt    
    def __mul__( self, other ) :
        a, x, y, z = self.__Data
        return quat( other*x, other*y, other*z, other*a )
        
    def __rmul__( self, other ) :
        return self * other
        
    def __truediv__( self, other ) :
        a, x, y, z = self.__Data 
        f = float(other)
        return quat( x/f, y/f, z/f, a/f )       

    def __str__( self ) :
        if self.__Data[0] == 0.0 :
            return 'quat( {1}, {2}, {3} )'.format( *self.__Data )
        return 'quat( {1}, {2}, {3}, a={0} )'.format( *self.__Data )

    def __format__( self, spec ) :
        return '<{1},{2},{3}>'.format( *self.__Data )    

def rotate( axe, angle ) :  # angle - это угол
    sa = math.sin( angle / 2.0 )
    ca = math.cos( angle / 2.0 )
    a, x, y, z = axe._data
    return quat( x, y, z ) * sa + ca 

        
P = quat( 1, 2, 3 )
Q = quat( 4, 5, 6 )

Z = quat( 0, 0, 1 )
Rt = rotate( Z, math.pi / 2.0 )
print('Rt: ',Rt)
X = Rt * P * Rt.inv

Y = P + 10.0

print('P: ',P )
print('Q: ',Q )
print('Z: ',Z )
print('X: ',X )
print('Y: ',Y )




