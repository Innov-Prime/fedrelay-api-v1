from django.db import models

# Create your models here.
class UserFedrelay(models.Model):
    phone = models.CharField(max_length=200,null=True,unique=True)
    email = models.EmailField(max_length=300,null=True,unique=True)
    password = models.CharField(max_length=300)
    is_active = models.BooleanField(default=False)
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.password