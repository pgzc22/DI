from operaciones import *
op = 's'
while op=='s':
    print('Escribe dos números')
    a = int(input())
    b = int(input())
    print('¿Qué tipo de operación desea realizar?')
    print('1- Suma')
    print('2- Resta')
    print('3- Multiplicación')
    print('4- División')
    op = int(input())
    if op==1: print(suma(a,b))
    elif op==2: print(resta(a,b))
    elif op==3:print(multiplicacion(a,b))
    elif op==4:print(division(a,b))
    op = input ('¿Desea realizar otra operación? s/n ')
