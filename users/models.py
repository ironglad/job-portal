from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class user(AbstractUser):
    email=models.EmailField(unique=True)
    is_recuiter=models.BooleanField(default=False)
    is_applicant=models.BooleanField(default=False)
    is_resume=models.BooleanField(default=False)
    has_company=models.BooleanField(default=False)
    
    