#Las variables son datos que se almacenan en la memoria y cambian su valor
#las variables se declaran y se definen
# la variable "a" es igual a "5" por ejemplo, y pueden redefinirse despues

a = 5
b = 3
nombre = "moises"

#Las mostramos en consola
print(nombre)
print(a)
print(b)
print(a+b)

#Cancatenado de valores
#el concatenar es unir valores sin importar su tipo
#se puede concatenar con el uso de "+" 
bienvenida = "hola " + nombre + " como estas?" 
print(bienvenida)

#sin embargo el "+"" da problemas con el uso de multiples datos numericos
#para ello usaremos "f string" usando llaves, "{}"
#Es importante usar la "f" en la linea para que funcione
#"f" convirte todo tipo de dato en un string
bienvenida_dos = f"hola {nombre} como estas?"
print(bienvenida_dos)




