## OmniBrain: Personal Productivity Core 🧠

OmniBrain is a professional console-based assistant bot designed to manage your contacts and notes efficiently. Built with Python, this application provides a robust system for storing personal information, tracking birthdays, and organizing tasks or ideas with a tag-based note system.

### Key Features

* 💾 **Persistent Storage:** Automatically saves and loads all data (contacts and notes) to/from a binary file (`data.pkl`) using the `pickle` module, ensuring no data is lost between sessions.
* 👥 **Contact Management:** Add new contacts, store multiple phone numbers, email addresses, and physical addresses.
* 📝 **Smart Notes System:** Create, edit, and delete text-based notes. Organize them using **tags** for quick retrieval and categorization.
* 🎂 **Birthday Tracking:** Store birthdays and retrieve them with a single command. 
* 📅 **Smart Reminders:** Automatically calculates congratulation dates for the next 7 days, seamlessly adjusting weekend birthdays to the following Monday.
* ✅ **Data Validation:** Built-in strict validation for phone numbers (exactly 10 digits) and email formats.
* 🧱 **Modular Architecture:** Clean code separation into `main.py`, `handlers.py`, `logic.py`, `models.py`, and `validators.py` for maximum maintainability and separation of concerns.

---

### Available Commands

| Category | Command | Description | Example |
| :--- | :--- | :--- | :--- |
| **General** | **hello** | Receive a friendly greeting | `hello` |
| | **close / exit** | Securely save data and terminate | `exit` |
| **Contacts** | **add** | Add a new contact | `add Hanna 0954656234 email@test.com` |
| | **change** | Update a contact's phone number | `change Hanna 0954656234 0991234567` |
| | **phone** | Show all saved phones for a contact | `phone Hanna` |
| | **all** | Show all contacts | `all` |
| | **add-birthday**| Set a birthday for a contact | `add-birthday Hanna 10.05.1990` |
| | **show-birthday**| View a contact's birthday | `show-birthday Hanna` |
| | **birthdays** | Show upcoming birthdays for next 7 days | `birthdays` |
| | **delete-contact**| Delete a contact | `delete-contact Hanna` |
| **Notes** | **add-note** | Add a note with title, content, and tags | `add-note Project Content_here study,ai` |
| | **find-notes** | Search for notes by tag | `find-notes study` |
| | **delete-note** | Delete a note by its title | `delete-note Project` |

---

### Project Structure

* **`main.py`**: The entry point of the application. Handles data serialization/deserialization, controls the main CLI loop, and routes commands.
* **`handlers.py`**: Contains command-line interface handlers, argument parsing, and the `@input_error` decorator for safe exception handling.
* **`models.py`**: Defines core data structures (`AddressBook`, `NoteBook`, `Record`, `Note`, `Field`, etc.).
* **`logic.py`**: Contains core business logic, including birthday calculations and search algorithms.
* **`validators.py`**: Logic for ensuring data integrity (phone/email validation).

---

### How to Install and Run

#### Prerequisites
* **Python 3.10 or higher** is required (due to the use of `match/case` statements).

#### Setup Instructions
1. Copy the project files to your local workspace.
2. Open your terminal.
3. Navigate to the project directory: 
   ```bash
   cd your-project-directory
Run the application:

Bash
python main.py

Note for Windows users: If the command above is not found, try running py main.py.