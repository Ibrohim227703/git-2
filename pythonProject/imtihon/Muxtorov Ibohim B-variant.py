#1-misol

class Phone:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_name(self, new_name):
        self.name = new_name

    def set_color(self, new_color):
        self.color = new_color

    def set_price(self, new_price):
        self.price = new_price


phone1 = Phone("iPhone 13", "Black", 999)

phone2_name = str(input("Enter Name>>>  "))
phone2_color = str(input("Enter color>>>  "))
phone2_price = int(input("Enter price>>>  "))

phone2 = Phone(phone2_name, phone2_color, phone2_price)

print("Phone 1:", phone1.get_name())
print("Price of Phone 1:", phone1.get_price())

print("Phone 2:", phone2.get_name())
print("Price of Phone 2:", phone2.get_price())



#2- misol
class Animal:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

animal = Animal("Tiger")


print(animal.get_name())


#3-misol

#1 misol
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(self.name + "sound")


class Cat(Animal):
    def cat(self):
        print(self.name + "Meov Meov")


class Dog(Animal):
    def dog(self):
        print(self.name + "WOW WOW")


cat = Cat("")
cat.cat()

dog = Dog("")

dog.dog()


print("____________________________________")
# 2 misol

class Car:
    def __init__(self, model):
        self.model = model

    def name(self):
        print(self.model + "Name")


class AUDI(Car):
    def audi(self):
        print(self.model + "Audi")


class SUPRA(Car):
    def supra(self):
        print(self.model + "Supra")


audi = AUDI("")
audi.audi()

supra = SUPRA("")
supra.supra()

#4-msol



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print("Men " + self.name + ", " + str(self.age) + " yoshdaman.")



class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_info(self):
        print("Men talaba " + self.name + ", " + str(self.age) + " yoshdaman.")
        print("Mening talaba ID'im: " + str(self.student_id))



person = Person(input("Ism kiritin>>>>  "), input("Yosh kiritin>>>>  "))
person.get_info()

print("----------------------------")


student = Student(input("Ism kiritin>>>>  "), input("Yosh kiritin>>>>  "), 2222)
student.get_info()

