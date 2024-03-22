#1
list_vacia = [] 
#2 y 3
nombres = ["Edgar","Antonio","jhordy","carmen","Ruben","georgy","alberto"]
print("lista de estudiantes: ")
print(len(nombres))
print("lista vacia:")
print(len(list_vacia))
#4
print("lista de estudiantes En varios puntos: ")
print(f'{nombres[0]},\n{nombres[3]}, \n{nombres[6]}' )
#5
datos_personales = []
datos_personales.append("Junior")
datos_personales.append(30) # Edad
datos_personales.append(1.75)
datos_personales.append("Soltero")
datos_personales.append("Calle Lib")
#6
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
#7
it_companies.insert(4,"Castellana")
#8
elemento = "Castellana" 
if elemento in it_companies: 
    print("El elemento",elemento,"si existe en la lista.") 
else: 
    print("El elemento",elemento," no existe en la lista.")
#9
it_companies.sort()
print("lista Ordenada Ascendente: ")
print(it_companies)
#10
print("lista Ordenada Descendente: ")
it_companies.sort(reverse=True) 
print(it_companies)
#11
it_companies.pop(0)
print("Eliminar primer elemento: ")
print (it_companies)
#12
it_companies.clear()
print("Lista Vacia: ")
print(it_companies)