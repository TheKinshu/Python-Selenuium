# Creating Class
class Calculator:
    num  = 100

    # Default Contructor
    def __init__(self, a, b):
        self.firstNum = a
        self.secondNum = b
        print('I am called automatically when object is created')

    def getData(self):
        print("I amn now executing as method in class")
    
    # Calculating the sun of 3 numbers
    def getSum(self):
        return self.firstNum + self.secondNum + Calculator.num
