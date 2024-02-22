# class Device:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def get_info(self):
#         return f"{self.brand} {self.model}"

# class CoffeeMachine(Device):
#     def __init__(self, brand, model, coffee_type):
#         super().__init__(brand, model)
#         self.coffee_type = coffee_type

#     def make_coffee(self):
#         return f"Making {self.coffee_type} coffee with {self.get_info()}"

# class Blender(Device):
#     def __init__(self, brand, model, speed_levels):
#         super().__init__(brand, model)
#         self.speed_levels = speed_levels

#     def blend(self, ingredient):
#         return f"Blending {ingredient} with {self.get_info()} at {self.speed_levels} speed levels"

# class MeatGrinder(Device):
#     def __init__(self, brand, model, power):
#         super().__init__(brand, model)
#         self.power = power

#     def grind_meat(self, meat_type):
#         return f"Grinding {meat_type} with {self.get_info()} at {self.power} watts"



# if __name__ == "__main__":
#     coffee_machine = CoffeeMachine("BrandA", "ModelX", "Espresso")
#     print(coffee_machine.make_coffee())

#     blender = Blender("BrandB", "ModelY", 3)
#     print(blender.blend("Fruits"))

#     meat_grinder = MeatGrinder("BrandC", "ModelZ", 800)
#     print(meat_grinder.grind_meat("Beef"))













# class Ship:
#     def __init__(self, name, displacement):
#         self.name = name
#         self.displacement = displacement

#     def get_info(self):
#         return f"{self.name} - Displacement: {self.displacement} tons"

# class Frigate(Ship):
#     def __init__(self, name, displacement, missile_system):
#         super().__init__(name, displacement)
#         self.missile_system = missile_system

#     def launch_missile(self):
#         return f"Launching missiles from {self.missile_system} on {self.get_info()}"

# class Destroyer(Ship):
#     def __init__(self, name, displacement, artillery_guns):
#         super().__init__(name, displacement)
#         self.artillery_guns = artillery_guns

#     def fire_artillery(self):
#         return f"Firing artillery guns on {self.get_info()}"

# class Cruiser(Ship):
#     def __init__(self, name, displacement, radar_system):
#         super().__init__(name, displacement)
#         self.radar_system = radar_system

#     def operate_radar(self):
#         return f"Operating radar system on {self.get_info()}"

# if __name__ == "__main__":
#     frigate_ship = Frigate("FrigateA", 2000, "Aegis")
#     print(frigate_ship.launch_missile())

#     destroyer_ship = Destroyer("DestroyerX", 3500, "5-inch guns")
#     print(destroyer_ship.fire_artillery())

#     cruiser_ship = Cruiser("CruiserZ", 5000, "Phased Array Radar")
#     print(cruiser_ship.operate_radar())













# class Square:
#     def __init__(self, side_length):
#         self.side_length = side_length

#     def calculate_area(self):
#         return self.side_length ** 2

# class CircleInSquare(Square):
#     def __init__(self, side_length):
#         super().__init__(side_length)

#     def calculate_radius(self):
#         return self.side_length / 2

#     def calculate_circle_area(self):
#         radius = self.calculate_radius()
#         return 3.14 * radius ** 2



# if __name__ == "__main__":
#     square = Square(4)
#     print(f"Square Area: {square.calculate_area()}")

#     circle_in_square = CircleInSquare(4)
#     print(f"Circle Radius: {circle_in_square.calculate_radius()}")
#     print(f"Circle Area inscribed in the Square: {circle_in_square.calculate_circle_area()}")











# class Wheels:
#     def __init__(self, number_of_wheels):
#         self.number_of_wheels = number_of_wheels

#     def rotate(self):
#         return "Wheels are rotating"

# class Engine:
#     def __init__(self, fuel_type):
#         self.fuel_type = fuel_type

#     def start(self):
#         return "Engine started"

# class Doors:
#     def __init__(self, number_of_doors):
#         self.number_of_doors = number_of_doors

#     def open(self):
#         return "Doors opened"

# class Car(Wheels, Engine, Doors):
#     def __init__(self, brand, model, fuel_type, number_of_wheels, number_of_doors):
#         Wheels.__init__(self, number_of_wheels)
#         Engine.__init__(self, fuel_type)
#         Doors.__init__(self, number_of_doors)
#         self.brand = brand
#         self.model = model

#     def drive(self):
#         return "Car is driving"

# if __name__ == "__main__":
#     car = Car(brand="Toyota", model="Camry", fuel_type="Gasoline", number_of_wheels=4, number_of_doors=4)
#     print(car.drive())
#     print(car.rotate())
#     print(car.start())
#     print(car.open())







