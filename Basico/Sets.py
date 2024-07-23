# Set is a collection of unordered and un-indexed distinct elements.
#In Python set is used to store unique items, no permite duplicados.
# and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.
#Puedes crear un conjunto utilizando llaves {} o la función set().


# syntax
st = {'item1', 'item2', 'item3', 'item4'}

my_set = {'Roberto', 27, 'Grecia'}
print(type(my_set))


fruits = {'banana', 'orange', 'mango', 'lemon'}

len(fruits)

# acceder a los elementos de un set


fruits[0] #da error porque un set no es ordenado entonces no  tiene indexing 

# forma correcte de acceder a los elementos de un set
print("banana" in  fruits) #TRUE

print("lemon" in fruits)  #TRUE 

print('avocado' in fruits) #FALSE 

# Agregar elementos a un set
# los elementos no se agrgar en orden 

fruits.add('supermarket')
fruits 

my_set.add(34)
print(my_set)

my_set.add('alajuela')  # no los agrega al final porque los sets no tienen orden
my_set

my_set.add('Roberto')  # si agrego un elemento duplicado solo se imprime una vez
my_set


# Eliminar elementos de un set

fruits.remove('mango')
fruits

fruits.remove('orange')
fruits

# clear un set

fruits.clear()
fruits

# del con un set

del fruits
fruits


# conevetir una lista a un set
#  We can convert list to set and set to list. Converting list to set removes duplicates and only unique items will be reserved.

fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
type(fruits)
fruits = set(fruits) 
type(fruits)


list1 = [1,1,2,2,3,4,5,6,1,1]

list1=set(list1) # esto va a eleminiar los duplicados
list1



# union set



fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}

fruits.union(vegetables)
fruits


# update a set 

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits)



# fucion intersection:
# devuelve los elementos que estan en ambos sets(repetidos )

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}

