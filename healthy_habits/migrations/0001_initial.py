# Generated by Django 5.1.6 on 2025-02-17 16:10

import django.db.models.deletion
import healthy_habits.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, help_text='Укажите место', max_length=250, null=True, verbose_name='Место')),
                ('time', models.TimeField(blank=True, help_text='Укажите время', null=True, verbose_name='Время')),
                ('action', models.TextField(blank=True, help_text='Укажите действие', null=True, verbose_name='Действие')),
                ('sign_pleasant_habit', models.BooleanField(blank=True, default=False, help_text='Укажите признак приятной привычки', null=True, verbose_name='Признак приятной привычки')),
                ('periodicity', models.PositiveIntegerField(blank=True, default=1, help_text='Укажите периодичность', null=True, validators=[healthy_habits.validators.validate_periodicity], verbose_name='Периодичность(дней)')),
                ('reward', models.TextField(blank=True, help_text='Укажите вознаграждение', null=True, verbose_name='Вознаграждение')),
                ('time_to_complete', models.DurationField(blank=True, help_text='Укажите время на выполнение', null=True, validators=[healthy_habits.validators.validate_time_to_complete], verbose_name='Время на выполнение')),
                ('sign_publicity', models.BooleanField(blank=True, default=False, help_text='Укажите признак публичности', null=True, verbose_name='Признак публичности')),
                ('related_habit', models.ForeignKey(blank=True, help_text='Укажите связанную привычку', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_habits', to='healthy_habits.habit', verbose_name='Связанная привычка')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]
