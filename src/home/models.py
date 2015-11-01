from django.db import models
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify



class Profile(models.Model):
    user = models.OneToOneField(User)
    confirmation=models.BooleanField(default=False)
    Nom=models.CharField(max_length=120)
    Prenom=models.CharField(max_length=120)
    adresse=models.CharField(max_length=128)
    Tel=models.IntegerField()
    def __str__(self):
        return self.user.username



class Cat(models.Model):
    nom = models.CharField(max_length=30,unique=True)




    def __str__(self):
        return self.nom

class Actualite(models.Model):
    titre = models.CharField(max_length=150)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    url = models.URLField(default=0)
    image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    #views = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de parution")
    category = models.ForeignKey('Category')
    category = models.CharField(max_length=100)


    def __str__(self):
        """
        la classe Actualite nous permet de definir une table de donnees
        qui contient les differentes actualites visees par l'administration
        de notre site accessibles par les membres et les visiteurs web
        """
        return self.titre


class Event(models.Model):
    Tiitre=models.CharField(max_length=50)
    Appercu=models.TextField()
    Organisateur = models.CharField(max_length=100)
    Duree = models.CharField(max_length=42)
    Pre_requis = models.TextField(null=True,max_length=200)
    Programme = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name="Date de parution",null=True)
    #url = models.URLField(default=0)
    #views = models.IntegerField(default=0)


class file(models.Model):
    titre = models.CharField(max_length=100,null=True)
    auteur = models.CharField(max_length=42,null=True)
    contenu = models.TextField(null=True)
    docfile = models.FileField(upload_to ='files/',blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name="Date de parution",null=True)
    category = models.ForeignKey('Cat')
    category = models.CharField(max_length=100,null=True)
    def __str__(self):
       return self.titre


class Affectation(models.Model):
    name=models.CharField(max_length=50)
    event=models.CharField(max_length=50)
    def __str__(self):
       return self.name



class Taches(models.Model):
    event=models.CharField(max_length=50)
    text=models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name="Date de parution",null=True)
    def __str__(self):
       return self.event
