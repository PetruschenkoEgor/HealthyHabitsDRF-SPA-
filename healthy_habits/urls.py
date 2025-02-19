from django.urls import path

from healthy_habits.apps import HealthyHabitsConfig
from healthy_habits.views import (HabitCreateAPIView, HabitDestroyAPIView, HabitListAPIView, HabitPublicAPIView,
                                  HabitRetrieveAPIView, HabitUpdateAPIView)

app_name = HealthyHabitsConfig.name

urlpatterns = [
    path("habits/create/", HabitCreateAPIView.as_view(), name="habit-create"),
    path("habits/", HabitListAPIView.as_view(), name="habit-list"),
    path("habits/publicity/", HabitPublicAPIView.as_view(), name="habit-public-list"),
    path("habits/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit-get"),
    path("habits/<int:pk>/edit/", HabitUpdateAPIView.as_view(), name="habit-update"),
    path("habits/<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="habit-delete"),
]
