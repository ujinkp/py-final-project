import json
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
    add_note,
    find_notes_by_tag,
    delete_contact,
    delete_note,
    edit_note,
    smart_search,
    save_data,
    load_data,
)

from prompt_toolkit.history import InMemoryHistory
from rich import print
from views import (
    render_welcome_message,
    render_contacts_table,
    render_phones,
    render_notes_list,
    render_smart_search,
    get_user_input,
    render_success,
    render_error,
)


def main():
    book, notes = load_data()
    render_welcome_message()
    command_history = InMemoryHistory()

    while True:
        try:
            user_input = get_user_input(book, notes, command_history)
        except (KeyboardInterrupt, EOFError):
            user_input = "exit"
        if not user_input:
            continue

        command, *args = parse_input(user_input)
        try:
            match command:
                case "close" | "exit":
                    save_data(book, notes)
                    render_success("Good bye!")
                    break

                case "hello":
                    print("[bold blue]How can I help you?[/bold blue]")

                case "add-contact":
                    render_success(add_contact(args, book))

                case "add-address":
                    render_success(add_address(args, book))

                case "edit-address":
                    render_success(edit_address(args, book))

                case "change-contact":
                    render_success(change_contact(args, book))

                case "add-birthday":
                    render_success(add_birthday(args, book))

                case "delete-contact":
                    render_success(delete_contact(args, book))

                case "add-note":
                    render_success(add_note(args, notes))

                case "edit-note":
                    render_success(edit_note(args, notes))

                case "delete-note":
                    render_success(delete_note(args, notes))

                case "phone":
                    phones_list = show_phone(args, book)
                    render_phones(args[0], phones_list)

                case "show-birthday":
                    render_success(show_birthday(args, book))

                case "birthdays":
                    upcoming_birthdays = birthdays(args, book)
                    if not upcoming_birthdays:
                        print(
                            "[yellow]📅 No upcoming birthdays"
                            " next week.[/yellow]"
                        )
                    else:
                        print(
                            "\n[bold magenta]🎂 Upcoming"
                            " Birthdays:[/bold magenta]"
                        )
                        for u in upcoming_birthdays:
                            print(
                                f"  ▪️ [bold green]{u['name']}[/bold green]"
                                f": {u['congratulation_date']}"
                            )

                case "all":
                    contacts = show_all_contacts(book)
                    render_contacts_table(contacts)

                case "find-notes":
                    found_notes = find_notes_by_tag(args, notes)
                    render_notes_list(
                        found_notes, title=f"🔍 Notes with tag '{args[0]}'"
                    )

                case cmd if cmd.startswith("#"):
                    search_results = smart_search(cmd, book, notes)
                    render_smart_search(search_results)

                case _:
                    render_error("Invalid command. Try using TAB for hints.")
        except ValueError as e:
            render_error(e)

        except IndexError:
            render_error("Not enough arguments provided for this command.")

        except Exception as e:
            render_error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
