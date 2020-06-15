
from django.urls import path
from . import views

app_name = "easyfood"


urlpatterns = [
    path("", views.ListEasyFoodView.as_view()),
    path("<int:pk>/", views.SeeEasyFoodView.as_view()),
]
