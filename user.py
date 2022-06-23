import re
from datetime import date

from todolist import ToDoList


def checkMail(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, email):
        return True
    return False


def checkAge(birthday):
    today = date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    if age >= 13:
        return True
    return False


def checkPassword(password):
    return 8 < len(password) < 40


def isValid(email, birthday, password):
    if checkMail(email) and checkAge(birthday) and checkPassword(password):
        return True
    return False


class User:
    def __new__(cls, birthday, email, firstname, lastname, password):
        if isValid(email, birthday, password):
            return object.__new__(cls)

    def __init__(self, birthday, email, firstname, lastname, password):
        self.birthday = birthday
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.toDoList = None

    def createToDoList(self):
        if self.toDoList is None:
            self.toDoList = ToDoList(self)
            return True
        else:
            return False
