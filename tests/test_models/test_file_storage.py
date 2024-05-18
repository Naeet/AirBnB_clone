import unittest
import os
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_empty(self):
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 0)

    def test_new_save(self):
        obj = {"id": "test_id"}
        self.storage.new(obj)
        self.storage.save()
        all_objs = self.storage.all()
        self.assertIn("BaseModel.test_id", all_objs)

    def test_reload(self):
        obj_id = "test_id"
        obj = {"id": obj_id}
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertIn("BaseModel.test_id", all_objs)

if __name__ == "__main__":
    unittest.main()
