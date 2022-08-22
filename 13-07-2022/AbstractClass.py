from abc import ABC,abstractmethod
class Parent(ABC):
    @abstractmethod
    def info(self):
        print('this is parent info')
        
    @abstractmethod
    def details(self):
        print('this is parent details')
   
    def salary(self):
        print('this is parent salary')


class Child(Parent,ABC):
    @abstractmethod
    def info(self):
        print('this is child info')


class Grandson(Child):
    def details(self):
        print('this is grandson details')

    def info(self):
        print('this is granson info')

        
obj = Child()
obj.info()

