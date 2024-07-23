
'''yield se usa para ahorro de memoria
por cada yield que la funcion encuentra el ciclo se detiene y comienza de nuevo
al contrario de iterar con return que genera el resultado completo
a simple vista los resultados son los mismos 
la diferencia es que yield ejecuta uno a uno y return ejecuta todo usando toda la memoria '''    
        
 # ejemplo:

def generate_list(n):
    lista = []
    for i in range(n):
        lista.append(i)
    return lista

resultado = generate_list(5)
for i in resultado:
    print(i)



# usando yield

def generate_list(n):
    for i in range(n):
        yield i

resultado = generate_list(5)

for i in resultado:
    print(i)
 
 
 
 
 # generadores yield
        
def generate_gretings():
    yield 'hello'
    yield 'world'
    yield 'hola'
    
    
greetings = generate_gretings()

for greeting in greetings:
    print(greeting)
    


def generate_naturales(n):
    i = 0
    while i < n:
        yield i
        i += 1

for numero in generate_naturales(5):
    print(numero)
    
# diferencias entre bucle for y yield 

numbers = [i for i in range(6)]

for number in numbers:
    print(number)
else:
    print('The loop stops at', number)
    
# ejemplo con yield

def generate_numbers():
    for i in range(6):
        yield i

for tst in generate_numbers():
    print(tst)
    
    

# funcion que genere numeros pares

def even_numbers():
    for i in range(10):
        if i % 2 == 0:
            print(i)

even_numbers()


# funcion que genere numeros impares con yield

def odd_numbers():
    for i in range(10):
        if i % 2 == 0:
            yield i


for i in odd_numbers():
    print(i)


# metodo next
'''el metodo next imprime el iterable 1 a 1'''

def genera_pares(x):
    num = 1
    while num < x:
        yield num * 2
        num += 1
    
test = genera_pares(5)

print(next(test)) #output 2
print('test')
print(next(test)) #output 4
print('test')



