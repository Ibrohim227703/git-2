# # OOP => Object Oriented Programming
# username = 'John'
# john = ['John', 20, 'john@gmail.com']
# anna = ['Anna', 35, 'anna@gmail.com']
# jake = ['Jake', 24, 'jake@gmail.com']
# x = 5
#
# print(type(username))
# print(type(x))
# print(type(john))
from datetime import datetime


# class PersonForMars:
#     pass
#
#
# def get_user_by_username():
#     pass
#
#
# class GetUserByUsername:
#     pass
# class User:
#     pass
#
#
# obj1 = User()
# obj1.username = 'John'
# obj1.age = 24
# obj1.weight = '80 kg'
# print(obj1.age)

# class Person:
#     def __init__(self, username, age, weight, password):
#         self.username = username
#         self.age = age
#         self.weight = weight
#
#     def get_info(self):
#         print(f'Assalomu aleykum Mening ismim {self.username}.\nYoshim {self.age}')
#
#     def get_age(self):
#         return f'{self.age} years old'
#
#
# khabib = Person("Khabib", '40', "normal")
# # khabib.password = '123'
# igor = Person(username='Igor', weight='-24', age=10000000000000000000000000000)
#
# print(igor.get_age())

class Car:
    def __init__(self, model, brand, color, price, created_at):
        self.model = model
        self.brand = brand
        self.color = color
        self.price = price
        self.created_at = created_at

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def display(self):
        return f'{self.model} - {self.brand} - {self.color}'


# bmw = Car('Bmw', 'X7', 'black', 20_000, '2020-03-14')
# print(bmw.get_price())
# bmw.set_price(15_000)
#
# bmw = Car(model, brand, color, price, created_at)
# print(bmw.get_color())


# del user

# Animal  => attribute => name , age , id , passport,voice
# Animal  => method => sound() => "Woof Woof"  , "Meow Meow" , "Quack, Quack"
