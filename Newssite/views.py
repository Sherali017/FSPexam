from django.shortcuts import render

from math import ceil

from django.db.models import Q
from django.views.generic import ListView, DetailView

from Newssite.models import NewsModel


class NewsListView(ListView):
    template_name = 'mainnews.html'
    model = NewsModel
    paginate_by = 3



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = ceil(NewsModel.objects.count() / self.paginate_by)
        context['range'] = range(x)

        return context


class NewsDetailView(DetailView):
    template_name = 'details.html'
    model =  NewsModel
    queryset = NewsModel.objects.all()
