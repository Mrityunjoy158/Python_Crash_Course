class Car:
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reaading = 0

    def get_descriptive_name(self):
        """ Return a neatly formatted ddescriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reaading} miles on it")

    # Modifying an Attribute’s Value Through a Method
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reaading:
            self.odometer_reaading = mileage
        else:
            print("You can' roll back an odometer!")

    def increment_odometer(self, miles):
        """Add thee given amount to the odometer reading"""
        self.odometer_reaading += miles
    
# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())

# #Modifying an Attribute’s Value Directly
# # my_new_car.odometer_reaading = 23

# #Modifying an Attribute’s Value Through a Method
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()