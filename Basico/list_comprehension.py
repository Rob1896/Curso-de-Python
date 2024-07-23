# Sintax:
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.

# Condition
# The condition is like a filter that only accepts the items that valuate to True

#examples:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x] #condicion if va a tomar en cuenta solo las que son TRUE, es decir las que llevan A en el item
print(newlist) # aca va a salir la nueva lista que los items que NO llevan A




fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print(fruits)
newlist = [x for x in fruits if x != "apple"] # # Only accept items that are not "apple"
print(newlist)

# The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".

newlist = [x for x in range(10) if x < 5] #[0, 1, 2, 3, 4]
# la condicion en este caso va a crear la lista con los numeros del 1 al 4

# Iterable
# The iterable can be any iterable object, like a list, tuple, set etc.

#ejemplo con range
newlist = [x for x in range(10)]
print(newlist) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#ejemplo con una string

newlist = [x for x in 'hello Marte']
print(newlist) # ['h', 'e', 'l', 'l', 'o', ' ', 'M', 'a', 'r', 't', 'e']

word = 'hello python'
newlist = [x for x in word] # mismo ejemplo pero con la variable de la string
print(newlist)


# ejemplo con lista:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist) # ['apple', 'banana', 'cherry', 'kiwi', 'mango']



#For instance if you want to change a string to a list of characters. You can use a couple of methods. Let's see some of them:
# One way
language = 'Python'
print(language)
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension

frase = 'Hello world'
lst = [i for i in frase]
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

newlist = [x for x in 'hello Marte']
print(newlist) # ['h', 'e', 'l', 'l', 'o', ' ', 'M', 'a', 'r', 't', 'e']

word = 'hello python'
newlist = [x for x in word] # mismo ejemplo pero con la variable de la string
print(newlist)


# For instance if you want to generate a list of numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
#Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# With list comprehension you can do all that with only one line of code:
# combinado con IF

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


# generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers) 

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
print(odd_numbers) 



# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
#Return "orange" instead of "banana":

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# The expression in the example above says:
#"Return the item if it is not banana, if it is banana return orange".

