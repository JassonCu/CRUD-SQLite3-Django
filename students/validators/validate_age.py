from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_age(age: int) -> bool:
    """
    Valida la edad de una persona.
    Args:
        age (int): Edad de la persona.
    Returns:
        bool: True si la edad es válida, False en caso contrario.
    Raises:
        ValueError: Si la edad es negativa o mayor a 100.
    """

    if age < 0 or age > 100:
        raise ValidationError(_("La edad debe estar entre 0 y 100"))
    return True
