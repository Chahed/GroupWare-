from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from home.forms import *
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from home.models import *
from django.contrib.auth.models import Group


from django.core.urlresolvers import reverse

def index(request):
    ac = Actualite.objects.order_by()
    a1=ac[0]
    a2=ac[1]
    a3=ac[2]
    a4=ac[3]
    return render(request, 'rango/index.html',{'a1':a1,'a2':a2,'a3':a3,'a4':a4})

def inscription(request):

    registered = False


    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True

        else:
            print (user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'rango/inscription.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


def connexion(request):
    global user
    us = Profile.objects.order_by()
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        for i in us :
            if i.user.username==username:
                test=i.confirmation

        if user:
            if user.is_active:
                if test:
                    login(request, user)
                    return HttpResponseRedirect('/home/')
                else :
                    return HttpResponse("Votre compte n'est pas encore confirmé. Vous receverez un e-mail pour vous notifier ça ! ")
            else:
                return HttpResponse("Il y a eu une erreur veuillez essayer de nouveau !!!")
        else:

            return HttpResponse("Saisie incorrect !!!")
    else:
        return render(request, 'rango/connexion.html', {})


def deconnexion(request):
    logout(request)
    return HttpResponseRedirect('/home/')

def cours(request):

    category_list = Cat.objects.order_by()
    usg = Group.objects.get(name="enseignant").user_set.all()


    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return cours(request)
        else:
            print (form.errors)
    else:
        form = CategoryForm()


    return render(request, 'rango/cours.html',{'form':form,'categories': category_list,'usg':usg})



def lire(request, id):
    cati = get_object_or_404(Cat, id=id)

    if request.method == 'POST':
       form = DocForm(data=request.POST)
       if form.is_valid():

            profile = form.save(commit=False)
            profile.category=cati.nom

            if 'docfile' in request.FILES:
                profile.docfile = request.FILES['docfile']

            profile.save()
            form.save()
            return HttpResponseRedirect('/home/cours/')


    else:
        form = DocForm()
    usg = Group.objects.get(name="enseignant").user_set.all()
    category_list = Cat.objects.order_by()
    cours_list = file.objects.order_by()

    test=False
    for c in cours_list :
        if c.category==cati.nom :
            test=True

    return render(request, 'rango/lire.html', {'cati':cati,'categories': category_list,'cours': cours_list, 'form': form,'usg':usg,'test':test},)

def actualiser(request):

    actualite_list = Actualite.objects.order_by()



    if request.method == 'POST':
        form = ActualeForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)

            if 'image' in request.FILES:
                profile.image = request.FILES['image']

            profile.save()
            form.save()
            return HttpResponseRedirect('/home/actualites/')
    else:
        form = ActualeForm()


    return render(request, 'rango/actualites.html',{'form':form,'actualites': actualite_list})


def consulter(request, id):

    actualite = get_object_or_404(Actualite,id=id)

    return render(request, 'rango/actualdetail.html', {'a':actualite})

def participer(request):

    evt_list = Event.objects.order_by()
    usg = Group.objects.get(name="enseignant").user_set.all()


    if request.method == 'POST':
        form = EvenementForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return participer(request)
        else:
            print (form.errors)
    else:
        form = EvenementForm()


    return render(request, 'rango/evenements.html',{'form':form,'a': evt_list,'usg':usg})

def devenirmembre(request, id):
    ev=get_object_or_404(Event,id=id)
    list = Affectation.objects.order_by()
    if request.method == 'POST':
        form = AffectForm(data=request.POST)
        us=Profile.objects.order_by()
        test=False
        if form.is_valid():
            k=form.save(commit=False)
            for i in us :
                if i.user.username==k.name:
                    test=True
            if test:
                k.event=ev.Tiitre
                k.save()
                return rejoindre(request,id)
            else :
                HttpResponse('Votre nom n est pas dans notre base veuillez verfier votre "username" !!')

        else:
            print (form.errors)
    else:
        form = AffectForm()



    return render(request, 'rango/evenementsdetail.html', {'evenement':ev,'form':form,'list':list})

def evtform(request):
    if request.method == 'POST':
        form = EvenementForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return participer(request)
        else:
            print (form.errors)
    else:
        form = EvenementForm()

    return render(request,'rango/evtform.html',{'form':form})

def rejoindre(request,id):
    ev=get_object_or_404(Event,id=id)
    list = Affectation.objects.order_by()
    us = Profile.objects.order_by()
    tache = Taches.objects.order_by()
    taches=[]

    for a in tache :
        if a.event==ev.Tiitre:
            taches.append(a)

    t=taches[len(taches)-1]
    for i in us :
        if i.user.username==ev.Organisateur:
             m=i

    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():

             k=form.save()
             k.event=ev.Tiitre
             k.save()
             return HttpResponse('Tache changée, Retournez a la page précédente!!')
        else:
            print (form.errors)
    else:
        form = TacheForm()

    return render(request,'rango/rejoindre.html',{'ev':ev,'list':list,'us':us,'taches':taches,'form':form,'t1':t,'m':m})