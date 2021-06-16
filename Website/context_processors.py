from categories.models import CategoryModel


def get_categories(request):
    return {
        'categories': CategoryModel.objects.all()
    }