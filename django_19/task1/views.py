from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.
def sign_up_by_django(request):
    info = {}
    users = []
    buyers = Buyer.objects.all()
    for b in buyers:
        users.append(b.name)

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                info['error'] = "Пароли не совпадают"
            elif int(age) < 18:
                info['error'] = "Вы должны быть старше 18"
            elif username in users:
                info['error'] = "Пользователь уже существует"
            else:
                info['error'] = ''
            if not info['error']:
                Buyer.objects.create(name=username, balance = 1000.00, age = age)
                info['success'] = f"Приветствуем, {username}!"
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'registration_page.html', context = info)

def index(request):
    return render(request, 'index.html')

def catalog(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'catalog.html', context)

def help(request):
    return render(request, 'help.html')