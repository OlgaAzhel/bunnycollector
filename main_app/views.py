import uuid
import boto3
from django.shortcuts import render, redirect
from .models import Bunny, Toy, Photo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm
import os

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
    # Get the toys the bunny doesn't have...
    # Create a list of the toy ids that the bunny DOES have
    id_list = bunny.toys.all().values_list('id')
    # Now we can query for toys whose ids are not in the list using exclude
    toys_bunny_doesnt_have = Toy.objects.exclude(id__in=id_list)
    return render(request, 'bunnies/detail.html', {'bunny': bunny, 'feeding_form': feeding_form, 'toys':toys_bunny_doesnt_have})


class BunnyCreate(CreateView):
    model = Bunny
    fields = ['name', 'breed', 'description', 'age']


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


class ToyList(ListView):
  model = Toy


class ToyDetail(DetailView):
  model = Toy


class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'


class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']


class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'


def assoc_toy(request, bunny_id, toy_id):
    # Note that you can pass a toy's id instead of the whole toy object
  Bunny.objects.get(id=bunny_id).toys.add(toy_id)
  return redirect('detail', bunny_id=bunny_id)


def remove_toy(request, bunny_id, toy_id):
    # Note that you can pass a toy's id instead of the whole toy object
  Bunny.objects.get(id=bunny_id).toys.remove(toy_id)
  return redirect('detail', bunny_id=bunny_id)


# Each file uploaded to S3 must have a unique URL.
# We'll be "building" this unique URL using:
# The S3_BASE_URL
# The S3_BUCKET and ...
# A randomly generated string known as the "key"
def add_photo(request, bunny_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + \
        photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to bunny_id or bunny (if you have a bunny object)
            Photo.objects.create(url=url, bunny_id=bunny_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', bunny_id=bunny_id)