from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import NewsModel
from datetime import datetime
from .filters import NewsFilter
from .forms import NewsForm
from django.contrib.auth.mixins import PermissionRequiredMixin




class NewsViews(ListView):
    model = NewsModel
    template_name = 'flatpages/news.html'
    context_object_name = 'news'
    queryset = NewsModel.objects.order_by('-dateCreation')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context[
            'value1'] = None
        return context

class Post(DetailView):
    model = NewsModel
    template_name = 'flatpages\post.html'
    context_object_name = 'post'

class NewsUpdateView(UpdateView):

    template_name = 'flatpages/news_update.html'
    form_class = NewsForm
    context_object_name = 'update'

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return NewsModel.objects.get(pk=id)


# дженерик для удаления товара
class NewsDeleteView(DeleteView):

    template_name = 'flatpages/news_delete.html'
    queryset = NewsModel.objects.all()
    success_url = '/news/'
    context_object_name = 'news_delete'

# дженерик для получения деталей о товаре
class NewsDetailView(DetailView):
    template_name = 'flatpages/news_detail.html'
    queryset = NewsModel.objects.all()
    context_object_name = 'news_detail'

# дженерик для создания объекта. Надо указать только имя шаблона и класс формы, который мы написали в прошлом юните. Остальное он сделает за вас
class NewsCreateView(CreateView):

    template_name = 'flatpages/news_create.html'
    form_class = NewsForm
    context_object_name = 'news_create'

