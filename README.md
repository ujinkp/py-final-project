# OmniBrain: Your Personal Productivity Hub 🧠

## English Version

**OmniBrain** is a professional console assistant bot designed for efficient contact and work-notes management. Thanks to its smart search system and modular architecture, OmniBrain becomes a reliable “second brain” for managers who value speed and organization.

---

## Key Features

* 💾 **Persistent Storage:** Automatic saving and loading of data (contacts and notes) into the `data.json` file.
* 👥 **Contact Management:** Store names, phone numbers, emails and addresses, as well as birthdays.
* ⚡ **Omni Search (Smart Search):** Use the `#` symbol to instantly search clients and related work notes at the same time. No need to remember where information is stored!
* 📝 **Smart Notes:** Work with notes using tags to categorize projects, finances, or tasks.
* 🎂 **Birthday Tracker:** Track important dates and receive reminders for birthdays occurring within the defined number of days.
* 🛡 **Data Validation:** Built-in validation for phone numbers and email formats.

---

## OmniBrain Commands

| Category | Command | Description | Example |
|---|---|---|---|
| Search | `#name` | Smart Search: search contacts and notes by tag/name | `#Hanna` |
| Contacts | `add-contact` | Add a new contact (name, phone, email). Contacts can store multiple phone numbers — simply add the same contact with another number and OmniBrain will save both old and new numbers. | `add-contact Hanna 0951112233`<br>`hanna@email.com` |
|  | `change-contact` | Update a contact’s phone number to the new one | `change Hanna 0951112233 0951112234` |
|  | `all` | Show all contacts | `all` |
|  | `add-address` | Adds an address to a contact | `add-address Hanna Stryiska build. 12, apt. 35` |
|  | `add-birthday` | Add a birthday date | `add-birthday Mariia 21.11.2000` |
|  | `birthdays` | Upcoming birthdays: displays birthdays within the next 7 days. If a birthday falls on a weekend, it is moved to Monday. | `birthdays` |
|  | `delete-contact` | Delete a contact | `delete-contact Mariia` |
| Notes | `add-note` | Add a note (title, content, tags) | `add-note Project "Plan"`<br>`work,hanna` |
|  | `find-notes` | Search notes by tag | `find-notes work` |
|  | `delete-note` | Delete a note | `delete-note ProjectA` |

---

## Project Architecture

OmniBrain is built following clean architecture principles:

* `main.py` — Main bot loop and command router.
* `handlers.py` — User input processing and routing to business logic.
* `models.py` — Data structures (`AddressBook`, `NoteBook`, `Record`).
* `logic.py` — Business logic (date calculations, search algorithms).
* `validators.py` — Data validation rules.
* `views.py` — Implementation of console "rich UI" features, e.g. tables, formatting, menus and hints.

---

## Getting Started

### Requirements

* **Python 3.10+** (required for the `match/case` syntax).

### Installation and Launch

1. Clone or download the project files into your working folder.

2. Open a terminal in this folder.

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

For Windows, if the `pip` command does not work, try:

```bash
py -m pip install -r requirements.txt
```

4. Run the program:

```bash
python main.py
```

For Windows, if the `python` command does not work, try:

```bash
py main.py
```

💡 **Manager Tip:** Use `#ClientName` as your main quick-access tool during work calls to instantly retrieve all client-related information.

---


# OmniBrain: Центр вашої особистої продуктивності 🧠

## Ukrainian Version

**OmniBrain** — це професійний консольний бот-помічник, створений для ефективного керування контактами та робочими нотатками. Завдяки розумній системі пошуку та модульній архітектурі, OmniBrain стане надійним "другим мозком" для менеджера, який цінує швидкість та порядок у справах.

---

## Основні можливості

* 💾 **Постійне зберігання:** Автоматичне збереження та завантаження даних (контактів та нотаток) у файл `data.json`.
* 👥 **Керування контактами:** Зберігання імен, телефонів, email-адрес, поштових адрес та дат народження.
* ⚡ **Omni-пошук (Smart Search):** Використовуйте символ `#` для миттєвого пошуку клієнтів та пов'язаних з ними робочих нотаток одночасно. Більше не потрібно пам'ятати, де лежить інформація!
* 📝 **Інтелектуальні нотатки:** Робота з нотатками за допомогою тегів для категоризації проєктів, фінансів чи робочих завдань.
* 🎂 **Трекер днів народжень:** Відстежуйте важливі дати та отримуйте нагадування про дні народження, що настануть протягом вказаної кількості днів.
* 🛡 **Валідація даних:** Вбудована перевірка коректності номерів телефонів та форматів email.

---

## Команди OmniBrain

| Категорія | Команда | Опис | Приклад |
|---|---|---|---|
| Пошук | `#назва` | Smart Search: пошук контакту та нотаток за тегом/іменем | `#Hanna` |
| Контакти | `add-contact` | Додати новий контакт (ім'я, телефон, ел. пошта). Контакти можуть зберігати декілька номерів телефонів — просто додайте той самий контакт з новим номером, OmniBrain збереже і старий, і новий. | `add-contact Hanna 0951112233`<br>`hanna@email.com` |
|  | `change-contact` | Змінити номер телефона контакта на новий | `change-contact Hanna 0951112233 0951112234` |
|  | `all` | Показати всі контакти | `all` |
|  | `add-address` | Додати адресу до контакту | `add-address Hanna Стрийська буд. 12, кв. 35` |
|  | `add-birthday` | Додати дату народження | `add-birthday Mariia 21.11.2000` |
|  | `birthdays` | Найближчі дні народження: показуються дні народження, що попадають на найближчі 7 днів. Якщо ДН вихідний — він переноситься на понеділок. | `birthdays` |
|  | `delete-contact` | Видалити контакт | `delete-contact Mariia` |
| Нотатки | `add-note` | Додати нотатку (заголовок, зміст, теги) | `add-note Project "План"`<br>`work,hanna` |
|  | `find-notes` | Пошук нотаток за тегом | `find-notes work` |
|  | `delete-note` | Видалити нотатку | `delete-note Project` |

---

## Архітектура проєкту

OmniBrain побудований за принципом чистої архітектури:

* `main.py` — головний цикл бота та маршрутизатор команд.
* `handlers.py` — обробка вводу користувача та виклик відповідних логічних функцій.
* `models.py` — опис структур даних (`AddressBook`, `NoteBook`, `Record`).
* `logic.py` — бізнес-логіка (розрахунок дат, алгоритми пошуку).
* `validators.py` — правила валідації даних.
* `views.py` — реалізація консольного "rich UI": таблиці, форматування, меню та підказки.

---

## Як почати роботу

### Вимоги

* **Python 3.10+** (необхідно для використання конструкції `match/case`).

### Встановлення та запуск

1. Клонуйте або завантажте файли проєкту у робочу папку.

2. Відкрийте термінал у цій папці.

3. Встановіть необхідні залежності:

```bash
pip install -r requirements.txt
```

Для Windows, якщо команда `pip` не спрацювала, спробуйте:

```bash
py -m pip install -r requirements.txt
```

4. Запустіть програму:

```bash
python main.py
```

Для Windows, якщо команда `python` не спрацювала, спробуйте:

```bash
py main.py
```

💡 **Порада для менеджера:** Використовуйте `#Ім'яКлієнта` як основний інструмент швидкого доступу до всієї інформації про клієнта під час робочих дзвінків!