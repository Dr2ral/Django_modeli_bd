from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *


# Create your views here.
def main(request):
    title = 'Мой магазин'
    h1 = 'Главная страница'
    context = {
        'title': title,
        'h1': h1
    }
    return render(request, 'platform.html', context)

def game(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'games.html', context)

def cart(request):
    return render(request, 'cart.html')


# Create your views here.

#def sign_up_by_html(request):
#    #users = ['Vladislav', 'Alexander', 'Vitalik']
#    buyers = Buyer.objects.all()
#    users = [buyer.name for buyer in buyers]
#    context = {
#        'users': users
#    }
#    info = {}
#    if request.method == 'POST':
#        username = request.POST.get('username')
#        password = request.POST.get('password')
#        repeat_password = request.POST.get('repeat_password')
#        age = request.POST.get('age')
#        if password == repeat_password and int(age) >= 18 and username not in users:
#            create = Buyer.objects.create(name=username, balance=1203, age=age)
#            return HttpResponse(f"Приветствуем, {create}!")
#        elif password != repeat_password:
#            info['error'] = 'Пароли не совпадают'
#            #return render(request, 'registration_page.html', {'info': info})
#            return HttpResponse(info['error'])
#        elif int(age) < 18:
#            info['error'] = 'Вы должны быть старше 18'
#            return HttpResponse(info['error'])
#        elif username in users:
#            info['error'] = 'Пользователь уже существует'
#            return HttpResponse(info['error'])
#    return render(request, 'registration_page.html', {'info':info, 'users':users})




def sign_up_by_django(request):
    buyers = Buyer.objects.all()
    users = [buyer.name for buyer in buyers]
    context = {
        'users': users
    }
    if request.method == 'POST':
        info = UserRegister(request.POST)
        if info.is_valid():
            username = info.cleaned_data['username']
            password = info.cleaned_data['password']
            repeat_password = info.cleaned_data['repeat_password']
            age = info.cleaned_data['age']
            if password == repeat_password and int(age) >= 18 and username not in users:
                create = Buyer.objects.create(name=username, balance=600, age=age)
                return HttpResponse(f"Приветствуем, {create}!")
            if password != repeat_password:
                return HttpResponse('Пароли не совпадают')
            elif int(age) < 18:
                return HttpResponse('Вы должны быть старше 18')
            elif username in users:
                return HttpResponse('Пользователь уже существует')

    else:
        UserRegister()
    return render(request, 'registration_page.html', context)

