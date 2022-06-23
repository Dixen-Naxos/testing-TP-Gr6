import unittest
from datetime import datetime, timedelta

from user import User


class UserTest(unittest.TestCase):

    def testCorrectUser(self):
        user = User(datetime.now() - timedelta(weeks=20 * 52), "toto@gmail.com", "Armand", "Dailly", "teeeeeeest")
        self.assertIsInstance(user, User)

    def testIncorrectMail(self):
        user = User(datetime.now() - timedelta(weeks=20 * 52), "toto", "Armand", "Dailly", "teeeeeeest")
        self.assertNotIsInstance(user, User)

    def testTooShortPassword(self):
        user = User(datetime.now() - timedelta(weeks=20 * 52), "toto@gmail.com", "Armand", "Dailly", "test")
        self.assertNotIsInstance(user, User)

    def testTooLongPassword(self):
        user = User(datetime.now() - timedelta(weeks=20 * 52), "toto@gmail.com", "Armand", "Dailly", "t" * 50)
        self.assertNotIsInstance(user, User)

    def testTooYoung(self):
        user = User(datetime.now() - timedelta(weeks=4 * 52), "toto", "Armand", "Dailly", "teeeeeeest")
        self.assertNotIsInstance(user, User)

    def testValidCreationToDoList(self):
        user = User(datetime.now() - timedelta(weeks=20 * 52), "toto@gmail.com", "Armand", "Dailly", "teeeeeeest")
        self.assertTrue(user.createToDoList())

    def testInvalidCreationToDoList(self):
        user = User(datetime.now() - timedelta(weeks=20 * 52), "toto@gmail.com", "Armand", "Dailly", "teeeeeeest")
        user.createToDoList()
        self.assertFalse(user.createToDoList())