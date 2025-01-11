#Object = A "bundle" of related attributes (variables) and methods
# (functions)
# ex: phone, cup, book
# You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object
from car import Car

car1 = Car("Mustang", 2024, "red", False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
print()
car1.drive()
car1.stop()
car1.describe()
print()

car2 = Car("Corvette", 2025, "blue", True)

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
print()
car2.drive()
car2.stop()
car2.describe()
print()

car3 = Car("Charger", 2026, "yellow", True)

print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)
print()
car3.drive()
car3.stop()
car3.describe()
print()