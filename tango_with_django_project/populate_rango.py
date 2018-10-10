#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, django, random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tango_with_django_project.settings")
django.setup()

os.system('rm -rf db.sqlite3')
os.system('python manage.py migrate')
os.system('python manage.py makemigrations rango')

from rango.models import Category, Page

categorias = ['Esportes', 'Filmes', 'Política', 'Django', 'Python', 'git', 'Carros', 'Notícias', 'Televisão', 'Educação', 'Tecnologia', 'virtualenv', 'Entretenimento', 'Culinária', 'Rádios', 'Linux', 'Software livre', 'Ubuntu', 'Wine', 'Tutoriais', 'Eleições', 'Redes sociais', 'Podcast', 'Economia', 'E-mail', 'Jogos', 'Copa do Mundo', 'Humor', 'Vídeos', 'Ionic', 'Android', 'Blogs', 'Windows', 'Debian', 'Red Hat', 'Java', 'Flask', 'Bottle', 'Typescript', 'Bootstrap', 'CSS', 'HTML', 'PHP', 'Shell script', 'Redes', 'Matemática', 'Segurança da informação', 'Saúde', 'F1']

def gerar_arquivo_category():
    if os.path.isfile('categories.csv') and len(open('categories.csv', 'r').readlines()) > 0:
        print ("Arquivo categories.csv já existe!")
    else:
        print ("Criando arquivo categories.csv")
        arquivo_cat = open('categories.csv', 'w')
        for categoria in categorias:
            arquivo_cat.write("%s, %d, %d\n" % (categoria, random.randint(1,250), random.randint(1,250)))

def populate():
    categories = open('categories.csv').readlines()

    print('Populating %d categories...' % len(categories))
    for category in categories:
        cat, views, likes = category.rstrip().split(',')
        c = add_cat(cat, views, likes)

    pages = open('pages.csv').readlines()
    print('Populating %d pages...' % len(pages))
    for page in pages:
        cat, title, url = page.rstrip().split(',')
        views = random.randint(1,500)
        c = add_cat(cat)
        ok = add_page(c, title, url, views)

def show():
    # Print out the categories we have added.
    print('Showing pages...')
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} ({1})".format(str(c), str(p)))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    if not c.views:
        c.views = views
    if not c.likes:
        c.likes = likes
    c.save()
    return c


# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    gerar_arquivo_category()
    populate()
    show()
