from todoitem import *

class TodoList():

    def __init__(self):
        self.items = []

    def add_item(self, name, description):
        self.items.append(TodoItem(name, description))

    def delete_item(self, idx):
        del self.items[idx]

    def mark_item_as_done(self, idx):
        self.items[idx].is_done = True

    def display_todolist(self):
        for i in range(0,len(self.items)):
            self.display_todoitem_by_id(i)

    def display_todoitem_by_id(self, idx):
        done = "done" if self.items[idx].is_done else "not done"
        print(" %u  %s, %s (%s)" % (idx + 1, self.items[idx].name, self.items[idx].description, done))
