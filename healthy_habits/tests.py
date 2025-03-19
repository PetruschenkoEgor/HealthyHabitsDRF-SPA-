from datetime import timedelta

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from healthy_habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru")
        self.habit = Habit.objects.create(
            user=self.user,
            place="Дом",
            time="07:30:00",
            action="Принять витамины",
            sign_pleasant_habit=False,
            periodicity=7,
            reward="Слушать музыку",
            time_to_complete=timedelta(seconds=120),
            sign_publicity=True,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):
        """Тест создания привычки."""

        url = reverse("healthy_habits:habit-create")
        data = {
            "place": "Дом",
            "time": "8:00:00",
            "action": "Принять прохладный душ",
            "sign_pleasant_habit": False,
            "periodicity": 7,
            "reward": "Выпить теплого молока",
            "time_to_complete": "00:02:00",
            "sign_publicity": True,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_retrieve(self):
        """Тест информации об одной привычке."""

        url = reverse("healthy_habits:habit-get", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), self.habit.place)
        self.assertEqual(data.get("time"), self.habit.time)
        self.assertEqual(data.get("action"), self.habit.action)
        self.assertEqual(data.get("sign_pleasant_habit"), self.habit.sign_pleasant_habit)
        self.assertEqual(data.get("periodicity"), self.habit.periodicity)
        self.assertEqual(data.get("reward"), self.habit.reward)
        expected_duration = str(self.habit.time_to_complete).split(':')
        expected_duration = (f"{int(expected_duration[0]):02}:{int(expected_duration[1]):02}:"
                             f"{int(expected_duration[2]):02}")
        self.assertEqual(data.get("time_to_complete"), expected_duration)
        self.assertEqual(data.get("sign_publicity"), self.habit.sign_publicity)

    def test_habit_list(self):
        """Тест списка привычек текущего пользователя."""

        url = reverse("healthy_habits:habit-list")
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['count'], 1)
        self.assertEqual(len(data['results']), 1)
        habit_data = data['results'][0]
        self.assertEqual(habit_data['place'], self.habit.place)
        self.assertEqual(habit_data['time'], self.habit.time)
        self.assertEqual(habit_data['action'], self.habit.action)

    def test_habit_public(self):
        """Тест списка публичных привычек."""

        url = reverse("healthy_habits:habit-public-list")
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем, что хотя бы одна привычка возвращается
        self.assertTrue(len(data['habits_public']) > 0)

        # Проверяем первую привычку в списке
        habit_data = data['habits_public'][0]
        self.assertEqual(habit_data['place'], self.habit.place)
        self.assertEqual(habit_data['time'], self.habit.time)
        self.assertEqual(habit_data['action'], self.habit.action)
        self.assertEqual(habit_data['sign_pleasant_habit'], self.habit.sign_pleasant_habit)
        self.assertEqual(habit_data['periodicity'], self.habit.periodicity)
        self.assertEqual(habit_data['reward'], self.habit.reward)
        expected_duration = str(self.habit.time_to_complete).split(':')
        expected_duration = (f"{int(expected_duration[0]):02}:{int(expected_duration[1]):02}:"
                             f"{int(expected_duration[2]):02}")
        self.assertEqual(habit_data['time_to_complete'], expected_duration)
        self.assertEqual(habit_data['sign_publicity'], self.habit.sign_publicity)

    def test_habit_update(self):
        """Тест редактирование привычки"""

        url = reverse("healthy_habits:habit-update", args=(self.habit.pk,))
        data = {"action": "Сделать зарядку"}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), "Сделать зарядку")

    def test_habit_delete(self):
        """Тест удаление привычки"""

        url = reverse("healthy_habits:habit-delete", args=(self.habit.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)
