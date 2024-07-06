from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView
from .models import Advert
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class AdvertList(ListView):
    """Все объявления"""
    model = Advert
    queryset = Advert.objects.all()
    template_name = 'board/advert-list.html'


class AdvertDetail(DetailView):
    """Подробно об объявлении"""
    model = Advert
    context_object_name = "advert"
    template_name = 'board/advert-detail.html'


#class AdvertDelete(PermissionRequiredMixin, DeleteView):
    #permission_required = ('advert-detail.html/delete_advert', )
    #model = Advert
    #template_name = 'board/advert-delete.html'
    #success_url = '/advert/'

