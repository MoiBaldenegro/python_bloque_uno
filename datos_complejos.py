#los datos complejos son datos con otros datos simples
#equivalentes a arreglos
#listas

lista_de_frutas = ["limon", "sandia", "manzana", "melon"]
print(lista_de_frutas)

#llamamos a un elemento es especifico
print(lista_de_frutas[0])
print(lista_de_frutas[1])
print(lista_de_frutas[2])
print(lista_de_frutas[3])

#redefinimos el valor del indice 0 de la "lista_de_frutas"

lista_de_frutas[0] = "valor redefinido"
# a continuacion observamos que el valor ha sido redefinido
print(lista_de_frutas)


#tuplas a diferencia de los arrays usamos parentesis "()"
#las tuplas no pueden redefinir ningun valor

tupla_de_frutas =("limon", "sandia", "manzana", "melon")
print(tupla_de_frutas)
print(tupla_de_frutas[0])
print(tupla_de_frutas[1])
print(tupla_de_frutas[2])
print(tupla_de_frutas[3])

#tambien tenemos los conjuntos donde utilizamos las llaves "{}"
#los conjuntos podemos redefinirlos por completo pero no cada elemento en especifico como con las listas

conjunto_de_frutas = {"limon", "sandia", "manzana", "melon"}
print(conjunto_de_frutas)

#redefiniendo el conjunto por verduras

conjunto_de_frutas = "betabel", "ajo", "cebolla"
#reestructuramos el conjunto con solo 3 valores y ahora son verduras

print(conjunto_de_frutas)


