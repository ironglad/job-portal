from django.db import models
from users.models import user
# Create your models here.

class resume(models.Model):
    user=models.OneToOneField(user,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100,null=True, blank=True)
    surname= models.CharField(max_length=100,null=True, blank=True)
    location=models.CharField(max_length=100,null=True, blank=True)
    job_title=models.CharField(max_length=100,null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.first_name1}{self.surname}'