#Randal Geovanny Ayales Salgado
#07/14/2022

#Ejercicio 4

#se crea el arreglo y variables
x=0
cashUser=[]
sum=0
#se crea el for para recorrer el arreglo
for x in range(7):
    money= int(input(f"Digite la cantidad de dinero realizado en el {x+1} dia de la semana: "))
    #se agrega el dinero en los espacios correspondientes
    cashUser.append(money)
    #se crea una suma total de los valores para saber cuanto dinero recaudó
    suma=sum+cashUser[x]
    #se imprime el total recaudado
print("Su total de dinero en  recogido en la semana es de: ", sum)
#se averigua cuanto fue el valor minimo recaudado
minimum=min(cashUser)
#se imprime el dia que se recaudó menos dinero}
print("El dia que mas dinero recaudó fue el dia:",cashUser.index(minimum)+1)
