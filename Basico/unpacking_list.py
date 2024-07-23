# unpacking list
# es asignarle variables a cada uno de los elementos de la lista:

lst3 = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst3 #este *rest significa el resto de elemento de la lst3
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']


# First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *restante = fruits  #puede llevar cualquier nombre 
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(restante)           # ['lemon','lime','apple']

# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries #el scandic va a tomar en cuenta el resto de items que no son guardados en una variable 
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic) # output: ['Denmark', 'Finland', 'Norway', 'Iceland'] no estan en una variable almacenados
print(es)




# unpacking using functions 

def sumar(a,b,c):
    return a+b+c

valores = [1,2,4]
resultado = sumar(*valores)
print(resultado)


# unpacking using bucles
numeros = [(1,'uno'),(2,'dos'),(3,'tres')]

for n, a in numeros:
    print(f'{n} es {a}')



# unpacking ignoring some values

valores1 = [1,2,3,4,5,6,7]
a,b, _ = valores1[:3] # el _ bajo va ignorar el resto de valores pero debo colocar el index correcto 

print(a)

print(b)



countries2 = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, _ = countries2[:5] 
print(gr)
print(fr)
print(bg)
print(sw)