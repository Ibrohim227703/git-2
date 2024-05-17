def duck():
    class Animal:
        def __init__(self, name, age, id, passport, voice):
            self.name = name
            self.age = age
            self.id = id
            self.passport = passport
            self.voice = voice

        def sound(self):
            return self.voice

        def get_age(self):
            return self.age

        def set_age(self, new_age):
            if new_age >= 0:
                self.age += new_age
            else:
                print("Invalid age")

    animal1 = Animal("Duck", 12, "1234", "AB123456", "Quack")
    print("Name:", animal1.name)
    print("Age:", animal1.get_age())
    print("ID:", animal1.id)
    print("Passport:", animal1.passport)
    print("Voice:", animal1.sound())

    new_age = int(input("Enter new age: "))
    animal1.set_age(new_age)
    print("New age:", animal1.get_age())
    return main()


def dog():
    class Animal:
        def __init__(self, name, age, id, passport, voice):
            self.name = name
            self.age = age
            self.id = id
            self.passport = passport
            self.voice = voice

        def sound(self):
            return self.voice

        def get_age(self):
            return self.age

        def set_age(self, new_age):
            if new_age >= 0:
                self.age += new_age
            else:
                print("Invalid age")


    animal1 = Animal("DOG", 10, "1234", "AB123456", "Woof")
    print("Name:", animal1.name)
    print("Age:", animal1.get_age())
    print("ID:", animal1.id)
    print("Passport:", animal1.passport)
    print("Voice:", animal1.sound())


    new_age = int(input("Enter new age: "))
    animal1.set_age(new_age)
    print("New age:", animal1.get_age())
    return main()



def cat():
    class Animal:
        def __init__(self, name, age, id, passport, voice):
            self.name = name
            self.age = age
            self.id = id
            self.passport = passport
            self.voice = voice

        def sound(self):
            return self.voice

        def get_age(self):
            return self.age

        def set_age(self, new_age):
            if new_age >= 0:
                self.age += new_age
            else:
                print("Invalid age")

    animal1 = Animal("CAT", 5, "1234", "AB123456", "Meow")
    print("Name:", animal1.name)
    print("Age:", animal1.get_age())
    print("ID:", animal1.id)
    print("Passport:", animal1.passport)
    print("Voice:", animal1.sound())


    new_age = int(input("Enter new age: "))
    animal1.set_age(new_age)
    print("New age:", animal1.get_age())
    return main()


def main():
    section = int(input(
    """Menu choose:
        1> Cat
        2> Dog
        3> Duck

        >>>>>>> """))
    if section == 1:
        return cat()
    if section == 2:
       return dog()
    if section == 3:
        return duck()
    else:
        print("Invalid")

class Person:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = int(age)
        self.sound = sound
    



if __name__ == "__main__":
    main()