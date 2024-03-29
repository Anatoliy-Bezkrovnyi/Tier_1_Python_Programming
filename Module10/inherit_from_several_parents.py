class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def info(self):
        return f"{self.nickname}-{self.weight}"


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"
    
class CatDog(Cat, Dog):
    pass
    

class DogCat(Dog, Cat):
    pass

catdog = CatDog("Barbos", 23)
dogcat = DogCat("Tapok", 10)
print(catdog.say())
print(dogcat.say())
print(catdog.info())
print(dogcat.info())