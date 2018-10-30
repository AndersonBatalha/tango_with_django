from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from ..models import Category

def add_like(request, cat_id):
    cat_like = Category.objects.get(pk=cat_id)

    cat_like.likes += 1
    cat_like.views -= 1
    cat_like.save()

    return HttpResponseRedirect(reverse('show_category', args=[cat_like.slug]))