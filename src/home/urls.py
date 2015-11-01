from django.conf.urls import patterns, url
from home import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='home'),
        url(r'^inscription/$', views.inscription, name='inscription'),
         url(r'^connexion/$', views.connexion, name='connexion'),
         url(r'^deconnexion/$', views.deconnexion, name='deconnexion'),
         url(r'^cours/$', views.cours, name='cours'),

         url(r'^cours/(?P<id>\d+)$', views.lire),
          url(r'^actualites/$', views.actualiser, name='actualites'),
         url(r'^actualites/(?P<id>\d+)/$', views.consulter),
          url(r'^evenements/(?P<id>\d+)/$', views.devenirmembre),
          url(r'^evenements/rejoindre/(?P<id>\d+)$', views.rejoindre),
         url(r'^evenements/$', views.participer, name='evenements'),
         url(r'^evenements/ajout/$', views.evtform, name='evtform'),
         )