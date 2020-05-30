import numpy as np
from scipy import linalg
from fractions import Fraction
import random

matriz = [[1,2,3],[1,2,3],[1,2,3]]

print("Hecho por  LUIS ENRIQUE MEZA BAUTISTA ")
print("")
print("¿Que es la matriz inversa :")
print("")
print("     La matriz inversa de una matriz cuadrada es una matriz tal que el producto M * M-1 = I")
print("")

print("Ingrese 1 si quiere ingresar sus propias variables o 2 si quiere variables aleatorias")
print("")
variable = int(input("¿Eliges la opcion 1 o 2?: "))

if (variable==1):
    for i in range (3):
        for j in range (3):
            matriz[i][j]=int(input("Introduce la cantidad en la ubicacion (%d,%d): " %(i+1,j+1)))

else:
    for i in range (3):
        for j in range (3):
            matriz[i][j]=random.randint(1,100)



m=np.array(matriz)
print("Mostrando la matriz ingresada: ")
print(m)
print("")


try:
    i = linalg.inv(matriz)
    print("Mostrando la matriz inversa")
    print("")
    print(i)
    print("")
   

    
    I = m.dot(i)
    print("Comprobando los resultados")
    print("")
    print(I)
    print("")

    print("Si gusta comprobar la matriz multiplicandola, le dejo una pagina web muy buena")
    print("https://matrix.reshish.com/es/inverse.php")
except(np.linalg.LinAlgError):
    print("No tiene matriz inversa por que es singular")

print("")
print("")
final = input("        PRESIONA ENTER PARA CERRAR EL PROGRAMA              ")