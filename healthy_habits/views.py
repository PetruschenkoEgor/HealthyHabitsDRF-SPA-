from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView

from healthy_habits.models import Habit
from healthy_habits.serializers import HabitSerializer, HabitPublicSerializer


class HabitCreateAPIView(CreateAPIView):
    """ Создание привычки. """

    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """ Устанавливаем владельца привычки. """

        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitListAPIView(ListAPIView):
    """ Список привычек текущего пользователя. """

    serializer_class = HabitSerializer

    def get_queryset(self):
        """ Возвращает список привычек текущего пользователя. """

        return Habit.objects.filter(user=self.request.user)


class HabitPublicAPIView(ListAPIView):
    """ Список публичных привычек """

    queryset = Habit.objects.all()
    serializer_class = HabitPublicSerializer


class HabitRetrieveAPIView(RetrieveAPIView):
    """ Информация о привычке. """

    serializer_class = HabitSerializer

    def get_queryset(self):
        """ Возвращает список привычек текущего пользователя. """

        return Habit.objects.filter(user=self.request.user)


class HabitUpdateAPIView(UpdateAPIView):
    """ Редактирование привычки. """

    serializer_class = HabitSerializer

    def get_queryset(self):
        """ Возвращает список привычек текущего пользователя. """

        return Habit.objects.filter(user=self.request.user)


class HabitDestroyAPIView(DestroyAPIView):
    """ Удаление привычки. """

    serializer_class = HabitSerializer

    def get_queryset(self):
        """ Возвращает список привычек текущего пользователя. """

        return Habit.objects.filter(user=self.request.user)
