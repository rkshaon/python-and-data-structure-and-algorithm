class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def drive(self):
        print("The car is driving.")
        
my_car = Car("Toyota", "Corolla", 2020)

print(my_car.make)   # Output: "Toyota"

my_car.drive()   # Output: "The car is driving."

my_car2 = Car("BMW", "760i xDrive Sedan", 2023)
# print(my_car2)
print(f"Car: {my_car2.make}, Model: {my_car2.model}, Year: {my_car2.year}")
my_car2.drive()