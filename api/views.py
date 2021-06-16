from rest_framework.generics import ListAPIView

from Newssite.models import NewsModel
from api.serializers import NewsModelSerializer


class NewsListAPIView(ListAPIView):
    serializer_class = NewsModelSerializer
    queryset = NewsModel.objects.all()

