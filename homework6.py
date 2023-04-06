# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# a1=int(input("Первый элемент"))
# d=int(input("Разность"))
# n=int(input("Количество элементов"))
# A=[]
# for i in range(n-1):
#     A.append(a1 + (n-1) * d)
#     n-=1
# print(A)
# Задача 32: Определить индексы элементов массива (списка), 
#значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше 
#заданного максимума)
from random import *

def create_array(n:int):
    for i in range(n):
        A.append(randint(0,10))
    return A

def modify_array(A,  a, b):
    for i in range(len(A)):
        if a < A[i] and A[i] < b: 
            print(i+1, end=",")

A=[]
n=int(input())
a=int(input())
b=int(input())
my_array=create_array(n)
print(my_array)
modify_array(A, a, b)