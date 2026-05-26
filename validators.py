import re
from datetime import datetime

def validate_phone(phone: str) -> bool:
    return bool(re.fullmatch(r"\d{10}", phone))

def validate_email(email: str) -> bool:
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return bool(re.fullmatch(pattern, email))

def validate_date(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, "%d.%m.%Y")
        return True
    except ValueError:
        return False

def validate_not_empty(value: str) -> bool:
    return bool(value and value.strip())

def check_or_raise(validator_func, value, error_message):
    if not validator_func(value):
        raise ValueError(error_message)
    return True