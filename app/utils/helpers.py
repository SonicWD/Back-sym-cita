# utils/helpers.py

from datetime import datetime
import re

def validate_date_format(date_string: str) -> bool:
    """
    Valida si una cadena tiene el formato de fecha correcto (YYYY-MM-DD).
    """
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(pattern, date_string):
        try:
            datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False
    return False

def calculate_age(birth_date: str) -> int:
    """
    Calcula la edad a partir de la fecha de nacimiento.
    """
    birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    return age

def format_phone_number(phone: str) -> str:
    """
    Formatea un número de teléfono para asegurar un formato consistente.
    """
    # Elimina todos los caracteres no numéricos
    digits = re.sub(r'\D', '', phone)
    
    # Verifica si el número tiene la longitud correcta (asumiendo 10 dígitos)
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    else:
        return phone  # Devuelve el número original si no tiene el formato esperado

def sanitize_string(input_string: str) -> str:
    """
    Sanitiza una cadena de texto eliminando caracteres especiales y espacios extra.
    """
    # Elimina caracteres especiales y deja solo letras, números y espacios
    sanitized = re.sub(r'[^a-zA-Z0-9\s]', '', input_string)
    # Elimina espacios extra y espacios al inicio y al final
    sanitized = ' '.join(sanitized.split())
    return sanitized