from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_phone(value):
    """
    Valida que el número de teléfono tenga exactamente ocho dígitos.
    """
    if not str(value).isdigit() or len(str(value)) != 8:
        raise ValidationError(
            _('El número de teléfono debe contener exactamente ocho dígitos.'))
