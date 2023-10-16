import json
import os
import unittest

from user_class import User, load_json, save_json
from user_logger import Logger


class TestUserClass(unittest.TestCase):
    def setUp(self):
        self.id_ = 1
        self.name = 'YodaXD'
        self.level = 7
        self.user_data = {str(self.id_): {'name': self.name, 'level': self.level}}

    def tearDown(self):
        if os.path.exists('test_json.json'):
            os.remove('test_json.json')
        if os.path.exists('test_logger.json'):
            os.remove('test_logger.json')

    def test_user_creation(self):
        user = User(self.name, self.id_, self.level)
        self.assertEqual(user.name, self.name)
        self.assertEqual(user.id_, self.id_)
        self.assertEqual(user.level, self.level)

    def test_invalid_user_creation(self):
        with self.assertRaises(ValueError):
            User(self.level, self.id_, self.name)

    def test_successful_user_level_creation(self):
        loger = Logger('test_logger.json')
        loger.__class__.db[str(self.id_)] = {'name': self.name, 'level': self.level}
        loger.__class__.users[self.id_] = User(self.name, self.id_, self.level)
        loger.authorize(self.id_, self.name)
        new_level = self.level - 1 if self.level - 1 > 0 else 1
        new_user = loger.create_user('new_' + self.name, self.id_ + 1, new_level)
        self.assertEqual(new_user.level, new_level)

    def test_invalid_user_level_creation(self):
        with self.assertRaises(ValueError):
            loger = Logger('test_logger.json')
            loger.__class__.db[str(self.id_)] = {'name': self.name, 'level': self.level}
            loger.__class__.users[self.id_] = User(self.name, self.id_, self.level)
            loger.authorize(self.id_, self.name)
            new_level = self.level
            new_user = loger.create_user('new_' + self.name, self.id_ + 1, new_level)
            self.assertEqual(new_user.level, new_level)

    def test_successful_authorize(self):
        loger = Logger('test_logger.json')
        loger.__class__.db[str(self.id_)] = {'name': self.name, 'level': self.level}
        loger.__class__.users[self.id_] = User(self.name, self.id_, self.level)
        loger.authorize(self.id_, self.name)

    def test_invalid_authorize(self):
        with self.assertRaises(PermissionError):
            loger = Logger('test_logger.json')
            loger.authorize(self.id_ * 10, self.name)
        with self.assertRaises(PermissionError):
            loger = Logger('test_logger.json')
            loger.authorize(self.id_, self.name * 10)

    def test_load_json(self):
        with open('test_json.json', 'w', encoding='UTF-8') as file:
            json.dump(self.user_data, file)

        loaded_data = load_json('test_json.json')
        self.assertEqual(loaded_data, self.user_data)

    def test_save_json(self):
        user_db = self.user_data
        save_json('test_json.json', user_db)
        with open('test_json.json', 'r', encoding='UTF-8') as file:
            saved_data = json.load(file)
        self.assertEqual(saved_data, user_db)


if __name__ == '__main__':
    unittest.main()
