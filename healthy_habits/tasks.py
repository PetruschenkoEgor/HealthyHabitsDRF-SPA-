from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.utils import timezone

from healthy_habits.models import Habit
from healthy_habits.services import send_telegram_message


@shared_task
def send_reminder_in_telegram():
    """Отправить напоминание в телеграм."""

    now = timezone.now().time()
    current_minute = now.replace(second=0, microsecond=0)
    formated_now = now.strftime("%H:%M:%S")
    print(f"время: {formated_now}")
    habits = Habit.objects.filter(time=current_minute)
    for habit in habits:
        user = habit.user
        if user.tg_chat_id:
            if habit.related_habit:
                message = (f"Напоминание! У Вас запланировано: {habit.action if habit.action else 'действие'}. "
                           f"В {habit.time.strftime('%H:%M')}. Место: {habit.place if habit.place else 'не указано'}. "
                           f"Время на выполнение: "
                           f"{habit.time_to_complete if habit.time_to_complete else 'не указано'}. "
                           f"И в награду Вы можете {habit.related_habit.lower()}.")
            elif habit.reward:
                message = (f"Напоминание! У Вас запланировано: {habit.action if habit.action else 'действие'}. "
                           f"В {habit.time.strftime('%H:%M')}. Место: {habit.place if habit.place else 'не указано'}. "
                           f"Время на выполнение: {habit.time_to_complete if habit.time_to_complete else 'не указано'}"
                           f". И в награду Вы можете {habit.reward.lower()}.")
            else:
                message = (f"Напоминание! У Вас запланировано: {habit.action if habit.action else 'действие'}. "
                           f"В {habit.time.strftime('%H:%M')}. Место: {habit.place if habit.place else 'не указано'}. "
                           f"Время на выполнение: "
                           f"{habit.time_to_complete if habit.time_to_complete else 'не указано'}.")
        send_telegram_message(user.tg_chat_id, message)
        print("Сообщение отправлено")
