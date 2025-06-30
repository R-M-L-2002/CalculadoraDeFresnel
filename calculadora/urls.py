from django.urls import path
from .views import fresnel_view

urlpatterns = [
    path('', fresnel_view, name='fresnel'),
]
