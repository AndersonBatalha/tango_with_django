from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from ..models import Page

def track_url(request, page_id):
    if request.method == "GET":
        try:
            page = Page.objects.get(id=page_id)
            url = page.url

            page.views += 1
            page.save()

        except Page.DoesNotExist:
            url = reverse('index')

    return redirect(url)


