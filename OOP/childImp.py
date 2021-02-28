from oop1 import Calculator

class childImp(Calculator):
    num2 = 200

    # Child calling parent constructor 
    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.getSum()

obj = childImp()
print(obj.getCompleteData())