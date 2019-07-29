# state1 = "New York"
# abbr1 = "NY"
# state2 = "Californo"
# abbr2 = "CA"
#
# print(abbr2 + " is short for " + state2)
#
# states = ("CA = California", "NY = New York")
# states_abbr = ["CA", "NY"]
# states = ["California", "New York"]
# for state in range(len(states)):
#     print(state_abbr[index] + " is short for " + states[index]
#
#
# states = {
#     "NY": "New York",
#     "MI": "Michigan",
#     "FL": "Florida"
# }
#
# print(states["MI"])
# print(states)
#
# for state in states:
#     print("Key is " + state)
#     print("Value is " + states[state])
#     print(state)
#
#
# rappers = {
#     "BAD": "Lil Dicky",
#     "AVG": "Drake",
#     "BEST": "Kendrick"
# }
#
# for rapper in rappers:
#     print("Key is " + rapper)
#     print("Value is " + rappers[rapper])
#
#
#
# pet = {
#     'name': 'Skeemer',
#     'animal': 'dog',
#     'breed': 'bichon frise',
#     'age': 16
# }
#
# class Pet(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def bark(self):
#         print("Ruff ruff ruff")
#
# my_pet = Pet("Finn", 14)
# my_pet.bark()
# print("My new pet is " + my_pet.name + " and he/she is " + str(my_pet.age))
#
#
# pets = [
#     pet,
#     {
#     'name': 'Michael',
#     'age': 5
#     }
# ]
#
#
#
#
#
# print(pets)
#
#
# modify
# print(pet['name'] + ' has disassociated himself from the Walshes')
# pet['name'] = 'Simba'
# print(' and shall now be known as ' + pet['name'])
#
# add
# pet['favorite'] = 'milkbone'
# print(pet['favorite'])
#
# Remove
# print(pet)
# pet.pop('age')
# print(pet)
#
#
#
# roberts_life = {
#     'name': 'Robert',
#     'age': 17,
#     'movies': {
#         'name': 'Avenger\'s End Game',
#         'rating': 'PG-13',
#         }
# }
#
# print(roberts_life)
#
# for life in roberts_life:
#     print("Key is " + life)
#     if type(roberts_life[life]) == type("dict"):
#         for nested_key in roberts_life[life]:
#             print("nested key is " + nested_key)
#             print("nested value is " + roberts_life[life])
#
#     print("Value is " + str(roberts_life[life]))
#
#     print("Movie is " + str(roberts_life[life]))
#     print(roberts_life)
#         for movie in movies:
#             print("The rating for his favorite mo")
#
# for state in states:
#     print("Key is " + state)
#     print("Value is " + states[state])
#     print(state)
















class Pokemon(object):
    # Constructor
    def __init__(self, name, type, sex):
        self.name = name
        self.type = type
        self.sex = sex

    def attack(self, move):
        # print(move)
        print("My name is " + self.name + " and my move is " + move)

class Pikachu(Pokemon):
    def __init__(self, name, type, sex, voltage, current):
        super(Pokemon, self).__init__(name, type, sex)
        self.voltage = voltage
        self.current = current

class Charizard(Pokemon):
    def __init__(self, name, type, sex, tail_flame_size):
        Pokemon.__init__(self, name, type, sex)
        self.tail_flame_size = tail_flame_size

    def burnTheGuy(self):
        print("$$$$$")


char = Charizard("Charry", "flame-fly", "F", "large")
# print(char.tail_flame_size)

(char.attack("burn"))
(char.burnTheGuy())

# myPokemon = Pokemon("Pikachu", "electric", "Male")
# myPokemon.attack("electro shock therapy")
# print(myPokemon.sex)





#
