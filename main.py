from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10:
            raise PhoneLenError("Phone number less or bigger than 10 digits")
        if not value.isdigit():
            raise PhoneDigitError("Phone number contains not only digits")
        else:
            self.value = value
        
class PhoneLenError(Exception):
    pass

class PhoneDigitError(Exception):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones: list(Phone) = []

    def add_phone(self, phone: str):
        try:
            self.phones.append(Phone(phone))
        except (PhoneLenError, PhoneDigitError) as e:
            print(e)
      
    def remove_phone(self, del_phone : str):
            if self.find_phone(del_phone) != None:
                self.phones.remove(self.find_phone(del_phone))
            else:
                print("This phone isn't exists!")
                
    def edit_phone(self, old_phone : str, new_phone : str):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)
    
    def find_phone(self, find_phone):
        for phone in self.phones:
            if phone.value == find_phone:
                return phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
                
    def add_record(self, record : Record):
        self.data[record.name.value] = record

    def find(self, name):
        self.name = name
        if name in self.data:
            return self.data.get(name)
        else:
            return None
        
    def delete(self, name):
        del self.data[name]

    def __str__(self):
        return "\n".join([str(record) for record in self.data.values()])



# Створення нової адресної книги

book = AddressBook()

# Створення запису для John

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги

book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі

print(book)

# Знаходження та редагування телефону для John

john = book.find("John")
john.edit_phone("1234567890", "1112223333")
john.remove_phone("1112223333")
print(john)


# Видалення запису Jane
book.delete("Jane")

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555


