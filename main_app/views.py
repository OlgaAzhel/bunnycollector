from django.shortcuts import render, redirect
from .models import Bunny
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm


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
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'bunnies/detail.html', {'bunny': bunny, 'feeding_form': feeding_form})


class BunnyCreate(CreateView):
    model = Bunny
    fields = '__all__'


class BunnyUpdate(UpdateView):
    model = Bunny
    fields = ['breed', 'description', 'age']


class BunnyDelete(DeleteView):
    model = Bunny
    success_url = '/bunnies'


def add_feeding(request, bunny_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.bunny_id = bunny_id
        new_feeding.save()
    return redirect('detail', bunny_id=bunny_id)
