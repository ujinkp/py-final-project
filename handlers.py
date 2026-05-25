from models import Record, AddressBook, NoteBook, Note

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e: return str(e)
        except IndexError: return "Enter the required information."
        except KeyError: return "Not found."
    return inner

# --- Команди для контактів ---

@input_error
def add_contact(args, book: AddressBook):
    name, phone = args[0], args[1]
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
    record.add_phone(phone)
    return "Contact added."

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    raise KeyError

@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return f"{name}'s birthday is on {record.birthday.value}"
    raise KeyError

@input_error
def birthdays(args, book: AddressBook):
    # Використовуємо функцію з logic.py (переконайтеся, що імпортували її)
    from logic import get_upcoming_birthdays
    upcoming = get_upcoming_birthdays(book)
    if not upcoming: return "No birthdays next week."
    return "\n".join([f"{u['name']}: {u['congratulation_date']}" for u in upcoming])

@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return "Contact updated."
    raise KeyError

@input_error
def show_phone(args, book: AddressBook):
    record = book.find(args[0])
    return "; ".join([p.value for p in record.phones]) if record else "Not found."

@input_error
def show_all_contacts(book: AddressBook):
    return "\n".join([str(r) for r in book.data.values()]) if book.data else "Address book is empty."

@input_error
def delete_contact(args, book: AddressBook):
    book.delete(args[0])
    return f"Contact '{args[0]}' deleted."


# --- Команди для нотаток (працюють з NoteBook) ---

@input_error
def add_note(args, notes: NoteBook):
    # args тепер містить все після "add-note"
    #  останній аргумент — це завжди теги
    if len(args) < 3:
        raise ValueError("Usage: add-note [title] [content] [tags_comma_separated]")
    
    title = args[0]
    tags = args[-1].split(',')
    content = " ".join(args[1:-1])
    
    notes.add_note(Note(title, content, tags))
    return f"Note '{title}' added."


@input_error
def find_notes_by_tag(args, notes: NoteBook):
    # Використовуємо функцію з logic.py
    from logic import sort_notes_by_tag
    tag = args[0]
    found = sort_notes_by_tag(notes, tag)
    return "\n".join([str(n) for n in found]) if found else "No notes found."

@input_error
def delete_note(args, notes: NoteBook):
    title = args[0]
    notes.delete_note(title)
    return f"Note '{title}' deleted."