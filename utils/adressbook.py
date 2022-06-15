class AddressBook:
    def __init__(self, fullname, phone):
        self.fullname = fullname
        self.phone = phone

    def add_new_phone(self, phone):
        self.phone = phone
