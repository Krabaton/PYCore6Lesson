class AddressBook:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'AddressBook({self.name})'
