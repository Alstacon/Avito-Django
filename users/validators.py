from datetime import date

from django.core.exceptions import ValidationError


def age_validator(value):
    if (date.today() - value).days // 365 < 9:
        raise ValidationError('Only users over the age of nine can register.')


def email_validator(value):
    if '@rambler.ru' in value:
        raise ValidationError('Use another email.')
