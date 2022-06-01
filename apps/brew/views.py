from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery,SearchRank
from django.views.generic import ListView
import json
from django.core import serializers
#from django.utils.safestring import make_safe
from django.utils.html import mark_safe
from .models import Brew, Recipie
from apps.roast.models import Roast
from .forms import AddBrew, AddBrewRecipie
from django.urls import reverse_lazy

# Create your views here.

def brew_landing(request):
    brews = Brew.objects.all().order_by('brewDate')
    #roasts = Roast.objects.all().order_by('name')

    if request.GET.get('search'):
        keywords = request.GET.get('search')
        query = SearchQuery(keywords)

        brew_vector = SearchVector('brew_method', 'roastID__name')

        brews = brews.annotate(search=brew_vector).filter(search=query)
        brews = brews.annotate(rank=SearchRank(brew_vector, query)).order_by('-rank')


    return render(request, 'brew/brew_landing.html', {'brews': brews})

@login_required(login_url="/users/login/")
def brew_add (request):
    if request.method == 'POST':
        #roastID = request.POST.get('roastID')
        form = AddBrew(request.POST, request.FILES)
        #return HttpResponse(form.errors)
        if form.is_valid():
            #save to Database
            brew = form.save(commit=False)
            brew.userID = request.user
            brew_slug = brew.save()
            #success_url = reverse_lazy(+'/details/'+)
            return redirect('apps.brew:brew_details', slug=brew_slug) #redirect to detail page of the brew using the
        else:
            return HttpResponse(form.errors)
    else:
        roast_objects = Roast.objects.all()
        #json_serializer = json.Serializer()
        roasts_json = []
        for object in roast_objects:
            roasts_json.append(
                {
                    'id': object.id,
                    'name': object.name
                }
            )
        roasts_json = mark_safe(serializers.serialize("json", roast_objects, fields = ("id", "name")))
        form = AddBrew()
    return render(request, 'brew/brew_add.html', {'form': form, 'roasts': roasts_json})
#@login_required(login_url="/users/login/")


def brew_details(request, slug):
    brew = Brew.objects.get(slug=slug)
    if brew:
        recipies = Recipie.objects.filter(brewID=brew)
    else:
        recipies = []

    if request.method == 'POST':
        if request.POST.get('bestRecipieID'):
            bestrecipie = recipies.get(id=request.POST.get('bestRecipieID'))
            brew.bestRecipieID = bestrecipie
            brew.save()
            #return HttpResponse("saved best recipie id")
        else:
            form = AddBrewRecipie(request.POST, request.FILES)
            if form.is_valid():
                recipie = form.save(commit=False)
                recipie.brewID = brew
                recipie.save()
                recipies = Recipie.objects.filter(brewID=brew)
                form = AddBrewRecipie()
            #success_url = reverse_lazy(+'/details/'+)
            #return HttpResponse(status=204) #tells the browser to not change the current page, because no new content has been returned.
        #else:
            #return HttpResponse(form.errors)

    form = AddBrewRecipie()
    context = {
        'brew': brew,
        'recipies': recipies,
        'form': form,
    }
    return render(request, 'brew/brew_details.html', context)
