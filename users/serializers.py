from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор для пользователя. """

    class Meta:
        model = User
        fields = ['email', 'phone', 'avatar', 'tg_chat_id', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """ Создание пользователя с хэшированным паролем. """

        user = User.objects.create_user(**validated_data)
        return user
