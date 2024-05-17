from abc import ABC, abstractmethod


class Car(ABC):

     @abstractmethod
     def start(self):
        pass
     @abstractmethod
     def stop(self):
         pass

     def get_brand(self):
         print('Get brand')

     def get_magnitafon(self):
         print('Get magnitafon')



abstract_obj = Car()
abstract_obj.get_brand()



class UzbCar(Car):

     def start(self):
         print('Starting')

     def stop(self):
        print('Stopping')

     def say(self):
         print('hi')


obj1 = UzbCar()
obj1.get_brand()
