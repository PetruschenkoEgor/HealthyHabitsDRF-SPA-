from rest_framework import serializers

from healthy_habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'


class HabitPublicSerializer(serializers.ModelSerializer):

    habits_public = serializers.SerializerMethodField()

    def get_habits_public(self):
        """ Публичные привычки. """

        return Habit.objects.filter(sign_publicity=True).values()

    class Meta:
        model = Habit
        fields = '__all__'
