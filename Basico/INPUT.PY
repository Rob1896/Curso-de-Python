#  se graba la variable como lo haria normalmente en este caso son "first name" y "age" 
# luego se coloca input despues del = y se coloca el texto que quiero que el usuario vea
# en este caso va a ver "what is your name:  y " how old are you?" 
# usuario ingresa los datos y luego se imprime la variable con la funcion print#

#la funcion imput siempre va a tomar todo como texto


first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)


#los datos ingresado con imput() siempre son cadenas
# ejemplo:
# para que sea tomado como numero se hace asi:
#sintax: el int combierte el input en type int 

num = int(input('type your number: '))
print("Your number  * 2 is: ")
print(num * 2)



name = input("Ingresa tu nombre: ")
print("Hola, " + name + ". ¡Un gusto conocerte!")

###3

anything = input("Dime lo que sea...")
print("Hmm...", anything, "...¿en serio?")


# Write a program to accept two numbers from the user and calculate multiplication

number = int(input('insert a number: '))
number2= int(input('insert a second number: '))

result = number * number2

print("Result: ", result)



