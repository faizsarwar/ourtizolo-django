from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
# Create your models here.

# Create your models here.
class info(models.Model):
    email= models.EmailField()
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    phone_number= models.CharField(max_length=255)
    account_type= models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, blank=True)

class Category(models.Model):
    name_without_space= models.CharField(max_length=255)
    title= models.CharField(max_length=255)
    slug= models.SlugField()

    class Meta:
        ordering=('title',)
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return f'/{self.slug}'


class Product(models.Model):
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    priceRange= models.CharField(max_length=255)
    slug= models.SlugField()
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='uploads/',blank=True,null=True)
    thumbnail=models.ImageField(upload_to='uploads/',blank=True,null=True)
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=("-date_added",)
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}'
    
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

class ProductVariation(models.Model):
    Product=models.ForeignKey(Product,related_name='variation',on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=9,decimal_places=2)
    size= models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=("-date_added",)
    
    def __str__(self) -> str:
        return self.size 
    

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

