from django.urls import path
from . import views
from .views import image_extraction

urlpatterns = [
    path('', views.image_extraction, name='image_extraction' )

]