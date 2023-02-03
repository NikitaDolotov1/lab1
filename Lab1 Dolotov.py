class math:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def addition(self):
        return a + b

    def multiplikation(self):
        return a * b

    def division(self):
        return a / b

    def subtraction(self):
        return a - b

a = int(input("Введите A: "))
b = int(input("Введите B: "))
ab = math(a,b)



c = input("Выберите знак: ")

if c == "+":
    print(ab.addition())

if c == "*":
    print(ab.multiplikation())

if c == "/":
    print(ab.division())

if c == "-":
    print(ab.subtraction())
