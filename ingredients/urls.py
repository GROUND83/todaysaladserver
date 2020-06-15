
from django.urls import path
from . import views

app_name = "ingredients"


urlpatterns = [
    path("", views.ListIngredientView.as_view()),
    path("<int:pk>/", views.SeeIngredientView.as_view()),

]
