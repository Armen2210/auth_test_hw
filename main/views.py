from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# Create your views here.
# Здесь мы описываем функции-обработчики для разных маршрутов


def index(request):
    return render(request, 'index.html')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
    login_url = 'login'



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm(request)

    return render(request, 'login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # Создаёт форму UserCreationForm, заполняя её данными, которые пользователь отправил через POST-запрос (то есть данными из формы регистрации)
        if form.is_valid():
            form.save()                 # создаём нового пользователя
            return redirect('login')    # редирект на страницу входа
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
