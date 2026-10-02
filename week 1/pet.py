class Pet:

    species = ""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_human_age(self):
        return self.age * 7

    def get_lifespan(self, species):
        if species == "dog":
            return 12
        elif species == "cat":
            return 15
        elif species == "rabbit":
            return 10


name1 = input("Enter the name of your first pet: ")
age1 = int(input("Enter the age of your first pet: "))
species1 = input("Enter the species of your first pet: ")

name2 = input("Enter the name of your second pet: ")
age2 = int(input("Enter the age of your second pet: "))
species2 = input("Enter the species of your second pet: ")

name3 = input("Enter the name of your third pet: ")
age3 = int(input("Enter the age of your third pet: "))
species3 = input("Enter the species of your third pet: ")

pet1 = Pet(name1, age1)
pet2 = Pet(name2, age2)
pet3 = Pet(name3, age3)