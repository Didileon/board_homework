
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
#from config.views import AdvertDelete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('profile/', include("profiles.urls")),
    #path('<url>/delete/', AdvertDelete.as_view(), name='advert_delete'),
    path('', include("config.urls")),
    #path('<url>/delete/', AdvertDelete.as_view(), name='advert_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)