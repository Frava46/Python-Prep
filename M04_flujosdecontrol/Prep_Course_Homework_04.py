#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

var = 0

if( var > 0):
    print("El numero es mayor que 0")
elif(var < 0):
    print("El numero es negativo")
else:
    print("El numero es igual a 0")


# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

var1 = 5
var2 = "hola"

if(type(var1) == type(var2)):
    print("Las variabloes son del mismo tipo de dato")
else: print("Las variables son de tipos de datos distintos")

# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

for i in range(1, 21):
    if i % 2 == 0:
        print(f"El numero, {i} es par")
    else: print(f"El numero, {i} es impar")



# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:
for i in range(1, 6):
    print(f"El numero {i} elevado a la 3 es igual a {i** 3}")




# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:

ent = 5
for i in range(ent):
    print("---..")



# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:
num = 70

if(type(num) == int):
    
    if(num > 0):
        i = num
        while(i >= 1):
            if(num % i == 0):
                print(f"El numero {i} es factor de {num}")
            i -= 1    
            
    else:print("El numero no es superior a 0")
else: print("El numero no es un entero")

# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:
num = 10
while (num != 0):
    for i in range(1):
        print("Reste 1 a ",num)
        num -= 1



# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:
for i in range(1, 6):
    print("soy el for")
    while(True):
        print("yo soy el while")
        break




# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

tope_rango=30
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:

n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1


# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:
ciclos_sin_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_sin_break += 1
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_sin_break))
# //
ciclos_con_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_con_break += 1
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_con_break))
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')


# In[57]:




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:

min = 99
while (min < 300):
    if(min % 12 == 0):
        print(f"{min} es divisible por 12")
    min+=1




# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:

nombre = input("Cual es su nombre?")
print(f"Hola señor {nombre}")

# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:
n = 100
while(n<=300):
    if (n % 6 == 0):
        print('El número es: ', str(n))
        break
    n += 1



# %%
