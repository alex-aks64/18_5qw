from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from .forms import UserRegister

# Pseudo-list of existing users
users = ['user1', 'user2', 'user3']

def sign_up_by(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age', 0))

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            return render(request, 'fifth_task/registration_page.html', {'message': f'Приветствуем, {username}!'})

    return render(request, 'fifth_task/registration_page.html', info)

def sign_up(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                return render(request, 'fifth_task/registration_page.html', {'message': f'Приветствуем, {username}!'})
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)
    

# Create your views here.
