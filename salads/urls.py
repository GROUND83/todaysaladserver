
from django.urls import path
from . import views

app_name = "salads"


urlpatterns = [
    path("", views.ListSaladsView.as_view()),
    path("<int:pk>/", views.SeeSaladView.as_view()),
]
