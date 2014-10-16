#-*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
def home(request):
  text = """<h1>Bienvenue sur mon blog !</h1> </br> <p> palpalpala <p>"""
  return HttpResponse(text)

def view_article(request, id_article):
    if int(id_article) > 100: #Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
        raise Http404
    return redirect('redirection')

def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """
    text = "Vous avez demandé les articles de {0} {1}.".format(year, month)
    return HttpResponse(text)

def view_redirection(request):
    return HttpResponse(u"Vous avez été redirigé.")

def tpl(request):
    return render(request, 'blog/tpl.html', {'current_date': datetime.now()})

def addition(request, nombre1, nombre2):	
    total = int(nombre1) + int(nombre2)

    # retourne nombre1, nombre2 et la somme des deux
    return render(request, 'blog/addition.html', locals())