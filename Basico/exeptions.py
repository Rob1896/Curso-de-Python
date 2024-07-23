
# siempre que hay un try tiene que haber un except

try:
    print(10 + '5')
except:
    print('Something went wrong')



n1 = 3
n2 = 4
n3= '4'

try: 
    print(n1+n3)
except: # este except se ejecuta cuando el try da error
    print('hubo un error')
    
    
try:
    print(n1+n2)
except: # este except NO se ejecuta y salta al else 
    print('hubo un error')
else: #este else es opcional
    print('aqui sigue el programa')
    
# si queremos saber la razon del error 


# este ejemplo va a dar error
residuo1 = 3 % 't'
print(residuo1)

#como evitar o informar el error: 

try:
    residuo = 3% 't'
    print(residuo)
except TypeError as e:
    print('the error is: ', e)
    
# ejemplo 2
try:
    multiplication = 10-'3'
    print(multiplication)
except:
    print('fatal error') # esto solo va a colocar este print pero no la razon del error


try:
    multiplication = 10-'3'
    print(multiplication)
except TypeError as e: # puede ser cualquier nombre de variable pero se usa E por generalidad 
    print('the error is: ', e) # la e en este print nos va a dar la razon del error
    
# este ejemplo va a dar error
multiplication2 = 3 % 't'
print(multiplication2)

try:
    resultado = 10/0
except ZeroDivisionError as e:
    print('error: ', e)
    

# ejemplo con una app mas grande:


def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):		
    try: # este try es como un IF si se ejecuta da el resultado pero sino pasa al except
        return num1/num2
    except ZeroDivisionError:  # si el try falla se ejecuta este except y se imprime 
        print("No se puede dividir por cero")
        return "operacion erronea"
    
# que pasa si el usuario ingresa algo que NO es numero como un str?
# se ejecuta otro try en la liena donde se genera el error en este caso en los input que solicitan los numeros

while True:
    try: 
        op1=(int(input("Insert a number: ")))

        op2=(int(input("Insert another number: ")))	
        break # este break detiene el while cuando es TRUE o sea cuando son numeros en este caso
    except:
        print("Error, only numbers allowed")	
	
operacion=input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operacion no contemplada")


print("Operacion ejecutada")