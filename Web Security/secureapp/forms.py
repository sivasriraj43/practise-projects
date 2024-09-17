from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django_recaptcha.fields import ReCaptchaField

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password','password2']

    captcha = ReCaptchaField()
    