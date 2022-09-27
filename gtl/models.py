from django.db import models

# Create your models here.
class GtlForm(models.Model):
    FirstName = models.CharField(max_length=255)
    LastName= models.CharField(max_length=255)
    email = models.EmailField('email address', unique=True, null=True, default=True)
    CompanyName=models.TextField(blank=True,null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=("-date_added",)
    
    def __str__(self) -> str:
        return self.FirstName