'''Claro, *args y **kwargs son usados para manejar un número variable de argumentos en funciones de Python. 
*args se usa para pasar una lista de argumentos posicionales,
mientras que **kwargs se usa para pasar un diccionario de argumentos de palabra clave. Por ejemplo:'''

def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60,56,78,90,78)
func1(80, 100)


#ejemplo 2
def myfunc(*args):
    return sum(args)*.05

print(myfunc(40,60,20))


# siempre va a devolver en tupla 
def ejemplo_args(*args):
    print(type(args))  # Imprime el tipo de args
    print(args)        # Imprime el contenido de args

ejemplo_args(1, 2, 3)  # Salida: <class 'tuple'> (1, 2, 3)
ejemplo_args("a", "b") # Salida: <class 'tuple'> ('a', 'b')
ejemplo_args()         # Salida: <class 'tuple'> ()


#ejemplo 3
def suma(*args):
    total = 0
    for i in args: # i va a iterar en cada argumento que le pase 
        total += i # va a sumar total + i o sea va a sumar cada argumento pasado
    return total # va a devolver el resultado de sumar todos los argumentos 

resultado = suma(1, 2, 3, 4, 35) #le paso los argumentos a sumar 
print(resultado)  # Output: 45

#ejemplo 4 **kwargs

def detalles_persona(**kwargs):
    for x, y in kwargs.items():
        print(x + ":", y)

detalles_persona(nombre="Juan", edad=30, ciudad="Madrid")


#ejempl 4 **kwargs

def myfunc(**kwargs):
    if 'fruit' in kwargs: # si la palabra fruit esta al llamar la funcion 
        print(f"My favorite fruit is {kwargs['fruit']}")  # que ejecute esto
    else:
        print("I don't like fruit") #s no que ejecute este else 
        
myfunc(x ='pineapple') # se ejecuta el else porque 'fruit' no esta al llamar la funcion
myfunc(fruit = 'apple')

#ejemplo usando args y kwargs
def imprimir_detalles(*args, **kwargs):
    print("Argumentos posicionales:")
    for arg in args:
        print(arg)
    
    print("\nArgumentos de palabra clave:")
    for key, value in kwargs.items():
        print(key + ":", value)

imprimir_detalles("Hola", "Mundo", saludo="¡Hola!", despedida="Adiós")

#ejemplo 2 
def imprimir_detalles2(*args, **kwargs):
    print("Argumentos posicionales:")
    for arg in args:
        print(arg)
    
    print("\nArgumentos de palabra clave:")
    for key, value in kwargs.items(): # imprime ambos keys=value
        print(key + ":", value)

    print("\nSolo Valores: ")
    for value in kwargs.values(): # imprime solo valores
        print('valores: ', value)
    
    
    print("\nSolo Keys: ")
    for key in kwargs.keys(): # imprime solo keys
        print('keys: ', key)


    
imprimir_detalles2("Hola", "Mundo", saludo="¡Hola!", despedida="Adiós")



#ejemplo 2  
def ejemplo(*args, **kwargs):
    for arg in args:
        print("Argumento posicional:", arg)
    
    for key, value in kwargs.items():
        print("Argumento de palabra clave:", key, "=", value)

# Usando *args y **kwargs
ejemplo(1, 2, 3, nombre="Juan", edad=30)



def demo(*args):
    print(args)


demo('Maggie',56,'Peggy',56) # esto imprime ('Maggie', 56, 'Peggy', 56)



def demo1(*args):
    for i in args: print(i)

demo1('Maggie',56,'Peggy',56) 
''' output:
Maggie
56
Peggy
56'''

#ejemplo **kwargs

def register_user(user,**kwargs):
    print(f'User name: {user}')
    for key, value in kwargs.items():
        print(f'{key}: {value}')

register_user('Juan', age=34, city='Monaco')

#ejemplo 2 **kwargs
def update_DB(name,**kwargs):
    print(f'Updating profile: {name}') # este print solo es para imprimir el parametro 'name
    for key, value in kwargs.items():
        print(f'Updating {key} to {value}')

update_DB('Juan', age=30, city='Madrid')




'''Que hace el .get 
Se usa para obtener el valor asociado a una calve especifica
si la clave no existe el .get devuelve un valor predeterminado
'''

'''sintaxis:
valor = dic.get(clave, valor_predeterminado)'''



def configurar_conexion(**kwargs):
    configuracion = {
        "host": kwargs.get("host", "localhost"), # si host no esta presente se usa el valor predeterminado "localhost"
        "port": kwargs.get("port", 5432), # si port no esta presente se usa el valor predeterminado "5432"
        "user": kwargs.get("user", "root"), # si user no esta presente se usa el valor predeterminado "root"
        "password": kwargs.get("password", "") # si pwd no esta presente se usa la cadena vacia como valor 
    }
    print("Configuración de conexión:", configuracion) # esto va a imprimir el diccionaro con los {}

# Llamada a la función
configurar_conexion(host="192.168.1.1", user="admin", password="1234", port= 34544)



def configurar_conexion(**kwargs):
    configuracion = {
        "host": kwargs.get("host", "localhost"), # si host no esta presente se usa el valor predeterminado "localhost"
        "port": kwargs.get("port", 5432), # si port no esta presente se usa el valor predeterminado "5432"
        "user": kwargs.get("user", "root"), # si user no esta presente se usa el valor predeterminado "root"
        "password": kwargs.get("password", "") # si pwd no esta presente se usa la cadena vacia como valor 
    }
    for k, v in configuracion.items(): # esto va a a imprimir cada key con su  valor 
        print(f"{k}: {v}")

# Llamada a la función
configurar_conexion(host="192.168.1.1", password="1234", port= 34544)




def enviar_mensaje(destinatario, **kwargs):
    mensaje = kwargs.get("mensaje", "Hola!")
    print(f"Enviando mensaje a {destinatario}: {mensaje}")
    if "firma" in kwargs:
        print(f"Firma: {kwargs['firma']}")

# Llamada a la función
enviar_mensaje("Ana",  firma="Tu amigo, Pedro")

