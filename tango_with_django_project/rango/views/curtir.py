from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from ..models import Category

def curtir(request, cat_slug):
    cat_like = Category.objects.get(slug=cat_slug)

    cat_like.likes += 1
    cat_like.views -= 1
    cat_like.save()

    return HttpResponseRedirect(reverse('show_category', args=[cat_slug]))