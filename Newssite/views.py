from django.core.mail import send_mail
from django.shortcuts import render, redirect

from math import ceil

from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView

from Newssite.models import NewsModel, ContactModel
from Website import settings


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

class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModel
    success_url = '/'

    def form_valid(self, form):
        obj = form.save()
        text = f'Name: {obj.name}\nEmail:{obj.email}\nMessage: {obj.comment}'
        send_mail(
            'Notification',
            text,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER]

        )
        return redirect(self.success_url)

