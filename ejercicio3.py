#Randal Geovanny Ayales Salgado
#07/14/2022

#Ejercicio 3

#se solicita al usuario la palabra y se crea el arreglo
word=input("Ingrese la palabra que desea imprimir alrevés: ")
wor=[]
#se recorre el arreglo y se va agreando cada letra en cada espacio
for x in word:
    wor.append(x)
#se imprime la palabra escrita al revés
print("La palabra que usted escribió, escrita al revés es: ",list(reversed(wor)))