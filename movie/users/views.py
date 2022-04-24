from django.shortcuts import render
from django.views.generic import CreateView

# Функция reverse_lazy позволяет получить URL по параметру "name" функции path()
from django.urls import reverse_lazy

#  импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm  # Указываем класс из которого нужно взять форму
    # Куда перенаправить пользователя после успешной отправки
    success_url = reverse_lazy("login")  # login - это параметр "name" в path()
    # Имя шаблона куда будет передана переменная form с объектом HTML-формы.
    template_name = "signup.html"