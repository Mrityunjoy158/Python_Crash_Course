# Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user's information. Make another method called greet_user() that prints a personalized greeting to the user.

# Create several instances representing different users, and call both methods for each user

class User:
    """Represent user profile"""
    def __init__(self, first_name, last_name, email, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.location = location

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"Nomoskar {self.first_name} {self.last_name}")

# Creating Instance
first_user = User('Mrityunjoy', 'Bhaduree', 'mrityunjoy@gmail.com', 28, 'Mirpur-2')
first_user.describe_user()
first_user.greet_user()

print('\n')

second_user = User('Rumpa', 'Bhaduree', 'rumpa@gmail.com', 27, 'Mirpur-2')
second_user.describe_user()
second_user.greet_user()