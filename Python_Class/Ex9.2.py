# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

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
restaurant1 = Restaurant('Food Ranger1', 'Italian cuisine1')
restaurant2 = Restaurant('Food Ranger2', 'Italian cuisine2')

restaurant.describe_restaurant()
print('\n')
restaurant1.describe_restaurant()
print('\n')
restaurant2.describe_restaurant()