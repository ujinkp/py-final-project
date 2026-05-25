from datetime import datetime, timedelta
from models import AddressBook  

def search_contacts(address_book, query):
    """Логіка пошуку по книзі контактів."""
    results = []
    query = query.lower()
    for record in address_book.data.values():
        match = (query in record.name.value.lower() or 
                 any(query in p.value for p in record.phones) or
                 (record.email and query in record.email.value.lower()) or
                 (record.address and query in record.address.value.lower()))
        if match:
            results.append(record)
    return results

def get_upcoming_birthdays(address_book):
    """Логіка розрахунку днів народження."""
    upcoming_birthdays = []
    today = datetime.today().date()
    for record in address_book.data.values():
        if not record.birthday:
            continue
        birthday_this_year = record.birthday.value.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        days_until = (birthday_this_year - today).days
        if 0 <= days_until <= 7:
            congrats_date = birthday_this_year
            weekday = congrats_date.weekday()
            if weekday == 5: congrats_date += timedelta(days=2)
            elif weekday == 6: congrats_date += timedelta(days=1)
            
            upcoming_birthdays.append({
                "name": record.name.value, 
                "congratulation_date": congrats_date.strftime("%d.%m.%Y")
            })
    return upcoming_birthdays


def search_notes(note_book, query):
    """Пошук нотаток за заголовком або контентом."""
    return [n for n in note_book.data.values() if query.lower() in n.title.lower() or query.lower() in n.content.lower()]

def sort_notes_by_tag(note_book, tag):
    """Пошук нотаток за тегом."""
    return [n for n in note_book.data.values() if tag.lower() in [t.lower() for t in n.tags]]