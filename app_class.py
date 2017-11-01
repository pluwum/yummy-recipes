"""Contains the User and Recipe classes"""

class User():
    """Handles the registration and logging in of users

    Parameters:
    - email: Holds the e-mail address the user uses to register
      and log into the application
    - password: Holds the password the user submits during registration
      and logging into the application"""

    def __init__(self):
        self.user_db = {}

    def register_user(self, email, password, confirm_password):
        """Method to handle registration of users.
        - email: Holds the user's entered e-mail address.
        - password: Holds the user's entered password.
        - confirm_password: Holds the second entry of the password
          by the user."""
        if email in self.user_db:
            return "You're already registered. Try logging in."
        else:
            if password != confirm_password:
                return "Sorry, the two passwords don't match. Try again. "
            elif email != None and password != None:
                self.user_db.update({email: password})

    def login_user(self, email, password):
        """Method to handle logging in of users.
        - email: Holds the user's entered e-mail address.
        - password: Holds the user's entered password"""
        if email in self.user_db and self.user_db[email] != password:
            return "You have entered the e-mail and/or wrong password. Please try again."
        elif email in self.user_db and self.user_db[email] == password:
            return "Welcome. You've successfully logged in."
        else:
            return "Are you sure you have an account with us?\n Please try registering."

class Recipe():
    """This class contains the methods for interacting with the users'
    Recipes """
    def __init__(self):
        pass

    def create_recipe_category(self, parameter_list):
        """This method creates a recipe category"""
        pass

    def delete_recipe_category(self):
        """This method deletes a recipe category"""
        pass

    def view_recipe_category(self, key, recipe_value):
        """This method views a recipe category"""
        pass

    def update_recipe_category(self, key, new_key, recipe_value):
        """This method updates a recipe category"""
        pass

    def add_recipe(self):
        """This method adds a recipe to a category"""
        pass

    def view_recipe(self):
        """This method views recipes in a category"""
        pass

    def delete_recipe(self):
        """This method deletes recipes from a category"""
        pass

    def update_recipe(self):
        """This method updates recipes from a category"""
        pass
        