# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indi-
# cating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attri-
# butes individually, and then call both methods.

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restauurant name is {self.restaurant_name}")
        print(f"{self.cuisine_type} type of cuisine")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open")


restaurant = Restaurant('Food Ranger', 'Italian cuisine')
print(f"Restauurant name is {restaurant.restaurant_name}")
print(f"{restaurant.cuisine_type} type of cuisine")
print('\n')
restaurant.describe_restaurant()
restaurant.open_restaurant()