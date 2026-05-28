from rich import print
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.markup import escape

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style

PROMPT_STYLE = Style.from_dict({
    'prompt': '#00ffcd bold',           # Колір для "🤖 assistant ❯"
    'command': '#ffffff italic',        # Колір введеного тексту
    'toolbar': 'bg:#222222 #00aa00',    # Нижній статус-бар
    'completion-menu.completion': 'bg:#005f5f #ffffff',
    'completion-menu.completion.current': 'bg:#00ffff #000000 bold',
})

COMMANDS_LIST = [
    "hello", "add", "change", "phone", "add-birthday", "show-birthday", 
    "birthdays", "all", "add-note", "find-notes", "delete-contact", 
    "edit-note", "delete-note", "close", "exit"
]

COMMAND_COMPLETER = WordCompleter(COMMANDS_LIST, ignore_case=True, sentence=True)

def render_welcome_message():
    welcome_text = Text("Welcome to the assistant bot!", style="bold cyan")
    welcome_text.append("\nType your command or press [TAB] to see available commands.", style="italic magenta")
    print(Panel(welcome_text, border_style="green", expand=False))

def render_contacts_table(records_list):
    if not records_list:
        print("[yellow]📭 Address book is empty.[/yellow]")
        return

    table = Table(
        title="👥 Address Book Contacts", 
        title_style="bold magenta", 
        show_lines=True, 
        border_style="cyan"
    )
    
    table.add_column("Name", style="bold green", justify="left")
    table.add_column("Phones", style="white", justify="center")
    table.add_column("Birthday", style="yellow", justify="center")

    for record in records_list:
        name = str(record.name)
        phones = ", ".join([str(p) for p in record.phones]) if record.phones else "-"
        birthday = str(record.birthday) if record.birthday else "-"
        table.add_row(name, phones, birthday)

    print(table)

def render_phones(name, phones_list):
    if not phones_list:
        print(f"[yellow]📞 Contact '{name}' has no phone numbers saved.[/yellow]")
        return
    phones_str = ", ".join(phones_list)
    print(Panel(f"[bold cyan]{phones_str}[/bold cyan]", title=f"📞 Phones for {name}", expand=False))

def render_notes_list(notes_list, title="📝 Found Notes"):
    if not notes_list:
        print("[yellow]🔍 No notes found.[/yellow]")
        return
    
    print(f"\n[bold magenta]{title}[/bold magenta]")
    for note in notes_list:
        tags_str = ", ".join(note.tags) if hasattr(note, 'tags') and note.tags else "no tags"
        content = note.content if hasattr(note, 'content') else str(note)
        
        content = " ".join(content.split())
        
        note_text = f"{content}\n\n[italic grey50]🏷️ Tags: {tags_str}[/italic grey50]"
        
        print(Panel(
            note_text, 
            title=f"[bold cyan]{note.title}[/bold cyan]", 
            border_style="bright_blue", 
            expand=False,
            width=50
        ))

def render_smart_search(search_results):
    contacts = search_results.get("contacts", [])
    notes = search_results.get("notes", [])
    
    if not contacts and not notes:
        print("[yellow]🧠 Smart Search: Nothing found anywhere.[/yellow]")
        return
        
    if contacts:
        render_contacts_table(contacts)
        
    if notes:
        render_notes_list(notes, title="📝 Smart Search: Matching Notes")

def get_user_input(address_book, notes, command_history):
    def get_toolbar_text():
        contacts_count = len(address_book.data) if hasattr(address_book, 'data') else 0
        notes_count = len(notes.data) if hasattr(notes, 'data') else 0
        return f" [TAB] Hints | Total 👥 Contacts: {contacts_count} 📝 Notes: {notes_count} | Type 'exit' to quit"

    return prompt(
        [('class:prompt', '🤖 assistant ❯ ')],
        completer=COMMAND_COMPLETER,
        style=PROMPT_STYLE,
        history=command_history,
        bottom_toolbar=get_toolbar_text,
        complete_while_typing=True
    ).strip()

def render_success(message):
    print(f"[bold green]✅ {message}[/bold green]")

def render_error(message):
    msg_str = str(message)
    
    if "usage:" in msg_str.lower():
        print(f"[bold red]❌ {escape(msg_str)}[/bold red]")
    else:
        print(f"[bold red]❌ Error: {escape(msg_str)}[/bold red]")
