from django.urls import path, include
from .views import talk
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('a/', talk),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
