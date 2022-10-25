#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:24:47 2022

@author: i02samoj
"""
import math

def area_cuadrado(lado):
    area = lado*lado
    return area

def area_perimetro(lado):
    area = lado*lado
    perimetro = lado*4
    return area, perimetro

def area_petrimetro_rec(a, b):
    area = a * b
    perimetro = a*2 + b*2
    return [area, perimetro]

def intercambia_valores():
    '''
    Función que lea de teclados dos números (A y B) e intercambie sus valores.
    '''
    a = int(input('Introduce a:'))
    b = int(input('Introduce b:'))
    print(f'a: {a}, b: {b}')
    aux = a
    a = b
    b = aux
    print(f'a: {a}, b: {b}')


if (__name__ == '__main__'):
    print('Práctica 1:')
    n = int(input('Introduce un número de ejercicio:'))
    
    if (n == 1):
        x = 1.1 
        area = area_cuadrado(x)
        print(f'El área de lado {x} vale {area:.3f})')
        [area, perimetro] = area_perimetro(x)
        print(f'El lado {x}: área es {area:.3f} y perímetro {perimetro}')
    
    elif (n == 2):
        a = 1
        b = 5
        [area, perimetro] = area_petrimetro_rec(a,b)
        print(f'El área es {area:.3f} y perímetro {perimetro}')
    
    elif (n == 7):
        # Aquí se llama a la función del ej3
        intercambia_valores()
        
    else:
        print('Número de ejercicio no válido')
        