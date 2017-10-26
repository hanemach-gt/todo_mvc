from todoitem import *

class TodoList():

    def __init__(self):
        self.items = []

    def add_item(self, name, description):
        self.items.append(TodoItem(name, description))

    def delete_item(self, identifier):
        del self.items[identifier - 1]

    def mark_item_as_done(self, identifier):
        self.items[identifier - 1].set_done()

    def display_todolist(self):
        for i in range(1,len(self.items) + 1):
            self.display_todoitem_by_id(i)

    def display_todoitem_by_id(self, identifier):
        print(" %u  %s" % (identifier, self.items[identifier - 1].name))
