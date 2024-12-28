

from re import X
from tkinter import Y


class calculator : 
    x = 0 
    y = 0 

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def addition(self):
        return self.x + self.y
    def substaction(self):
        return self.x - self.y
    def multiplication(self):
        return self.x * self.y
    def division(self):
        return self.x / self.y

C_Object = calculator(4,5)
print(C_Object)


