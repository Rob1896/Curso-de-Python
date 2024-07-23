


def genera_pares(x):
    num = 1
    while num < x:
        yield num * 2
        num += 1
    
test = genera_pares(5)

print(next(test)) #output 2
print('test')
print(next(test)) #output 4
print('test')

