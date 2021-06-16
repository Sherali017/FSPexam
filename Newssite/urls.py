from django.urls import path

from Newssite.views import NewsListView, NewsDetailView

app_name ='Newssite'

urlpatterns = [
    path('', NewsListView.as_view(), name = 'list'),
    path('categories/<int:pk>', NewsListView.as_view(), name = 'category'),
    path('news/<int:pk>', NewsDetailView.as_view(), name = 'detail')

]
