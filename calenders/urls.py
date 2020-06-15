from rest_framework.routers import DefaultRouter
from . import views

app_name = "calenders"

router = DefaultRouter()
router.register(r"day", views.CalendersViewSet)
router.register(r"month", views.CalenderMonthViewSet)
urlpatterns = router.urls
