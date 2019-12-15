from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^O_nama/$', views.O_nama, name='O_nama'),
    url(r'^Lokacije/$', views.Lokacije, name='Lokacije'),
    url(r'^Cenovnik/$', views.Cenovnik, name='Cenovnik'),
    url(r'^Konsultacije/$', views.Konsultacije, name='Konsultacije'),
    url(r'^kursevi/$', views.kursevi, name='kursevi'),
    url(r'^Priprema_za_ispit/$', views.Priprema_za_ispit, name='Priprema_za_ispit'),
    url(r'^Statisticke_analize_podataka/$', views.Statisticke_analize_podataka, name='Statisticke_analize_podataka'),
    url(r'^Ucenje_na_daljinu/$', views.Ucenje_na_daljinu, name='Ucenje_na_daljinu'),
    url(r'^sendemail/Kontakt/$', views.Kontakt, name='Kontakt'),
    url(r'^sendemail/success/$', views.success, name='success'),
]
