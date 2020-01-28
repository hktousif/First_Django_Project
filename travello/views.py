from django.shortcuts import render

# Create your views here.
from travello.models import Destination


def index(request):
    dest = Destination.objects.all()
    return render(request, 'index.html', {'dest': dest})



