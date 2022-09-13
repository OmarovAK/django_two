from django.urls import path
from .views import pagin_view

app_name = 'paginat'
urlpatterns = [
    path('', pagin_view, name='pagin_list'),
   ]
