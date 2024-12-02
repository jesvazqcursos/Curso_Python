# Video 7 listas

# Son estructuras de datos que nos permiten almacenar gran cantidad de valores
# Pueden guardar diferente tipo de valores
# se pueden explandir dinámicamente añadiendo nuevos elementos

miLista=["Luis","Arturo","Felipe","Roberto"]
print(miLista[:])

# para escribir un elemento concreto. el primer elemento es el valor 0. si ponemos 
# valor negativo se cuenta en sentido contrario pero parte desde -1

print(miLista[1])

#se puede acceder a una PORCION DE LISTA    se pone un rango de lista se informa el primer
#  indice (inclusive) y el último (exclusive). si no se informa el primero se considera 0.
# si no se informa del segndo va hasta el final

print(miLista[2:4])
 
# para añadir a la lista

miLista.append("Pedro")
print(miLista[:])

# si queremos que entre en un lugar concreto.

miLista.insert(2,"Fabian")
print(miLista[:])