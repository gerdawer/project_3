from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


# Создадим собственный класс для фформы регистрации
# Сделаем его наследником предустановленного класса UserCreationForm
class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # Указываем модель, с которой связанна создаваемая форма
        model = User
        # Укажем, какие поля должны быть видны в форме и в каком поряде
        fields = ('first_name', 'last_name', 'username', 'email')