#-*- coding: utf-8 -*-
from django.db import models

class User(models.Model):
    pseudo = models.CharField(max_length=20)
    fb = models.CharField(max_length=30, blank=True)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nom

class Group(models.Model):
    nom = models.CharField(max_length=100)
    list_user = models.ManyToManyField(User)

    def __unicode__(self):
        return self.nom

class Tag(models.Model):
	nom = models.CharField(max_length=20)
	logo = models.CharField(max_length=20)

#class Actions(models.Model):
#	nom = models.CharField(max_length=20)
#	logo = models.CharField(max_length=20)
#	x = models.IntegerField() # regarder si django permet de stocker 
#	x = models.IntegerField()
#	logo = models.CharField(max_length=20)
#	user = models.ForeignKey('User') // ForeignKey ou OneToOneField à vérifier
#   tag 
#   visibilité
#   comment
#   date

#class Challenge
#   chanllenger
#   chanlengé
#   location
#   catch phrase
#   photo
