#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 10:20:14 2022

@author: javi
"""

import numpy as np
import matplotlib.pyplot as plt

# Tenemos un fichero con nombres, apellidos y nota
#rafa; perez; 4,5
#monica; sanchez; 8,9
#paula; sanchez; 7,6

def procesar_fichero(nombre): 
    ''' Función que lee un fichero separado por comas
    y mete cada campo en un diccionario. Devuelve una lista de diccionarios con uno por cada línea'''
    file = open(nombre, 'r')
    lista = list()
    for linea in file:
        #print(linea)
        # partir la cadena por el carácter ';'
        # en trocitos tendremos una lista con cada subcadena resultante
        trocitos = linea.split(';') 
        # creamos un diccionario vacío y añadimos campos
        # strip() limpia caracteres en blanco al inicio y final de la cadena
        d = dict()
        d['nombre'] = trocitos[0].strip()
        d['apellido'] = trocitos[1].strip()
        # La nota está expresada con , como separador decimal, lo reemplazamos por el . que es lo que espera python y la transformamos en float
        nota = trocitos[2].strip()
        nota = float(nota.replace(',','.'))
        d['nota'] = nota
        
        # Cada diccionario de datos lo metemos en la lista
        lista.append(d)
    
    file.close()
    return lista

def nota_media(lista):
    '''Recibe una lista de diccionarios que tienen un campo llamado "nota"'''
    media = 0
    for d in lista: 
        media = media + d['nota']
    media = media / len(lista)
    return media


def notas_a_vector(lista):
    '''Recibe una lista de diccionarios que tienen un campo llamado "nota"'''
    vector = np.zeros(len(lista))
    
    for i in range(len(lista)):
        vector[i] = lista[i]['nota']
        
    return vector

def diagrama_barras(ma,mb):
    plt.figure()
    plt.bar([0,1],[ma, mb])
    plt.legend(['Media clase'])
    plt.show()

lista_procesadaA = procesar_fichero('claseA.txt')
mediaA = nota_media(lista_procesadaA)
vectorA = notas_a_vector(lista_procesadaA)

lista_procesadaB = procesar_fichero('claseB.txt')
mediaB = nota_media(lista_procesadaB)
vectorB = notas_a_vector(lista_procesadaB)

print(f'media+-std clase A: {vectorA.mean()}+-{vectorA.std()}')
diagrama_barras(mediaA, mediaB)