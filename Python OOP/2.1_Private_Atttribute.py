class Profile:
    def __init__(self, name, id):
        self.name = name
        self.__id = id      # private

p = Profile("Alif", 123)
print(p.name)
print( )
print(p.__id)