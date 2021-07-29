from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegisterForm

from products.models import Product




def index(request):
    products = Product.objects.all().order_by('price')
    return render(request, 'index.html', {
        'message' : 'Listado de productos',
        'title' : 'Productos',
        'products' : products,
    })


def login_view(request):

    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))

            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])
            return redirect('index')     
        else:
            messages.error(request, 'El usuario y/o contraseña es incorrecto')


    return render(request, 'users/login.html', {
        
    })


def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('login')


def register_view(request):

    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = User.objects.create_user(username, email, password)
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')


    return render(request, 'users/register.html', {
        'form': form
    })

