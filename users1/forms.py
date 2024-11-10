from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from messages1.forms import StyleFormMixin
from users1.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """
    Форма для регистрации пользователя
    """
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class UserUpdateForm(StyleFormMixin, ModelForm):
    """
    Форма для редактирования профиля пользователя
    """
    class Meta:
        model = User
        fields = ("avatar", "first_name", "last_name")


class UserModeratorForm(StyleFormMixin, ModelForm):
    """
    Форма для редактирования профиля пользователя в режиме модератора
    """
    class Meta:
        model = User
        fields = ("is_active",)