from .car.car import Car, Bus, Truck

car_1 = Car("black", "BMW")
print(car_1.color)
car_1.drive_to("Каракол")
car_1.change_color("blue")
# car_1.color = "blue"
print(car_1.color)
bus_42 = Bus("red", "Mercedes", "42")
print(bus_42.model, bus_42.number)
bus_42.drive_to("Бишкек")
truck_1 = Truck("silver", "Mercedes")
print(type(bus_42))
print(isinstance(bus_42, Bus))
print(isinstance(bus_42, Car))

# car_1.drive_to("Osh")
# bus_42.drive_to("Osh")
# truck_1.drive_to("Osh")
vehicles = [car_1, bus_42, truck_1]
for v in vehicles:
    v.drive_to("Karakol")
