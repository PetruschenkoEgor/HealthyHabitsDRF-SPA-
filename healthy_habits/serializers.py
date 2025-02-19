from rest_framework import serializers

from healthy_habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = "__all__"


class HabitPublicSerializer(serializers.Serializer):

    habits_public = serializers.SerializerMethodField()

    def get_habits_public(self, obj):
        """Публичные привычки."""

        habit_publicity = Habit.objects.filter(sign_publicity=True)
        return HabitSerializer(habit_publicity, many=True).data
