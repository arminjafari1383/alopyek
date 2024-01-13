from django.urls import path
from .views import index,html


urlpatterns = [
    path('', index , name='index'),
    path('html', html,name='html'),
    
]