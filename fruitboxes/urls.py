
from django.urls import path
from . import views

app_name = "fruitebox"


urlpatterns = [
    path("", views.ListFruitboxView.as_view()),
    path("<int:pk>/", views.SeeFruitboxView.as_view()),
]
