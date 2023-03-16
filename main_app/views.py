from django.shortcuts import render
from .models import Bunny
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def bunnies_index(request):
    bunnies = Bunny.objects.all()
    return render(request, 'bunnies/index.html', {'bunnies': bunnies})

def bunnies_detail(request, bunny_id):
    bunny = Bunny.objects.get(id=bunny_id)
    return render(request, 'bunnies/detail.html', {'bunny': bunny})

class BunnyCreate(CreateView):
    model = Bunny
    fields = '__all__'

class BunnyUpdate(UpdateView):
    model = Bunny
    fields = ['breed', 'description', 'age']


class BunnyDelete(DeleteView):
  model = Bunny
  success_url = '/bunnies'
