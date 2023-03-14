from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.




def index(request):
    return render(request,'home.html')


def entree_page(request):
    return render(request,'Entrees.html')


def desserts_page(request):
    return render(request,'desserts.html')


def appetizers(request):
    return render(request,'appetizers.html')


def add_recipe(request):
    return render(request,'add_recipe.html')

