class Member:

    def __init__(self, first_name, last_name, dob, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.full_name = first_name + last_name
        self.id = id