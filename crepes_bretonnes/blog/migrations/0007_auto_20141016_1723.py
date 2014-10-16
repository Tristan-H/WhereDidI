# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20141016_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pseudo', models.CharField(max_length=20)),
                ('fb', models.CharField(max_length=30, null=True)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='article',
            name='categorie',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Categorie',
        ),
        migrations.RemoveField(
            model_name='offre',
            name='produit',
        ),
        migrations.RemoveField(
            model_name='offre',
            name='vendeur',
        ),
        migrations.RemoveField(
            model_name='vendeur',
            name='produits',
        ),
        migrations.DeleteModel(
            name='Produit',
        ),
        migrations.DeleteModel(
            name='Offre',
        ),
        migrations.DeleteModel(
            name='Vendeur',
        ),
        migrations.RemoveField(
            model_name='voiture',
            name='moteur',
        ),
        migrations.DeleteModel(
            name='Moteur',
        ),
        migrations.DeleteModel(
            name='Voiture',
        ),
        migrations.AddField(
            model_name='group',
            name='list_user',
            field=models.ManyToManyField(to='blog.User'),
            preserve_default=True,
        ),
    ]
