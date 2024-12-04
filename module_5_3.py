class House:
    def __init__(self,name, floors):
        self.floors = floors
        self.name = name
    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors != other.floors
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, int):
            self.floors += value
            return self
        return NotImplemented

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __repr__(self):
        return f"{self.name}, этажей: {self.floors}"


house1 = House('ЖК Мечта', 10)
house2 = House('ЖК Надежда', 20)

print(house1)
print(house2)
print(house1 <= house2)
print(house1 > house2)
print(house1 == house2)
print(house1 >= house2)
house1 = house1 + 10
print(house1 <= house2)
print(house1 > house2)
print(house1 == house2)
print(house1 >= house2)
house2 = house2 + 7
print(house2)
print(house1 <= house2)
print(house1 > house2)
print(house1 == house2)
print(house1 >= house2)


