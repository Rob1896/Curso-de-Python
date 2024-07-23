

'''formas de pasarle argumentos a una funcion'''
#posicional arguments
def personal_data(first_name, second_name, last_name, email):
    print(f'Welcome {first_name} {second_name} {last_name} to the python course, your email is: {email}')


personal_data('Roberto','jefte','mercado','rob@hotmail.com')


#keyword arguments

def personal_data(first_name, second_name, last_name, email):
    print(f'Welcome {first_name} {second_name} {last_name} to the python course, your email is: {email}')


personal_data(first_name='Roberto',second_name='jefte',last_name='mercado',email='rob@hotmail.com') # esto se puede evitar con los iterable unpacking 


# iterable unpacking 

def personal_data(first_name, second_name, last_name, email):
    print(f'Welcome {first_name} {second_name} {last_name} to the python course, your email is: {email}')

data=('Roberto','Jefte','Mercado','rob45@gmail.com') #tuple
data1=['Rob','Jef','Sanchez', 'rob34@gmail.com'] #lista
data3 = {
    'first_name':'Robert',
    'last_name':'Mercado',
    'second_name' : 'Jeftee',
    'email':'rob4455@gmail.com'
}                           # dictionary 

personal_data(*data)
personal_data(*data1)
personal_data(**data3)