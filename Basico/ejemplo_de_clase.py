class Personaje:
    #atributos
    def __init__(self, name, power, level, defense, life_level):  
        self.name = name
        self.power = power
        self.level = level
        self.defense = defense
        self.life_level = life_level
    # metodos:
    def atributos(self):
        print('Name: ', self.name)
        print('Power: ', self.power)
        print('Level: ', self.level)
        print('Defense: ', self.defense)
        print('Life level: ', self.life_level)
        
    def level_up(self,  x, y):
        self.level = self.level + x
        self.defense = self.defense + y
    
    def available(self):
        if self.level > 8 and self.defense > 50:
            return True

        else:
            return False
    
    def welcome_message(self): # este metodo depende del metodo available para cumplirse
        if self.available():
            print(f"Welcome {self.name} to the game!")
            return
        else:
            print(f"You are not ready {self.name}. Come back when you are stronger!")
        
    
# le paso los atributos grabando en una variable
#instanciar clase
My_skin = Personaje('Carter', 'Run fast', 6, 23, 'high')
Enemy =  Personaje('Kitty CaT', 'attack your face',2, 66, 'high')







# forma de acceder a los atributos:
print('name: ', My_skin.name)
print('name: ', Enemy.name)
print('level: ', My_skin.level)
print('level: ', Enemy.level)

print('\n')


# forma de acceder a los metodos
My_skin.welcome_message()
My_skin.available() # esto no imprime nada en consola por se valores booleanos 
Enemy.available() # esto no imprime nada en consola por se valores booleanos 


# modifico los niveles para que se cumpla el welcome message
My_skin.level_up(5,45) # esto le suma a los valores iniciales en la instancia(level y defense)
My_skin.welcome_message() #ahora si se cumplen las condiciones del welcome message
My_skin.atributos()




