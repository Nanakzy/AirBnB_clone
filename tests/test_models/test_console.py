#!/usr/bin/python3

import unittest
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up method to initialize FileStorage instance"""
        self.storage = FileStorage()

    def test_reload_no_file(self):
        """Test reload method when file doesn't exist"""
        self.storage.reload()  # This should not raise any errors

    def test_reload_with_file(self):
        """Test reload method with existing file"""
        # Prepare a sample data file
        sample_data = {
            "User.1234":
            {"id": "1234", "email": "test@example.com", "password": "password"}
            # Add more sample data as needed
        }
        with open(self.storage._FileStorage__file_path, 'w') as f:
            json.dump(sample_data, f)

        # Reload data
        self.storage.reload()

        # Check if the User object was loaded correctly
        self.assertTrue("User.1234" in self.storage.all())
        user_obj = self.storage.all()["User.1234"]
        self.assertIsInstance(user_obj, User)
        self.assertEqual(user_obj.id, "1234")
        self.assertEqual(user_obj.email, "test@example.com")
        self.assertEqual(user_obj.password, "password")

    def tearDown(self):
        """Tear down method to clean up after each test"""
        try:
            os.remove(self.storage._FileStorage__file_path)
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
