from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class RegistrationUserForm(UserCreationForm):
    class meta:
        model=get_user_model()
        fields=['username','password1','password2']
        
