"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from .views import About, RangoIndex, ShowCategory, AddCategory, AddPage

urlpatterns = [
    url(r'^$', RangoIndex.as_view(), name='rango_index'),
    url(r'^about/', About.as_view(), name='about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', ShowCategory.as_view(), name='show_category'),
    url(r'^add_category/', AddCategory.as_view(), name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page', AddPage.as_view(), name='add_page'),
    # url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page', views.add_page, name='add_page'),
]
