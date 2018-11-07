# dog class
class Dog:
    all = "mammals"
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def eating(self):
        self.is_hungry = False

        # using the pets class to manipulate dog class instances
class Pets:
    dogs = []
    
    def __init__(self,dogs):
        self.dogs = dogs

domestic = [Dog("Tom",6),Dog("Fletcher",7),Dog("Larry",9)]

pets = Pets(domestic)

print("I have {} dogs".format(len(pets.dogs)))

for dog in pets.dogs:
    dog.eating()
    print("{} is {}".format(dog.name,dog.age))

print("And they're all {},ofcourse.".format(dog.all))

all_hungry = False

for dog in pets.dogs:
    if dog.is_hungry:
        all_hungry = True
if all_hungry:
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry")

