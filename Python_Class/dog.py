class Dog: # Define class
    """ A simple attempt to model a dog."""
    # Method
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    # Method
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    # Method
    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")


# Creating Instance
my_dog = Dog('While', 6)
your_dog = Dog('Lucy', 8)
print(f"My dog name is {my_dog.name}")
print(f"My dog is {my_dog.age} year old")

"""Using Dot notation call any method"""
my_dog.sit()
my_dog.roll_over()
print('\n')
print(f"Your dog name is {your_dog.name}")
print(f"Your dog is {your_dog.age} year old")

"""Using Dot notation call any method"""
your_dog.sit()
your_dog.roll_over()