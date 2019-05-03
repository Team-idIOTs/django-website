from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    title = "index"
    context = {'title': title}
    return render(request, 'cueball/index.html', context)
    
def cues(request):
    title = "cues"
    context = {'title': title}
    return render(request, 'cueball/cues.html', context)
    
def monitor(request):
    title = "monitor"
    context = {'title': title}
    return render(request, 'cueball/monitor.html', context)
    
def settings(request):
    title = "settings"
    context = {'title': title}
    return render(request, 'cueball/settings.html', context)
    