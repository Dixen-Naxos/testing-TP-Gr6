from datetime import datetime, timedelta
from customemailservice import CustomEmailService
from item import Item


class ToDoList:
    def __init__(self, parent):
        self.items = []
        self.last_insert_date = datetime.now() - timedelta(minutes=30)
        self.parent = parent
        self.custom_email_service = CustomEmailService()

    def checkNameUnicity(self, name):
        return any(item.name == name for item in self.items)

    def add(self, name, content):
        if len(content) > 1000:
            return False
        elif not name or self.checkNameUnicity(name):
            return False
        elif datetime.now() - timedelta(minutes=30) < self.last_insert_date:
            return False
        else:
            self.items.append(Item(name, content))
            self.last_insert_date = datetime.now()
            if len(self.items) == 8:
                self.custom_email_service.sendMail(self.parent.email)
            return True
