# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I9h4T0HQ3qE83MJiELKH5YfOKKhrpZ0C

# Probabilidad y Estadística
## Facilitador: José Gabriel Rodríguez Rivas
## Alumna: Lluvia A. Saenz S.
"""

from statistics import *

# lista de calificaciones del grupo
grupoa =[70,65,90,80,73,20,100,96]
print(grupoa)

# tipo de variable
type(grupoa)

# sacar media
promedio = sum(grupoa)/len(grupoa)
print(promedio)

promedio2 = mean(grupoa)
print(promedio2)

# determinar la mediana
mediana =median(grupoa)
print(mediana)

tiempo100=[15.10,17.20,14.69,13.27,22.15,18.71,19.15,20.65,15.10,17.20]

print("el tiempo promedio es", mean(tiempo100) )

print("la media es", median(tiempo100))

print("la moda es", mode(tiempo100))

print("la multimoda es", multimode(tiempo100))