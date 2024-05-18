import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_instance_creation(self):
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_attributes(self):
        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_to_dict(self):
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertTrue('created_at' in user_dict)
        self.assertTrue('updated_at' in user_dict)
        self.assertTrue('id' in user_dict)
        self.assertTrue('email' in user_dict)
        self.assertTrue('password' in user_dict)
        self.assertTrue('first_name' in user_dict)
        self.assertTrue('last_name' in user_dict)

    def test_str_representation(self):
        string = str(self.user)
        self.assertIsInstance(string, str)
        self.assertEqual(string[:6], "[User]")
        self.assertIn("'id':", string)
        self.assertIn("'created_at':", string)
        self.assertIn("'updated_at':", string)
        self.assertIn("'email':", string)
        self.assertIn("'password':", string)
        self.assertIn("'first_name':", string)
        self.assertIn("'last_name':", string)

if __name__ == '__main__':
    unittest.main()
