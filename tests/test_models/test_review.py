import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_attributes(self):
        """Test Review attributes"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_instance(self):
        """Test instance creation"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)

if __name__ == '__main__':
    unittest.main()
