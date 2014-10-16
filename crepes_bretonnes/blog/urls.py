#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url
urlpatterns = patterns('blog.views',
    url(r'^accueil/$', 'home'),
    url(r'^$', 'tpl'),
    url(r'^redirect/$', 'view_redirection', name ="redirection"),
    url(r'^article/(\d+)/$', 'view_article', name="afficher_article"), # Vue d'un article
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$', 'list_articles'), # Vue des articles d'un mois précis
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', 'addition'), # Vue des articles d'un mois précis
)