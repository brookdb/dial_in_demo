from django.shortcuts import render, redirect
from .models import Roast
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery,SearchRank
from django.views.generic import ListView
from django.core import serializers
from .import forms

# Create your views here.
def roast_landing(request):

    # = Roast.objects.all()
    roasts = Roast.objects.all().order_by('name')
    featured_roasts = Roast.objects.filter(is_featured=True).order_by('name');
    if request.GET.get('search'):
        keywords = request.GET.get('search')
        print(keywords)
        query = SearchQuery(keywords)
        #vector = SearchVector('name', 'region', 'producer')
        search_vector = SearchVector("name", weight="A")+SearchVector("process", weight="A")+SearchVector("region", weight="C")+SearchVector("producer", weight="B")
        #roasts = roasts.annotate(search=vector).filter(search=query)
        #roasts = roasts.annotate(rank=SearchRank(vector, query)).order_by('-rank')
        rank = SearchRank(search_vector, query, weights=[0.4,0.6,0.8,1.0])
        roasts = Roast.objects.annotate(rank=rank).filter(rank__gte=0.4).order_by("-rank")
    #return qs
    return render(request, 'roast/roast_landing.html', {'roasts': roasts, 'featured_roasts':featured_roasts})

def roast_detail(request, slug):
    #return HttpResponse(slug)
    roast = Roast.objects.get(slug=slug)
    roast_id = roast.id
    return render(request, 'roast/roast_detail.html', {'roast': roast,})

def roast_search(request):
    if request.method == 'POST':
        query = request.POST.get("q")
        data = Roast.objects.annotate(search=SearchVector("name", "region", "producer")).filter(search=query)
        roast = serializers.serialize("json", data)
        return render(request, 'roast/roast_search.html', {'roast': roast,})
    else:
        return render(request,'roast/roast_search.html')


@login_required(login_url="/users/login/")
def roast_add (request):
    if request.method == 'POST':
        form = forms.AddRoast(request.POST, request.FILES)
        if form.is_valid:
            #save to Database
            form.save()
            return redirect('apps.roast:roast_landing')
    else:
        form = forms.AddRoast()
    return render(request, 'roast/roast_add.html', {'form': form})
