
# se  pueden importar funciones de otros files para reutilzarlas



from module import seconds_hours 


print(seconds_hours(6))
print(seconds_hours(5))



import module
module.seconds_hours(4) 
module.add_two_numbers(34,45)


from module import greetings, add_two_numbers 


print(greetings('Pedrito'))
print(add_two_numbers(23,45))







