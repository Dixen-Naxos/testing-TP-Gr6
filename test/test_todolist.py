import unittest
from datetime import datetime, timedelta
from unittest.mock import MagicMock

from user import User


class ToDoListTest(unittest.TestCase):

    def testCorrectItem(self):
        user = User(datetime.now() - timedelta(weeks=20 * 52), "toto@gmail.com", "Armand", "Dailly", "teeeeeeest")
        user.createToDoList()
        self.assertTrue(user.toDoList.add("test", "test"))

    def testNotUniqueName(self):
        user = User(datetime.now() - timedelta(weeks=20 * 52), "toto@gmail.com", "Armand", "Dailly", "teeeeeeest")
        user.createToDoList()
        user.toDoList.add("test", "test")
        user.toDoList.last_insert_date = datetime.now() - timedelta(minutes=31)
        self.assertFalse(user.toDoList.add("test", "test"))

    def testIncorrectContentLength(self):
        user = User(datetime.now() - timedelta(weeks=20 * 52), "toto@gmail.com", "Armand", "Dailly", "teeeeeeest")
        user.createToDoList()
        self.assertFalse(user.toDoList.add("test", "test" * 300))

    def testMail8Items(self):
        user = User(datetime.now() - timedelta(weeks=20 * 52), "toto@gmail.com", "Armand", "Dailly", "teeeeeeest")
        user.createToDoList()
        user.toDoList.custom_email_service.sendMail = MagicMock(return_value=True)
        for i in range(7):
            user.toDoList.add("test" + str(i), "test")
            user.toDoList.last_insert_date = datetime.now() - timedelta(minutes=31)
        self.assertTrue(user.toDoList.add("test" + str(99), "test"))
