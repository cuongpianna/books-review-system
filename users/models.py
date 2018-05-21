from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):

    SEX_CHOICES = (
        ('F','Nam'),
        ('M','Nữ'),
        ('O','Khác'),
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True,null=True)
    sex = models.CharField(max_length=1,choices=SEX_CHOICES)
    photo = models.ImageField(upload_to="image/user/%Y/%m/%d",blank=True)

    def __str__(self):
        return "Profile này của user {}".format(self.user.username)



