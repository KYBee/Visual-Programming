class Calc:

    def __init__(self, number = 0):
        self.value = number

    def setvalue(self, number):
        self.value = number

    def getvalue(self):
        return self.value

    def add(self, number):
        self.value = self.value + number

    def minus(self, number):
        self.value = self.value - number

    def print(self):
        print(self.value)

cal1 = Calc()
cal2 = Calc(5)
cal1.setvalue(10)
cal1.add(20)
cal1.minus(5)
cal1.print()
cal2.add(cal1.getvalue())
cal2.print()