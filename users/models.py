from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""

    username = None

    email = models.EmailField(unique=True, verbose_name="Email", help_text="Укажите email")
    phone = models.CharField(max_length=15, verbose_name="Телефон", help_text="Укажите телефон", blank=True, null=True)
    avatar = models.ImageField(
        upload_to="users_avatars", verbose_name="Аватар", help_text="Загрузите аватар", blank=True, null=True
    )
    tg_chat_id = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Телеграм chat-id", help_text="Укажите телеграм chat-id"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_set",
        related_query_name="custom_user",
        blank=True,
        help_text="Группы, к которым принадлежит этот пользователь. Пользователь получит все разрешения, "
                  "предоставленные для каждой из своих групп.",
        verbose_name="Группы",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_set",
        related_query_name="custom_user",
        blank=True,
        help_text="Определенные разрешения для этого пользователя.",
        verbose_name="Права пользователя",
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
