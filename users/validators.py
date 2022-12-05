from datetime import date

from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError
from rest_framework import serializers


def age_validator(value):
    if relativedelta(date.today(), value).years < 9:
        raise ValidationError('Only users over the age of nine can register.')


class EmailValidator:
    def __init__(self, disabled_list):
        self.disabled_list = disabled_list

    def __call__(self, value):
        for dom in self.disabled_list:
            if dom in value:
                raise serializers.ValidationError("User different email")
