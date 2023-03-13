from django.shortcuts import render

# Create your views here.

bunnies = [
    {'name': 'Cinnabun', 'breed': 'Holland Lop',
        'description': 'adorable bundle of joy', 'age': 3},
    {'name': 'Truffle', 'breed': 'Lionhead',
        'description': 'energetic little fluff ball', 'age': 2},
]


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def bunnies_index(request):
    return render(request, 'bunnies/index.html', {'bunnies': bunnies})
