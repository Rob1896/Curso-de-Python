#Un bucle o ciclo en programación es la ejecución  continua de un determinado bloque de código mientras una condición asignada se cumple. 


# loop WHILE

# El bucle “while” en Python se utiliza para repetir un bloque de código mientras se cumpla una condición específica
# It is used to execute a block of statements repeatedly until a given condition is satisfied.
# When the condition becomes false, the lines of code after the loop will be continued to be executed.

# ejemplo usando +=
# += se suele usar como contador ya que suma el primer elemento mas el segundo y va a detener el while
#  ejemplo: 




a = 0 

while a < 5: # mientras "a" sea menor que 5 print "a"(en este caso 0)
    print(a) # este print se va a ejecutar e imprimir 0 hasta que A cambie su valor.
    a += 1 # esto va a sumarle 1 a "a" cada vez que se ejecute hasta llegar a 9 que es donde se detiene el while. sino hago esto el while no se detiene

print('espacio de ejemplo')

# ejemplo 2

contador = 1
limite = 7

while contador <= limite:
    print(contador)
    contador += 1 # condicion que va a detener el while 
    
print('espacio de ejemplo')   
 
 
  # ejemplo 3 
  # sin +=  es el mismo resultado


b = 0
while b < 5:
    print(b)
    b = b + 1
    
print('espacio de ejemplo')
# ejemplo 4

my_condition = 0
while my_condition < 20:
    print(my_condition)
    my_condition += 2

print('espacio de ejemplo')
# podemos "marcar" donde el while se deja de ejecutar usando else, ejemplo: 
# el else es opcional


j = 0

while j < 5:
    print(j)
    j += 1
else:
    print("aqui se detiene el while")
    
print('espacio de ejemplo')
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print("count")



# Break: We use break when we like to get out of or stop the loop.
# ejemplo:

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

# ejemplo2:
print('separador de ejemplo')

maggie = 0
while maggie < 7:
    print(maggie)
    maggie += 1 # esto va a contar hasta que maggie llegue a 7

print('aqui termina el while de maggie')

peggy = 0

while peggy < 10:
    print(peggy)
    peggy += 1
    if peggy == 5: # hasta aqui va a llegar el while de peggy y no hasta 10
        break
    
    
    

print('ejemplo')
# Bucle FOR
# el codigo se va a ejecutar una vez por cada elemento de la lista,tupla,set o diccionario
#

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5
    
    
estaciones = ['invierno','veraono','otono','primavera']
for tr in estaciones:
    print('probando')# si imprimo un 'str' se va a imrpimir 4 veces porque hay 4 items en la lista
    
fruits  = ('banano','melon','sandia','naranja')
for test in fruits:
    print(test) 


language = 'Python'
for letter in language:
    print(letter)


vegetales = ('lechuga','tomate','papas','cebolla')
for feria in vegetales:
    print(vegetales) # en este caso se imprime la lista 4 veces porque 4 son es la cantidad de items
    
    
supermarket = ['frijoles','aceite','arroz','leche','azucar']
for super in supermarket:
    print(super) # en este caso imprime la variable "super"
    
# en este ejemplo el bucle for hace que la variable se grabe por cada item dentro de la lista
# for se ejecuta grabando la variable "super" con cada uno de los elementos
# recordemos que son 5 elementos, el primer for graba frijoles en super, se vuelve a ejecutar y graba aceite en super y asi sucesivamente.
# los va imprimiendo segun el orden 

# ejemplo 2 con lista
utiles = ['lapiceros','cuadernos','lapiz','pinturas']
for escuela in utiles:
    print(escuela) # imprime cada elemento de la lista en lineas separadas
    

# ejemplo 3 con set

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company) # imprime cada elemento del set en lineas separadass
    
# ejemplo 4 con tuples 
construccion = ('arena','cemento','piedra','madera')
for materiales in construccion:
    print(materiales) # imrpime cada elemento de la tupla en lienas separadas

# ejemplo 5 con string

frase = 'Python es un lenguaje'
for letra in frase:
    print(letra)

# ejemplo 6 con diccionario

my_dic = {'name':'Roberto','surename':'Mercado','city':'grecia','state':'alajuela'}

for word in  my_dic:
    print(word) # esto solo imprime los keys del diccionario    


my_dic2 = {'name':'Roberto','surename':'Mercado','city':'grecia','state':'alajuela'}

for nombres in  my_dic2:
    print(nombres) #esto va a imprimir solo los keys
for nombres, informacion in my_dic2.items(): # esto va a hacer que se impriman los keys y sus items 
    print(nombres,informacion)




# For usando Break

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break # cuando llegue a 3 se termina el for 
    
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
   
   

# funcion range
#
for i in range(10):
    print(i) # imprime numeros del 0 al  10


for i in range(10,20):
    print(i) # imprime numeros del 10 al 20
    
lista2 = list(range(10,20)) #aqui creo la lista en ese rango del 10 al 20
print(lista2) # imprime lista del 10 al 20

lista3 = list(range(0,20,2)) # imprime lista del 0 al 20 y el 2 al final significa que va de 2 en 2
print(lista3) 


# usando else
#If we want to execute some message when the loop ends, we use else
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number) # este else sale cuando se termina el for, o sea en 10



# continue

for i in range(10):
    if i % 2 == 0:
        continue # salta los numeros que no son pares, no los va a tomar en cuenta
    print(i)


i= 0
while i < 5:
    i += 1
    if i % 2 == 0:
        continue # salta los numeros que no son pares, no los va a tomar en cuenta
    print(i)



cadena3 = 'mamammmmsdadsmamasda'
count = 0
for i in cadena3:
    if i != 'm': # si es diferente a M que pase a la siguiente letra,cadd vez que i encuentre a M se ejecuta el Else
        continue 
    else: # si el IF NO SE CUMPLE que sume 1 al contador, o sea cada que i encuente a M.
        count = count + 1 # basicamente no esta buscando M en la cadena sino que cuenta las veces que el IF no se cumplio

print('Total number of m is:', count) # muestra el resultado de las veces que IF no se cumplio y se cumplio el else sumandole 1 al count 


'''filtrar numeros positivos de una lista'''

numbers = [10, -5, 3, -1, 0, 6, -2, 8]

for num in numbers:
    if num <= 0:
        continue  # Saltar a la siguiente iteración si el número es negativo o cero
    print(f"Processing number: {num}")
    


'''evitar errores de conversion'''

data = ["123", "abc", "456", "def", "789"]

for item in data:
    try:
        number = int(item)
    except ValueError:
        continue  # Saltar a la siguiente iteración si hay un error de conversión
    print(f"Converted number: {number}")


'''saltar elementos repetidos de una lista'''

elements = [1, 2, 2, 3, 4, 4, 5]
seen = set()

for elem in elements:
    if elem in seen:
        continue  # Saltar a la siguiente iteración si el elemento ya ha sido visto
    seen.add(elem)
    print(f"Unique element: {elem}")  

'''procesar lienas que no estan vacias de archivo de texto'''

lines = [
    "First line",
    "",
    "Second line",
    "   ",
    "Third line"
]

for line in lines:
    if line.strip() == "":
        continue  # Saltar a la siguiente iteración si la línea está vacía
    print(f"Processing: {line}")
  

