class User:
    def __init__(self, name):
        self.name = name 

    def get_profile(self):
        return f"Name : {self.name}"