from rest_framework.routers import DefaultRouter
from . import views

app_name = "destinations"

router = DefaultRouter()
router.register("", views.DestinationViewSet)
urlpatterns = router.urls
