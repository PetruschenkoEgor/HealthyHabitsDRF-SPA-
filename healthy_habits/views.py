from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from healthy_habits.models import Habit
from healthy_habits.pagination import HabitPagination
from healthy_habits.serializers import HabitPublicSerializer, HabitSerializer
from users.permissions import IsOwnerUser


class HabitCreateAPIView(CreateAPIView):
    """Создание привычки."""

    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """Устанавливаем владельца привычки."""

        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitListAPIView(ListAPIView):
    """Список привычек текущего пользователя."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        """ Возвращает список привычек текущего пользователя. """

        return Habit.objects.filter(user=self.request.user)


class HabitPublicAPIView(ListAPIView):
    """Список публичных привычек."""

    queryset = Habit.objects.all()
    serializer_class = HabitPublicSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def list(self, request, *args, **kwargs):
        """Убирает дублирование словарей с публичными привычками."""

        serializer = self.get_serializer(self.get_queryset(), many=False)
        return Response(serializer.data)


class HabitRetrieveAPIView(RetrieveAPIView):
    """Информация о привычке."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerUser,]

    def get_queryset(self):
        """ Возвращает список привычек текущего пользователя. """

        if getattr(self, 'swagger_fake_view', False):
            # Возвращаем пустой queryset во время генерации схемы
            return Habit.objects.none()
        return Habit.objects.filter(user=self.request.user)


class HabitUpdateAPIView(UpdateAPIView):
    """Редактирование привычки."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerUser,]

    def get_queryset(self):
        """ Возвращает список привычек текущего пользователя. """

        if getattr(self, 'swagger_fake_view', False):
            # Возвращаем пустой queryset во время генерации схемы
            return Habit.objects.none()
        return Habit.objects.filter(user=self.request.user)


class HabitDestroyAPIView(DestroyAPIView):
    """Удаление привычки."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerUser,]

    def get_queryset(self):
        """ Возвращает список привычек текущего пользователя. """

        if getattr(self, 'swagger_fake_view', False):
            # Возвращаем пустой queryset во время генерации схемы
            return Habit.objects.none()
        return Habit.objects.filter(user=self.request.user)
