from datetime import timedelta

from rest_framework.exceptions import ValidationError


def validate_time_to_complete(value):
    """ Валидатор проверяет, чтобы время выполнения не превышало 2 минуты. """

    if value > timedelta(seconds=120):
        raise ValidationError('Время выполнения не может быть дольше 2-х минут.')


def validate_periodicity(value):
    """ Валидатор проверяет, чтобы периодичность была не реже 7 дней. """

    if value < 1:
        raise ValidationError('Периодичность выполнения не может быть реже 7 дней.')
