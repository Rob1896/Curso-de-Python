# List sintax: list = []
# list sintax 2: list = list()

list = [1,2,3,4]
print(list)
len(list)


fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']


print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

print(type(fruits))
type(vegetables)
type(animal_products)


# acceder a los datos de la lista usando indexing 

fruits[0]
fruits[1]
fruits[2]
fruits[3]

#acceder a los datos de la lista de al reves

vegetables[-1]
vegetables[-2]
vegetables[-3]

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruitss = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']

print(fruits[0:2])
print(fruits[1:3])
print(fruits[1:])
print(fruits[::2])
print(all_fruits)
print(all_fruitss)
print(orange_and_mango)

# unpacking list
# es asignarle variables a cada uno de los elementos de la lista:

lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']


# First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits 
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)




# concatenate list:

my_new_list = fruits+countries
print(my_new_list)

# agregando una lista a otra con .extend

lista=[1,2,3,4]
lista2= [10,11,12]

lista.extend(lista2)
print(lista)

#agregar cosas al final de una lista con .append

lista.append(13)
lista
print(lista)

# modificar una lista

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']


# agregando cosas a la lista usando .insert

fruits.insert(2,'papaya')
fruits

fruits.insert(0,'kiwi')
fruits

# elminando objetos de la lista usando .pop

fruits.pop(3)  # elmina papaya 
fruits

fruits.pop() # si no le indicamos el index elimina el ultimo elemento 
fruits

# elminando objetos de la lista usando.remove 
# con .remove podemos indicar el elemento que queremos elminar

fruits.remove('mango')
fruits


# eliminar objetos de la lista usando del
# syntax
lst23 = ['item1', 'item2']
del lst23[0]
lst23# only a single item
del lst        # to delete the list completely


# metodo sort/reverse
lista

lista.reverse() # orenda la lista al reves 
lista

lista.sort() # ordena la lista 
lista

# limpiando lista usando clear
# syntax
lst45 = ['item1', 'item2']
lst45
lst45.clear()
lst45

# Copiar una lista con .copy()


lst22 = ['item1', 'item2', 'item3']
lst22
lst21 = lst22.copy()
lst21


# contar elementos de una lista con .count()

super = ['trufas', 'apples','milk','juice','rice','apples','oranges','apples']

super.count('apples')


# saber el indexing de un item de la lista

super = ['trufas', 'apples','milk','juice','rice','apples','oranges','apples']

super.index('apples')
super.index('juice')


my_list5 = list(['trufas', 'apples','milk','juice'])

print(type(my_list5))
print(my_list5)


#creandd lista desde lista vacia

even_numbers = []

for i in range(1,10):
    if i % 2 == 0:
        even_numbers.append(i)

print(even_numbers)


even_numbers = list()

for i in range(1,10):
    if i % 2 == 0:
        even_numbers.append(i)

print(even_numbers)


