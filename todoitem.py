class TodoItem():

    def __init__(self, name = "", description = "", is_done = False):
        self.name = name
        self.description = description
        self.is_done = is_done

    def set_name(self, name):
        self.name = name

    def set_desc(self, description):
        self.description = description

    def set_done(status = True):
        self.is_done = status
