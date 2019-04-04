from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Pet

# Create your views here.
def home(req):
    pets = Pet.objects.all()
    # return HttpResponse('<p>Home view</p>')
    return render(req, 'home.html', {'pets': pets})

def pet_detail(req, id):
    try:
        pet = Pet.objects.get(id = id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(req, 'pet_detail.html', {'pet': pet})