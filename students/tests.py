from django.core.exceptions import ValidationError
from django.test import TestCase
from .validators.validate_phone import validate_phone
# Create your tests here.


class PhoneValidationTestCase(TestCase):
    def test_valid_phone(self):
        # Prueba un número de teléfono válido de ocho dígitos
        valid_phone = '12345678'
        try:
            validate_phone(valid_phone)
        except ValidationError:
            self.fail(
                'Se lanzó ValidationError para un número de teléfono válido.')

    def test_invalid_phone_length(self):
        # Prueba un número de teléfono con longitud incorrecta
        invalid_phone = '1234567'  # Solo siete dígitos
        with self.assertRaises(ValidationError):
            validate_phone(invalid_phone)

    def test_invalid_phone_format(self):
        # Prueba un número de teléfono con caracteres no numéricos
        invalid_phone = '12a45678'  # Caracter 'a' no es un dígito
        with self.assertRaises(ValidationError):
            validate_phone(invalid_phone)
