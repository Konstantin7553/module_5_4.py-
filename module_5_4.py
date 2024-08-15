class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        if args:
            cls.houses_history.append(args[0])
        return instance

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def __del__(self):
        print(f"{self.name} снесен, но он останется в истории")

    def __str__(self):
        return f"Название: {self.name}, кло-во этажей: {self.number_of_floor}"


h = House("ЖК Эльбрус", 10)
print(House.houses_history)
h1 = House("Домик в деревне", 3)
print(House.houses_history)
h2 = House("ЖК Город", 20)
print(House.houses_history)

del h1
del h2

print(House.houses_history)
