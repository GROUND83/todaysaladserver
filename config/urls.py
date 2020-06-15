from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import os

def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path(os.environ.get("DJANGO_ADMIN". "admin/"), admin.site.urls),
    path("api/v1/users/", include("users.urls")),
    path("api/v1/calender/", include("calenders.urls")),
    path("api/v1/salad/", include("salads.urls")),
    path("api/v1/ingredient/", include("ingredients.urls")),
    path("api/v1/events/", include("events.urls")),
    path("api/v1/order/", include("orders.urls")),
    path("api/v1/fooddiary/", include("fooddiarys.urls")),
    path("api/v1/fruitebox/", include("fruitboxes.urls")),
    path("api/v1/easyfood/", include("easyfoods.urls")),
    path("api/v1/postcode/", include("postcodes.urls")),
    path("api/v1/destinations/", include("destinations.urls")),
    path("sentry-debug/", trigger_error),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
