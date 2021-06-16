from django.db import models

class CategoryModel(models.Model):
    title =models.CharField(max_length=150)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'