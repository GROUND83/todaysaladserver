from rest_framework.routers import DefaultRouter
from . import views

app_name = "fooddiary"

router = DefaultRouter()
router.register("", views.FooddiaryViewSet)
urlpatterns = router.urls
