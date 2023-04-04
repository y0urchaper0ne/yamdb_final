import re

from datetime import datetime

from django.core.exceptions import ValidationError


def username_validator(value):
    if value.lower() == 'me':
        raise ValidationError('Имя пользователя не может быть me')
    if not re.match(r'^[-a-zA-Z0-9_]+$', value):
        raise ValidationError(
            f'Имя пользователя {value} содержит недопустимые символы'
        )


def year_validator(value):
    current_year = datetime.now().year
    if value > current_year:
        raise ValidationError(
            f'Год не может быть больше {current_year}'
        )
