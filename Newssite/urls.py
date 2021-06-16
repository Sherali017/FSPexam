from django.urls import path

from Newssite.views import NewsListView, NewsDetailView, ContactCreateView

app_name ='Newssite'

urlpatterns = [
    path('', NewsListView.as_view(), name = 'list'),
    path('categories/<int:pk>', NewsListView.as_view(), name = 'category'),
    path('news/<int:pk>', NewsDetailView.as_view(), name = 'detail'),
    path('contact/', ContactCreateView.as_view(), name = 'contact' )


]
