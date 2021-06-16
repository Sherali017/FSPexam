from django.urls import path

from api.views import NewsListAPIView

app_name = 'api'

urlpatterns = [
    path('News/', NewsListAPIView.as_view())
]