from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.forms, name='forms'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.ObservationMap.as_view(), name='observation-map'),
    path('forms/<int:pk>', views.ObservationMap.as_view(), name='observation-map')
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)