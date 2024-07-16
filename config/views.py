from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView
from .filters import AdvertFilter

from .models import Advert
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class AdvertList(ListView):
    """Все объявления"""
    model = Advert
    context_object_name = 'advert'
    queryset = Advert.objects.all()
    template_name = 'board/advert-list.html'
    paginate_by = 3


    # Переопределяем функцию получения списка товаров


def get_queryset(self):
    # Получаем обычный запрос
    queryset = super().get_queryset()
    # Используем наш класс фильтрации.
    # self.request.GET содержит объект QueryDict, который мы рассматривали
    # в этом юните ранее.
    # Сохраняем нашу фильтрацию в объекте класса,
    # чтобы потом добавить в контекст и использовать в шаблоне.
    self.filterset = AdvertFilter(self.request.GET, queryset)
    # Возвращаем из функции отфильтрованный список товаров
    return self.filterset.qs


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    # Добавляем в контекст объект фильтрации.
    context['filterset'] = self.filterset
    return context

class AdvertDetail(DetailView):
    """Подробно об объявлении"""
    model = Advert
    context_object_name = "advert"
    template_name = 'board/advert-detail.html'


class AdvertDelete(PermissionRequiredMixin, DeleteView):
    #permission_required = ('board.delete_advert', )
    model = Advert
    template_name = 'delete.html'
    success_url = 'http://127.0.0.1:8000'
