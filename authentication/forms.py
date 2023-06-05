from django.contrib.auth.forms import UserCreationForm
from authentication.models import User


class UserCreatedForm(UserCreationForm):
    """Форма Пользователя для джанго модели"""
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
