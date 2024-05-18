import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def test_attributes(self):
        """Test Amenity attributes"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_instance(self):
        """Test instance creation"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

if __name__ == '__main__':
    unittest.main()
