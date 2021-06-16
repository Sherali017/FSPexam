from django.db import models

from categories.models import CategoryModel


class NewsModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()

    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, related_name='news', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'new'
        verbose_name_plural = 'news'


class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    comment = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
