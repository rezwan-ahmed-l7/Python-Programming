class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def show(self):
        print(self.real, "i +", self.imag, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImag = self.imag + num2.imag
        return Complex(newReal, newImag)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImag = self.imag - num2.imag
        return Complex(newReal, newImag)

num1 = Complex(3, 4)
num1.show()

num2 = Complex(5, 6)
num2.show()

num3 = num1 + num2
num3.show()

num4 = num1 - num2
num4.show()
        