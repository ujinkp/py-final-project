from collections import UserDict
from datetime import datetime, timedelta
from validators import validate_phone, validate_email, validate_date, validate_not_empty, check_or_raise

class Field:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        check_or_raise(validate_not_empty, value, "Name cannot be empty.")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        check_or_raise(validate_phone, value, "Phone number must contain 10 digits.")
        super().__init__(value)

class Email(Field):
    def __init__(self, value):
        check_or_raise(validate_email, value, "Invalid email format.")
        super().__init__(value)

class Address(Field):
    def __init__(self, value):
        check_or_raise(validate_not_empty, value, "Address cannot be empty.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        check_or_raise(validate_date, value, "Invalid date format. Use DD.MM.YYYY")
        self.value = datetime.strptime(value, "%d.%m.%Y").date()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.address = None

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def edit_phone(self, old_number, new_number):
        for i, phone in enumerate(self.phones):
            if phone.value == old_number:
                self.phones[i] = Phone(new_number)
                return
        raise ValueError(f"Phone {old_number} not found.")    

    def remove_phone(self, phone_number):
        """Видаляє номер телефону з запису."""
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return
        raise ValueError(f"Phone {phone_number} not found.")    
    
    def add_email(self, email):
        self.email = Email(email)

    def edit_email(self, new_email):
        self.email = Email(new_email)

    def add_address(self, address):
        self.address = Address(address)

    def edit_address(self, new_address):
        self.address = Address(new_address)    

    def add_birthday(self, birthday_value):
        self.birthday = Birthday(birthday_value)

    def __str__(self):
        res = [f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"]
        if self.email: res.append(f"email: {self.email}")
        if self.address: res.append(f"address: {self.address}")
        if self.birthday: res.append(f"birthday: {self.birthday}")
        return ", ".join(res)

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError(f"Contact {name} not found.")
        

        #Нотатки

class Note:
    def __init__(self, title, content, tags=None):
        self.title = title.strip()
        self.content = content
        self.tags = tags if tags else []

    def __str__(self):
        tags_str = ", ".join(self.tags)
        return f"Title: {self.title}\nContent: {self.content}\nTags: [{tags_str}]"

class NoteBook(UserDict):
    def add_note(self, note):
        # Додаємо перевірку, чи не існує вже нотатка з таким заголовком
        if note.title in self.data:
            raise ValueError(f"Note with title '{note.title}' already exists.")
        self.data[note.title] = note

    def search_notes_by_tag(self, tag):
        tag = tag.lower()
        return [n for n in self.data.values() if tag in [t.lower() for t in n.tags]]

    def delete_note(self, title):
        if title in self.data:
            del self.data[title]
        else:
            raise KeyError(f"Note '{title}' not found.")
            
    def edit_note(self, title, new_content=None, new_tags=None):
        if title in self.data:
            if new_content: 
                self.data[title].content = new_content
            if new_tags: 
                self.data[title].tags = new_tags
        else:
            raise KeyError(f"Note '{title}' not found.")