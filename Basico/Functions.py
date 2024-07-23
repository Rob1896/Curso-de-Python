# A function is a reusable block of code or programming statements designed to perform a certain task.
#  Function can be declared with or without parameters.



# syntax
# Declaring a function
#def function_name():
   # codes
    #codes
# Calling a function
#function_name()

# ejemplo funcion sin parametros:

def generate_full_name (): #estos () estan vacios porque estan sin parametros
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name) # este print es el resutlado de mi funcion 


generate_full_name () # calling a function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)


add_two_numbers() # aqui  no necesito argumento porque la funcion no tiene parametro



#Ejemplo de funcion con parametros
# al tener parametros  siempre se debe llamar con argumentos

def greetings (name): #lo que esta dentro de los () son los parametros
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Rob')) # mi argumento es 'Rob'



# se puede usar la funcion con o sin  print al llamarla

#ejemplo de llamado de funcion sin el print:
def sumando (nume1, nume2): # pueden llevar varios parametros
    print(nume1+nume2)
    
sumando(45,4) # aqui no es necesario el print pero si el argumento

def name(firstname, surename):
    print(firstname + ' ' + surename)

name('Maggie', 'Garcia') 
name(firstname= 'Maggie', surename= 'Miranda') # mismo  resultado
    
    
#ejemplo de llamado de funcion con el print:  
# es necesario usar return

    
def restando(num1, num2): 
    total = num1-num2
    return total # el return hace los mismo que el print de los ejemplos de arriba

print(restando(10,3)) # igual es necesario el argumento y se van en (())
print(restando(num1=45, num2=27)) #mismo resultado



def add_ten(num):
    ten = 10
    return num + ten # le puedo agregar al return el codigo o funcion que quiero que realice 

print(add_ten(456))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age

print('Age: ', calculate_age(2024, 1996)) # al print se le pueden agregar cosas como strings


def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print(print_fullname(firstname = 'Roberto', lastname = 'Mercado')) 
print(print_fullname('Aly', 'Miranda')) 
print_fullname('a', 'Miranda') # este no funciona
print_fullname(firstname='Peggy', lastname='Mercado') # esto no funciona


def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print(print_fullname('Alyssa', 'Miranda')) # esto es lo mismo que la funcion aterior

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(3,2))

######################################

#functions returning a boolean value  and using  conditionals 

def is_even (n):
    if n * 2 == 30:
        print('felicidades')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(19)) 

def is_even (n):
    if n * 2 == 20:
        print('Congrats!')
        return True
    else:
        print('Sorry')
    return False
print(is_even(19)) 

def greetings(name=''):
    if name == '':
        print("Please enter a name")
    else:
        message = name + ', welcome to Python for Everyone!'
        return message
    
print(greetings('Roberto'))


#Sometimes we pass default values to parameters, when we invoke the function. 
# If we do not pass arguments when calling the function, their default values will be used.


def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())

print(greetings('Robert'))



def saludo(name = 'peter'):
    message = name + 'message1'
    return  message

print(saludo())


# varios return/ multiple return values

def arithmetic(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    multiply = num1 * num2
    division = num1 / num2
    # return four values
    return add, sub, multiply, division

# read four return values in four variables
a, b, c, d = arithmetic(10, 2)

print("Addition: ", a)
print("Subtraction: ", b)
print("Multiplication: ", c)
print("Division: ", d)



def calculation(a, b):
    addition = a + b
    subtraction = a - b
    # return multiple values separated by comma
    return addition, subtraction

# get result in tuple format
print(calculation(20, 5))

res = calculation(20, 5)

print(res)