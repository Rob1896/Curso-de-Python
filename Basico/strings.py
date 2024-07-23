# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=8643

### Strings ###
#Creating a string#

letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

my_string = "Mi String"
my_other_string = 'Mi otro String'


# String lenght

string1 = 'test'
len(string1) 
print(len(string1))
#ambas son los mismo

print(len(my_string))
print(len(my_other_string))

# concatenate strings
print(my_string + " " + my_other_string)



my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo/formating 
# .format
print('This is a string with an {}'.format('insert'))

#Otra manera de hacerlo es grabando la variable primero para luego solo darle print a la string: 
e='Peggy'
t='Maggie'
final_message= 'The names of my dogs are {} and {}'.format(e,t)
print(final_message)

first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)


#.format  with indexing
print('{0} you {2} be {1} {3} {4}'.format('tomorrow','home','should','before','dark'))
print('The {} {} is {}'.format('forest','tree','blooming'))

#format with keys:
print('maggie le gustan {k}, {z} y los {l}'.format(k='los gatos',z="las iguanas", l='tomates'))


# f-string
nombre = "Juan" 
edad = 25 
mensaje = f"Hola, me llamo {nombre} y tengo {edad} años." 
print(mensaje) 

h="computadora"
o="pantalla"
print(f'ayer fui por la {h} pero olvide la{o}')


# String slicing 
# se puede usar print o se puede usar la variable usando los []
# abajo se ven ambas maneras

language = "python"  #variable 

language_slice = language[1:3]
print(language_slice)

language_slice[1:3]   # mismo resultado que con print

language_slice = language[1:6]
print(language_slice)

language[1:6] # mismo resultado que con print


language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse
# para hacer reverse string o poner la cadena al reves 

reversed_language = language[::-1]
print(reversed_language)

language[::-1]  # mismo resultado que con print

# Funciones 

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo

language.capitalize()  # hace la primera letra de la strin en mayuscula 
language.upper() # hace toda la string en mayuscula 
language.lower() # hace toda la string en minuscula 
language.count('o') # cuenta el numero de veces que aparece un caracter en una string
language.isnumeric() # para verificar si todos los caracteres son numericos
language.isupper() # para verificar si todos los caracteres estan en mayuscula
language.islower() # para verificar si todos los caracteres estan en minuscula 
language.lower().isupper() # se usan combinadas y hacen la misma funcion(false porque estan en minuscula)
language.upper().isupper() # se usan combinadas y hacen la misma funcion(true porque ahora estan en mayus)
