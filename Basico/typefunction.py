# type sirve para saber que typo de dato hay 

# se puede hacer con print o sin print:

name = 'roberto'
type(name)
print(type(name))


surename = 'mercado'
age = 27
city = 'grecia'
height = 1.70
print(name, surename, age, city)


type(age)
type(city)
type(height)

print(type(age))
print(type(city))
print(type(height))



# conversion de tipos de datos


# int to float
num_int = 10

print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# str to int
number = "45"
type(number) #type str

number = int(number)
print(number)
type(number) #type int

# number to float
number = float(number)
print(number)
type(number)

#float to str
number = str(number)
print(number)
type(number)