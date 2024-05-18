import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def test_attributes(self):
        """Test City attributes"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_instance(self):
        """Test instance creation"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)

if __name__ == '__main__':
    unittest.main()
