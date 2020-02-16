from django.urls import path, include
from .views import TalkViewBase
from django.conf import settings
from django.conf.urls.static import static

app_name = 'talk'
urlpatterns = [
    path('', TalkViewBase.as_view(), name='list'), #urlの作り込み, classはas_viewをつける
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
