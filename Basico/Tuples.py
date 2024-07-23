### A tuple is a collection of different data types which is ordered and unchangeable (immutable). 
# Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. 
# We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable).
# Unlike list, tuple has few methods. Methods related to tuples:

# syntax
tpl = ('item1', 'item2','item3')
fruits = ('banana', 'orange', 'mango', 'lemon')


# tuples lengths

len(tpl)
print(len(tpl))
len(fruits)
print(len(fruits))


# accediendo tuples usando indexing

tpl[0]
print(tpl[0])
tpl[1]
print(tpl[1])
tpl[2]

# negativo tuples usando indexing

tpl[-1]
print(tpl[-1])

fruits[-2]
print(fruits[-2])

# slicing tuples

fruits[0:2]
fruits[0:]
fruits[1:3]


#We can change tuples to lists and lists to tuples.
# Tuple is immutable if we want to modify a tuple we should change it to a list.

# Syntax
tpl = ('item1', 'item2', 'item3','item4')
type(tpl)
lst = list(tpl)
type(lst)

#Checking an Item in a Tuple
#We can check if an item exists or not in a tuple using in, it returns a boolean.

# Syntax
#hay 2 formas de hacer, una con print y otra sin print
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl 

fruits = ('banana', 'orange', 'mango', 'lemon','papaya','watermelon')
print('orange' in fruits)
'orange' in fruits 


print('watermelon' in fruits)
'watermelon' in fruits

print('strwaberry' in fruits)
'stringwaberry' in fruits

# uniendo tuples

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
fruits_and_vegetables


#deleting tuples 

del tpl


# desempaquetado de tuples

fruits = ('banana', 'orange','mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')

rico, vitamina_c, verde, acido = fruits

print(rico, vitamina_c)



