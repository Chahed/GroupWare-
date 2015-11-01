__author__ = 'Hedi Chahed'
from django import forms
from home.models import *
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ('username', 'email', 'password','groups')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('Nom','Prenom','adresse','Tel')

class CategoryForm(forms.ModelForm):
    nom = forms.CharField(max_length=128)

    class Meta:
        model = Cat
        fields = ('nom',)


class ActualeForm(forms.ModelForm):
    class Meta:
        model = Actualite
        fields = ('titre','auteur','contenu','image')



class DocForm (forms.ModelForm):

     class Meta:
        model= file
        fields = ('titre','auteur','contenu','docfile',)

class EvenementForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('Tiitre','Organisateur','Appercu','Duree','Pre_requis','Programme')
class AffectForm(forms.ModelForm):
    class Meta:
        model=Affectation
        fields=('name',)

class TacheForm(forms.ModelForm):
     class Meta:
        model=Taches
        fields=('text',)