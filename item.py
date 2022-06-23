from datetime import datetime


class Item:
    def __init__(self, name, content):
        self.name = name
        self.content = content
        self.creation_date = datetime.now()
