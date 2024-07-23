#funciones a importar
#no se coloca el print aqui debido a que si se coloca el print se imprimen todas las funciones


def seconds_hours(hours):
    seconds_per_hour = 60 * 60
    return seconds_per_hour * hours



def sumar(n1, n2, n3):
    print(n1 + n2 + n3)


def greetings(name=''):
    if name == '':
        print("Please enter a name")
    else:
        message = name + ', welcome to Python for Everyone!'
        return message


def add_two_numbers (num1, num2):
    total = num1 + num2
    return total