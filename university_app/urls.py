from .views import index, new_data
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('new_data', new_data, name='new_data'),
]