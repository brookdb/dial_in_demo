from django.http import HttpResponse
from django.shortcuts import render
from apps.roast.models import Roast


def landing(request):
    #return HttpResponse("landing")
    roasts = Roast.objects.all()
    return render(request, 'pages/landing.html', {'roasts': roasts})
