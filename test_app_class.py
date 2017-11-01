"""Unittests for the User and Recipe classes"""
from unittest import TestCase
from app_class import Category, Recipe, User

class UserTestCase(TestCase):
    """This is an instance of the Test Case class
    that will be used in testing the User class in
    app_class.py"""
    def setUp(self):
        self.user = User()

    def test_register_user(self):
        """A method to test the accuracy of the
        register_user method in the User class"""
        email = "iseeyou@xyz.com"
        password = "somepassword"
        confirm_password = "somepassword"
        self.user.register_user(email, password, confirm_password)
        self.assertTrue(email in self.user.user_db, msg="No e-mail address entered")
        self.assertTrue(self.user.user_db[email], msg="No password given")
        self.assertEqual(self.user.user_db[email], password,
                         msg='User e-mail address and password not successfully associated')
        self.assertIn(email, self.user.user_db,
                      msg='E-mail address not added to user entries')

    def test_login_user(self):
        """A method to test the accuracy of the
        login_user method in the User class"""
        email = "iseeyou@xyz.com"
        password = "somepassword"
        self.user.user_db.update({email: password})
        self.assertEqual(self.user.user_db[email], password, msg='Invalid user password')

    class CategoryTestCase(TestCase):
        """This is an instance of the Test Case class
        that will be used in testing the Category class
        in app_class.py"""
        def setUp(self):
            self.test_category = Category()

        def test_create_recipe_category(self, category):
            """A method to test the create_recipe_category method
            in the Category class
            - category: a recipe category to be entered"""
            category = "something"
            self.test_category.create_recipe_category(category)
            self.assertTrue(category in self.test_category.categories,
                            msg="category not entered into category list")

        def test_delete_recipe_category(self, category):
            """A method to test the delete_recipe_category
            method in the Recipe class"""
            category = "something"
            self.test_category.delete_recipe_category(category)
            self.assertFalse(category in self.test_category.categories,
                             msg="Category not deleted")

        def test_update_recipe_category(self):
            """A method to test the update_recipe_category method
            in the Recipe class"""
            pass

        def test_view_recipe_category(self):
            """A method to test the view_recipe_category method
            in the Recipe class"""
            pass

    class RecipeTestCase(TestCase):
        """This is an instance of the Test Case class
        that will be used in testing the Recipe class
        in app_class.py"""
        pass
