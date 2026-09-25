class CPU:

    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print("CPU:", self.brand)

class RAM:

    def __init__(self, size):
        self.size = size

    def show(self):
        print("RAM:", self.size, "GB")

class Computer:

    def __init__(self, cpu, ram):
        self.cpu = CPU(cpu)
        self.ram = RAM(ram)

    def show(self):
        self.cpu.show()
        self.ram.show()

pc = Computer("Ryzen 7", 16)

pc.show()