from rest_framework.generics import CreateAPIView

from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """Регистрация пользователя."""

    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Переопределяем логику сохранения пользователя."""

        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
