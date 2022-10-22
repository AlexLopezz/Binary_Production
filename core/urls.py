from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeRest

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', HomeRest.as_view(), name="homeRest"),
    path('', include('applications.product.urls')),
    path('', include('applications.user.urls')),
    path('', include('applications.pdftoHtml.urls')),
    path('', include('applications.opinions.urls')),
    path('', include('applications.reservation.urls')),
    path('', include('applications.contact.urls')),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)