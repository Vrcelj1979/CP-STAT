from django.conf.urls import url, include
from . import views

from . import views

urlpatterns = [
    url('Kontakt/', views.KontaktView, name='Kontakt'),
    url('success/', views.successView, name='success'),
]
