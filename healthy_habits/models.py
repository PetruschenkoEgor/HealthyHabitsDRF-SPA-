from django.db import models

from users.models import User


class Habit(models.Model):
    """ Модель привычки. """

    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Создатель привычки', help_text='Укажите создателя привычки')
    place = models.CharField(max_length=250, blank=True, null=True, verbose_name='Место', help_text='Укажите место')
    time = models.TimeField(blank=True, null=True, verbose_name='Время', help_text='Укажите время')
    action = models.TextField(blank=True, null=True, verbose_name='Действие', help_text='Укажите действие')
    sign_pleasant_habit = models.BooleanField(blank=True, null=True, verbose_name='Признак приятной привычки', help_text='Укажите признак приятной привычки', default=False)
    related_habit = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Связанная привычка', help_text='Укажите связанную привычку', related_name='related_habits')
    periodicity = models.PositiveIntegerField(blank=True, null=True, verbose_name='Периодичность', help_text='Укажите периодичность', default=1)
    reward = models.TextField(blank=True, null=True, verbose_name='Вознаграждение', help_text='Укажите вознаграждение')
    time_to_complete = models.DurationField(blank=True, null=True, verbose_name='Время на выполнение', help_text='Укажите время на выполнение')
    sign_publicity = models.BooleanField(blank=True, null=True, verbose_name='Признак публичности', help_text='Укажите признак публичности', default=False)

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
