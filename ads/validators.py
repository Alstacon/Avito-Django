from django.core.exceptions import ValidationError


def is_published_validator(value: bool):
    if value:
        raise ValidationError("The advertisement has not been published yet")
