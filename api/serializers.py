from rest_framework import serializers

from Newssite.models import NewsModel


class NewsModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsModel
        fields = '__all__ '