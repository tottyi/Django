from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from . models import *
from . models import Produkt
from django.db.models import Q
# Create your views here.

def home(request):

    produkty = Produkt.objects.all()

    return render(request, 'home.html', {'key': produkty })

def registracia(request):

    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        ageold = request.POST.get('ageold')

    reg = Registracia(firstname=firstname, lastname=lastname, ageold=ageold)
    reg.save()

    return redirect('home')

def about(request):

    if 'q' in request.GET:
        q = request.GET['q']
        contact_list = Produkt.objects.filter(Q(nazov__icontains=q) | Q(partnumber__icontains=q) | Q(cena__icontains=q))
    else:
        contact_list = Produkt.objects.all()

    
    paginator = Paginator(contact_list, 15) # Show 25 contacts per page.

    nazov = Produkt.objects.filter(nazov='some value').order_by('-nazov')
    #nazov_ = Produkt.objects.all().order_by(nazov__icontains='html')
    partnumber = Produkt.objects.all().order_by('partnumber')
    cena = Produkt.objects.all().order_by('cena')
    cena_ = Produkt.objects.all().order_by('-cena')

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'about.html', {'page_obj': page_obj, 'nazov': nazov})

def products(request):

    produkty = Produkt.objects.all()

    return render(request, 'peoples.html', { 'key': produkty})

def peoples(request):

    peoples = Registracia.objects.all()

    return render(request, 'peoples.html', { 'key_peoples': peoples})