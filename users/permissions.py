from rest_framework import permissions


class IsOwnerUser(permissions.BasePermission):
    """Если пользователь владелец профиля."""

    def has_permission(self, request, view):
        # Проверяем, что пользователь аутентифицирован
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Проверяем, что пользователь является владельцем объекта
        return obj.user == request.user
