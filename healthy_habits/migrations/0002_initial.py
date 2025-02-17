# Generated by Django 5.1.6 on 2025-02-17 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('healthy_habits', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='user',
            field=models.ForeignKey(blank=True, help_text='Укажите создателя привычки', null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.user', verbose_name='Создатель привычки'),
        ),
    ]
