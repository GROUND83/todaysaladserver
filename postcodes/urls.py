
from django.urls import path
from . import views

app_name = "postcodes"


urlpatterns = [
    path("", views.ListPostcodeView.as_view()),
]
