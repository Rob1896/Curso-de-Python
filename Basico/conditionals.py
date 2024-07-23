# IF CONDITION
#In python and other programming languages the key word if is used to check if a condition is true and to execute the block code.
# para que se ejecute el if la condicion tiene que ser verdadera 

test = True
if test:
    print('test is True')

# aqui la condicion no se ejecuta porque es falsa

TEST1 = False
if TEST1:
    print('TEST1 is 45')


a = 5 + 2
if a == 7:
    print('a is 7')

c = 5*3
if c>= 15:
    print('c is greater than 15')
    
condition = 3+7
if condition == 10:
    print('condition is greater than 10')

# As you can see in the example above, 3 is greater than 0. The condition was true and the block code was executed.
# However, if the condition is false, we do not see the result. 
# In order to see the result of the falsy condition, we should have another block, which is going to be else


# ELSE condition
# If condition is true the first block will be executed, if not the else condition will run. eje:
# else no necesita condicion
# else se ejecuta cuando ni if ni elif se cumplieron 



test = False
if test:
    print('test is Real')
else:
    print('test is Fake')


a = 5 + 4
if a == 7:
    print('a is 7')
else:
    print('a is not 7') 
    
a = 5 + 3
if a == 7:
    print('a is 7')
else:  
    a == 8     # si puede tener condicion 
    print('a is not 7') 
    
t = 5 + 45
if t == 10:
    print('t is 10')
else:
    print('t is not 10')
    
    
condition1 = 5*3

if condition1 == 25:
    print('condition1 is 25')
else:
    condition1 == 30
    print('condition1 is 30')


rob = 25
if rob  >= 27:
    print('rob is greater than 27')
elif rob <= 27: #elif SI necesita condicion 
    print('rob is less than 27')
#####
rob = 30
if rob == 27:
    print('rob is greater than 27')
elif rob <= 27: #elif SI necesita condicion 
    print('rob is less than 27')
else:
    rob == 30 # else puede tener condicion tambien 
    print('rob is equal to 30')


# ELIF CONDITION
# We use elif when we have multiple conditions
# if and elif always need a condition

a = 2 + 6
if a == 4: 
    print ("A is Four") 
elif a == 5:
    print ("A is Five") 
elif a == 6:
    print ("A is six")
else:
    print ("no condition") 
    
   
   
# Short hand
 
a = 4
print('A is positive') if a > 0 else print('A is negative')



# nested condition

a = 0
if a > -3:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')


# para evitar nested condition podemos usar "and" 
# Devuelve True si ambos elementos son True

hace_sol = True
es_findesemana = True

if hace_sol and es_findesemana:
    print('ire a la playa')
    
    
# ejemplo 2

g = 19

if g > 10 and g < 20: 
    print('g is between 10 and 20')

# ejemplo 3 con elif

dog_weight  = 25

if dog_weight > 10 and dog_weight < 20: # if no se cumplio
    print('dog is between 10 and 20 pounds')
elif dog_weight > 20 and dog_weight < 30:# elif si se cumplio
    print('dog is between 20 and 30 pounds')
    
  

# uso de OR
# El operador or devuelve True cuando al menos uno de los elementos es igual a True.
# Es decir, evalúa si el valor a la izquierda o el de la derecha son True. 

user = 'admin'
access_level = 2
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
    


calor = True
ir_piscina = False

if calor or  ir_piscina:
    print('tomar cerveza!')
    
    
# uso de NOT
# Not niega la operacion booleana
# lo que quiere decir que si algo es FALSE lo convierte en TRUE 
# y si algo es TRUE lo convierte en FALSE

my_string = False
if not my_string:
    print('my string is True')
    
 
# EJEMPLO 2
   
my_string2 = True

if not my_string2:
    print('my string is False')

# NO imprime nada, recordemos que if solo acepta TRUE y con el uso de not convetitmos la variable en False

# ejemplo 3

if not my_string2:
    print('my string is False')
else:
    print('my string is big')

#aqui se ejecuta el else, recordar que el else se cumple si el if no se cumple y es falso



# contar la veces que aparce una letra en una cadena

cadena3 = 'mamammmmsdadsmamasda'
count = 0
for i in cadena3:
    if i != 'm': # si es diferente a M que pase a la siguiente letra,cadd vez que i encuentre a M se ejecuta el Else
        continue 
    else: # si el IF NO SE CUMPLE que sume 1 al contador, o sea cada que i encuente a M.
        count = count + 1 # basicamente no esta buscando M en la cadena sino que cuenta las veces que el IF no se cumplio

print('Total number of m is:', count) # muestra el resultado de las veces que IF no se cumplio y se cumplio el else sumandole 1 al count 