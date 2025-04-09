from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

ACCOUNT_TYPE_CHOICES = [
        ('ward', 'Ward'),
        ('local', 'Local'),
        ('state', 'State'),
        ('national', 'National'),
    ] 

class User(AbstractUser):
    # id = ShortUUIDField(primary_key=True, unique=True, editable=False, alphabet='bcarem12345qop09867890')
    fullname = models.CharField(max_length=200, default=False)
    username  =models.CharField( max_length=200, unique=True)
    phone  =models.CharField( max_length=200, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    state = models.CharField(max_length=254, default=False)
    ward = models.EmailField(max_length=254, default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    email_verified = models.BooleanField(default=False)
    phone_verified =  models.BooleanField(default=False)
    account_type = models.CharField(
        max_length=10, 
        choices=ACCOUNT_TYPE_CHOICES, 
        default='ward')

    # requires_google_auth = models.BooleanField(default=False) 

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.username

class WardAccount(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='wardaccount')
    date_of_birth = models.DateField()
    image = models.ImageField( upload_to='profile')

    def __str__(self):
        return self.user.fullname
    

class LocalAccount(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='localaccount')
    date_of_birth = models.DateField()
    registration_number = models.CharField(max_length=200)
    address = models.TextField()


    def __str__(self):
        return self.user.fullname
    

class StateAccount(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='stateaccount')
    date_of_birth = models.DateField()
    registration_number = models.CharField(max_length=200)
    address = models.TextField()


    def __str__(self):
        return self.user.fullname


class NationalAccount(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='nationalaccount')
    date_of_birth = models.DateField()
    registration_number = models.CharField(max_length=200)
    address = models.TextField()


    def __str__(self):
        return self.user.fullname

