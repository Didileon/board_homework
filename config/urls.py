from django.urls import path
from .views import *


urlpatterns = [
    path('', AdvertList.as_view(), name="advert-list"),
    path("<slug:category>/<slug:slug>/", AdvertDetail.as_view(), name="advert-detail"),
    path('<slug:category>/<slug:slug>/delete/', AdvertDelete.as_view(), name='advert_delete'),


]