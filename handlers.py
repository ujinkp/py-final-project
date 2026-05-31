import json
from models import Record, AddressBook, NoteBook, Note
from logic import search_contacts, search_notes
from validators import (
    check_or_raise,
    validate_phone,
    validate_email,
    validate_not_empty,
)


def save_data(address_book, note_book, filename="data.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(
            {"contacts": address_book.to_dict(), "notes": note_book.to_dict()},
            f,
            ensure_ascii=False,
            indent=2,
        )


def load_data(filename="data.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return AddressBook.from_dict(data["contacts"]), NoteBook.from_dict(
                data["notes"]
            )
    except (FileNotFoundError, KeyError, ValueError):
        return AddressBook(), NoteBook()


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            raise ValueError(str(e))
        except IndexError:
            raise ValueError("Not enough arguments provided for this command.")
        except KeyError as e:
            raise ValueError(str(e) if str(e) else "Requested item not found.")

    return inner


def smart_search(query, book, notes):

    
    # Очищаємо запит від символу #
    clean_query = str(query).lstrip("#").strip().lower()

    # Викликаємо потужні функції пошуку з logic.py
    found_contacts = search_contacts(book, clean_query)
    note_results = search_notes(notes, clean_query)

    # Повертаємо СЛОВНИК, як того вимагає функція render_smart_search у views.py
    return {
        "contacts": found_contacts,
        "notes": note_results
    }


# Команди для контактів


@input_error
def add_contact(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("add-contact [name] [phone] [email_optional]")

    name = args[0]
    phone = args[1]
    email = args[2] if len(args) > 2 else None

    check_or_raise(validate_not_empty, name, "Name cannot be empty.")
    check_or_raise(validate_phone, phone, "Invalid phone! Must be 10 digits.")
    if email:
        check_or_raise(
            validate_email,
            email,
            "Invalid email format. Please check the address.",
        )

    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)

    record.add_phone(phone)
    if email:
        record.add_email(email)

    return "Contact added."


@input_error
def add_birthday(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("add-birthday [name] [birthday]")

    name, birthday = args
    record = book.find(name)

    if record:
        record.add_birthday(birthday)
        return "Birthday added."

    raise KeyError


@input_error
def show_birthday(args, book: AddressBook):
    if len(args) < 1:
        raise ValueError("show-birthday [name]")
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return f"{name}'s birthday is on {record.birthday.value}"
    raise KeyError


@input_error
def birthdays(args, book: AddressBook):
    from logic import get_upcoming_birthdays

    # Перевіряємо, чи передав користувач кількість днів (наприклад, "birthdays 14")
    days = 7  # значення за замовчуванням
    if args:
        try:
            days = int(args[0])
            if days < 0:
                raise ValueError("Number of days cannot be negative.")
        except ValueError:
            raise ValueError("Please provide a valid number of days, e.g., 'birthdays 14'")

    # Передаємо days у функцію розрахунку
    upcoming = get_upcoming_birthdays(book, days=days)
    return upcoming


@input_error
def change_contact(args, book: AddressBook):
    if len(args) < 3:
        raise ValueError("change-contact [name] [old_phone] [new_phone]")
    name, old_phone, new_phone = args

    check_or_raise(
        validate_phone, new_phone, "Invalid new phone! Must be 10 digits."
    )

    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return "Contact updated."
    raise KeyError


@input_error
def show_phone(args, book: AddressBook):
    record = book.find(args[0])
    if not record:
        return "Not found."
    return "; ".join(p.value for p in record.phones)


@input_error
def show_all_contacts(book: AddressBook):
    if not book.data:
        return []
    return list(book.data.values())


@input_error
def delete_contact(args, book: AddressBook):
    if len(args) < 1:
        raise ValueError("show-birthday [name]")
    book.delete(args[0])
    return f"Contact '{args[0]}' deleted."


# Команди для нотаток (працюють з NoteBook)


@input_error
def add_note(args, notes: NoteBook):
    # Приклад введення: add-note Title "Content goes here" tag1,tag2
    if len(args) < 3:
        raise ValueError("Usage: add-note [title] [content] [tags_comma_separated]")

    title = args[0]
    tags = [t.strip() for t in args[-1].split(",")]
    content = " ".join(args[1:-1])

    notes.add_note(Note(title, content, tags))
    return f"Note '{title}' added."


@input_error
def edit_note(args, notes: NoteBook):
    if len(args) < 2:
        raise ValueError("Usage: edit-note [title] [new_content]")

    title, *content_parts = args
    new_content = " ".join(content_parts)

    notes.edit_note(title, new_content)
    return f"Note '{title}' updated."


@input_error
def find_notes_by_tag(args, notes: NoteBook):
    if not notes.data:
        return []
    return list(notes.data.values())


@input_error
def delete_note(args, notes: NoteBook):
    if not args:
        raise ValueError("delete-note [title]")

    title = args[0]

    if title not in notes.data:
        raise KeyError(f"Note with title '{title}' not found.")

    notes.delete_note(title)
    return f"Note '{title}' deleted."


@input_error
def add_address(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("Usage: add-address [name] [address]")

    name = args[0]
    # Використовуємо " ".join, щоб адреса могла складатися з кількох слів
    address = " ".join(args[1:])

    check_or_raise(validate_not_empty, address, "Address cannot be empty.")

    record = book.find(name)
    if record:
        record.add_address(address)
        return f"Address added to contact '{name}'."
    raise KeyError


@input_error
def edit_address(args, book: AddressBook):
    if len(args) < 2:
        raise ValueError("Usage: edit-address [name] [new_address]")

    name = args[0]
    new_address = " ".join(args[1:])

    check_or_raise(validate_not_empty, new_address, "Address cannot be empty.")

    record = book.find(name)
    if record:
        record.edit_address(new_address)
        return f"Address for contact '{name}' updated."
    raise KeyError
