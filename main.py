import pickle
from models import AddressBook, NoteBook
from handlers import (
    parse_input, 
    add_contact, 
    change_contact,  
    show_phone,     
    add_birthday, 
    show_birthday, 
    birthdays,
    add_address,
    edit_address,
    show_all_contacts,  
    add_note,           # Нові імпорти
    find_notes_by_tag,
    delete_contact,
    delete_note,
    edit_note,
    smart_search 
)

# --- Функції серіалізації даних ---

def save_data(address_book, note_book, filename="data.pkl"):
    """Зберігає і контакти, і нотатки в один файл."""
    with open(filename, "wb") as f:
        data = {
            "contacts": address_book,
            "notes": note_book
        }
        pickle.dump(data, f)

def load_data(filename="data.pkl"):
    """Завантажує дані. Якщо файл відсутній, створює порожні екземпляри."""
    try:
        with open(filename, "rb") as f:
            data = pickle.load(f)
            return data["contacts"], data["notes"]
    except (FileNotFoundError, KeyError, EOFError):
        return AddressBook(), NoteBook()

# --- Головна функція ---

def main():
    # Завантажуємо обидві книги
    book, notes = load_data()
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue
        
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                # Зберігаємо обидва об'єкти
                save_data(book, notes)
                print("Good bye!")
                break
                
            case "hello":
                print("How can I help you?")
                
            case "add":
                print(add_contact(args, book))
                
            case "change":  
                print(change_contact(args, book))
                
            case "phone":  
                print(show_phone(args, book))
                
            case "add-birthday":
                print(add_birthday(args, book))
                
            case "show-birthday":
                print(show_birthday(args, book))
                
            case "birthdays":
                print(birthdays(args, book))
                
            case "all":
                print(show_all_contacts(book))
  
            case "add-address":
                print(add_address(args, book))
                
            case "edit-address":
                print(edit_address(args, book))

            # --- Команди нотаток (тепер передаємо об'єкт notes) ---
            case "add-note":
                print(add_note(args, notes))
                
            case "find-notes":
                print(find_notes_by_tag(args, notes))
                
            case "delete-contact":
                print(delete_contact(args, book))
                
            case "edit-note":
                print(edit_note(args, notes))


            case "delete-note":
                print(delete_note(args, notes))   


            # Додаємо наш новий "розумний" кейс:
            case cmd if cmd.startswith("#"):
                print(smart_search(cmd, book, notes))       
                        
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()