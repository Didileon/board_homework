
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from config.views import AdvertDelete

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('profile/', include("profiles.urls")),
    # path('http://127.0.0.1:8000/<slug:category>/<slug:slug>/delete/', AdvertDelete.as_view(), name='advert_delete'),
    path('', include("config.urls")),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)