from abc import ABC, abstractmethod

class Tyre(ABC):
    @abstractmethod
    def car(self):
        print("MRF")


class MyClass(Tyre):

    def car(self):
        super().car()
        print("BMW")

try :
    a = Tyre()
    a.car()
except Exception as err :
    print (err)

b = MyClass()
b.car()
