from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from ..models import Category

def like_category(request):
    cat_id = None

    if request.method == "GET":
        cat_id = request.GET['category_id']
        likes = 0

    if cat_id:
        category = Category.objects.get(pk=int(cat_id))

        if category:
            likes = category.likes + 1
            category.likes = likes
            category.save()

    return HttpResponse(likes)