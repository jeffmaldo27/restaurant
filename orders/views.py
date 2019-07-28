from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Min, Count
from .models import Entree, Category

# Create your views here.
'''
def index(request):
    entrees = Entree.objects.get(pk=5)
    yooo = entrees.addons.all()
    x = []
    for item in yooo:
        x.append(item.name)
    #context = {
     #   "Entrees": entrees.name,
        #"Addons": addons
    #}
    #print("hello")
    #return render(request, "orders/index.html", context)
    return HttpResponse("Project 3: TODO")
'''
# Create your views here.
@login_required
def index(request):
    context = {
        #"entrees": Category.objects.values('name'),
        "entrees": Category.objects.all()
        #"highPrice": Entree.objects.all().aggregate(Max('price')),
        #"lowPrice": Entree.objects.all().aggregate(Min('price'))
    }
    return render(request, "orders/index.html", context)

def entree(request, entree_id):
    try:
        entree = Entree.objects.filter(category=entree_id)
    except Entree.DoesNotExist:
        raise Http404("Entree does not exist")
    context = {
        "entree": entree,
        #"addons": entree.addons.all()
    }   
    '''
    try:
        entree = Entree.objects.get(pk=entree_id)
    except Entree.DoesNotExist:
        raise Http404("Entree does not exist")
    context = {
        "entree": entree,
        "addons": entree.addons.all()
    }
    '''
    return render(request, "orders/entree.html", context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
    form = UserCreationForm
    return render(request, "registration/register.html", context={"form":form})