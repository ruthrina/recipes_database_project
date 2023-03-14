from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='home'),
    path('entrees/',views.entree_page,name='entrees'),
    path('desserts/',views.desserts_page,name='desserts'),
    path('add_recipe/',views.add_recipe,name='add_recipe'),
    path('appetizers/',views.appetizers,name='appetizers'),
]