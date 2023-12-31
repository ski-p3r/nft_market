from django.contrib import admin
from django.urls import path, include
from . import views

# Media file and Static Configuraton
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage, name="Home"),
    path('auth/', include('accounts.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)