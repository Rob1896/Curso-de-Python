# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.


# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct
dct['key1'] # esto solo se imprime usando shit+enter
dct['key2']

print(empty_dict)
print(dct)

my_new_dic = {'first_name':'Robert', 'last_name':'Mercado','Country':'Costa rica','city':'Grecia','age':25,'is_active':'yes'}


# We can access Dictionary items by referring to its key name

my_new_dic['Country'] # esto solo se imprime usando shift+enter
my_new_dic['age']

# con print

print(my_new_dic['Country'])
print(my_new_dic['age'])
print(my_new_dic['is_active'])

# con .get vamos a recibir un none en caso de que la entrada no exista

print(my_new_dic.get('continent')) # esto v a evitar que de error en caso de que la entrada no exista



# adding data to a dictionary 

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct
dct['key5'] = 'value5'
dct

dct['country'] = 'usa'
dct



# modify data 
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct
dct['key1'] = 'value-one'
dct


dct['key2'] = 'testing'
dct

# verificar si existe keys dentro del diccionario:

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key4' in dct)
print('key5' in dct)

# esto soloverifica las entradas y no los valores 
#ejemplo:

print('valie1' in dct) # False porque no es un Key sino un valor de key 

# para ver solo los keys del diccionario
keys = dct.keys()
print(keys)

# para ver solo los valores del diccionario

values = dct.values()
print(values)



#pop(key): removes the item with the specified key name:
#popitem(): removes the last item
#del: removes an item with specified key name
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem()# removes the last item
dct

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct['key2'] # removes key2 item
dct


