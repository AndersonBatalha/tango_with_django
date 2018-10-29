from django.http import HttpResponse

from ..models import Category

def add_like(request, cat_id):

    cat_like = Category.objects.get(pk=cat_id)

    print (cat_like)


    return HttpResponse(cat_like)