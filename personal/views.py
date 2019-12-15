from django.shortcuts import render

def index(request):
    return render(request, 'personal/main.html')

def O_nama(request):
    return render(request, 'personal/O_nama.html')

def Lokacije(request):
    return render(request, 'personal/Lokacije.html')

def Cenovnik(request):
    return render(request, 'personal/Cenovnik.html')

def Konsultacije(request):
    return render(request, 'personal/Konsultacije.html')

def Kontakt(request):
    return render(request, 'sendemail/Kontakt.html')

def kursevi(request):
    return render(request, 'personal/kursevi.html')

def Priprema_za_ispit(request):
    return render(request, 'personal/Priprema_za_ispit.html')

def Statisticke_analize_podataka(request):
    return render(request, 'personal/Statisticke_analize_podataka.html')

def Ucenje_na_daljinu(request):
    return render(request, 'personal/Ucenje_na_daljinu.html')

def success(request):
    return render(request, 'sendemail/success.html')


