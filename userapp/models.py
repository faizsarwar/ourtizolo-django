from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
from django.db.models.signals import post_save
from django.conf import settings
from django.core.mail import send_mail

class User(AbstractUser):
    account_type=models.CharField(max_length=150)
    date_of_birth=models.CharField(max_length=150)
    phone_number=models.CharField(max_length=150)
    adress_line1=models.CharField(max_length=150)
    adress_line2=models.CharField(max_length=150)
    advisor_crd_number=models.CharField(max_length=150 , null= True)
    advisor_role=models.CharField(max_length=150, null= True)
    email = models.EmailField('email address', unique=True)
    approved = models.BooleanField(default=False)
    report= models.FileField(upload_to='pdfs/', null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.email

class Faq(models.Model):
    Question = models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=("-date_added",)
    
    def __str__(self) -> str:
        return self.Question


class Blog(models.Model):
    tittle= models.CharField(max_length=255)
    slug= models.SlugField()
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='uploads/',blank=True,null=True)
    thumbnail=models.ImageField(upload_to='uploads/',blank=True,null=True)
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=("-date_added",)
    
    def __str__(self) -> str:
        return self.tittle
    
    def get_absolute_url(self):
        return f'/{self.slug}'
    
    def get_image(self):
        if self.image:
            return self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            return ''

    def make_thumbnail(self,image,size=(300,200)):
        img=Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)
        thumb_io=BytesIO()
        img.save(thumb_io,'JPEG',quality=85)
        thumbnail=File(thumb_io,name=image.name)
        return thumbnail



# admin username: deefyinsurancebot@gmail.com , password: perfectcup

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