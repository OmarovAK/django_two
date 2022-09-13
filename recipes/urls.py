from django.urls import path
from .views import recipes_view, calcul_view, default_view

app_name = 'recipes'
urlpatterns = [
    path('', default_view, name='home'),
    path('recipes/', recipes_view, name='recipes'),
    path('recipes/<str:name_dish>/', calcul_view),
]
