from unittest import result
from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
# Create your models here

# change the image urls

class Faq(models.Model):
    Question = models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=("-date_added",)
    
    def __str__(self) -> str:
        return self.Question

class Research(models.Model):
    crop = models.CharField(max_length=100)
    ProductUsed = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    image=models.ImageField(upload_to='uploads/',blank=True,null=True)
    thumbnail=models.ImageField(upload_to='uploads/',blank=True,null=True)
    protocol=models.TextField(blank=True,null=True)
    
    def __str__(self) -> str:
        return self.crop
    
    
    def get_image(self):
        if self.image:
            return  self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return  self.thumbnail.url
        else:
            return ''
            # if self.image:
            #     self.thumbnail=self.make_thumbnail(self.image)
            #     self.save()
            #     return  self.thumbnail.url

            # else:
            #     return ''


    def make_thumbnail(self,image,size=(300,200)):
        img=Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)
        thumb_io=BytesIO()
        img.save(thumb_io,'JPEG',quality=85)
        thumbnail=File(thumb_io,name=image.name)
        return thumbnail

class Testemonial(models.Model):
    tittle = models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=("-date_added",)
    
    def __str__(self) -> str:
        return self.tittle

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
            # if self.image:
            #     self.thumbnail=self.make_thumbnail(self.image)
            #     self.save()
            #     return  self.thumbnail.url

            # else:
            #     return ''

    def make_thumbnail(self,image,size=(300,200)):
        img=Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)
        thumb_io=BytesIO()
        img.save(thumb_io,'JPEG',quality=85)
        thumbnail=File(thumb_io,name=image.name)
        return thumbnail

class Press(models.Model):
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
            return  self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            return ''
            # if self.image:
            #     self.thumbnail=self.make_thumbnail(self.image)
            #     self.save()
            #     return self.thumbnail.url
            # else:
            #     return ''

    def make_thumbnail(self,image,size=(300,200)):
        img=Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)
        thumb_io=BytesIO()
        img.save(thumb_io,'JPEG',quality=85)
        thumbnail=File(thumb_io,name=image.name)
        return thumbnail











