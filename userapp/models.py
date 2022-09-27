from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
from django.db.models.signals import post_save
from django.conf import settings
from django.core.mail import send_mail

class User(AbstractUser):
    account_type=models.CharField(max_length=150)
    date_of_birth=models.CharField(max_length=150)
    First_name=models.CharField(max_length=150)
    Last_name=models.CharField(max_length=150)
    phone_number=models.CharField(max_length=150)
    adress_line1=models.CharField(max_length=150)
    adress_line2=models.CharField(max_length=150)
    email = models.EmailField('email address', unique=True)
    approved = models.BooleanField(default=False)
    report= models.FileField(upload_to='pdfs/', null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.email

# hardcode this in settings 
# gmail account
# gold.anasazi@gmail.com

# password
# anasazi123


# admin username: anass@gmail.com, password: perfectcup

def post_save_user(*args,**kwargs):
    user=kwargs['instance']
    if user.account_type!="Consumer":
        if user.approved:
            print("email sent")
            try:
                send_mail(
                    'Account Verified',
                    "your'e Account is now been verified by our team ",
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False,
                )
            except:
                print("Account not Found")

post_save.connect(post_save_user,sender=User)