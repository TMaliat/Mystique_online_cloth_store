from django.db import models

# Create your models here.
class Category(models.Model):
  title=models.CharField(max_length=150, unique=True)
  slug=models.SlugField(max_length=150,unique=True)
  featured=models.BooleanField(default=False)
  created_date=models.DateTimeField(auto_now_add=True)
  
  class Meta:
      ordering=['title']
      
  def __str__(self)-> None:
      return self.title   
    

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    desc=models.TextField(max_length=500)
    phonenumber=models.IntegerField()

    def __str__(self):
        return self.name    

class Product(models.Model):
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    title=models.CharField(max_length=250, unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    featured=models.BooleanField(default=False)
    price=models.DecimalField(max_digits=8, decimal_places=2)
    thumbnail = models.ImageField(upload_to='product_thumbnails')
    in_stock=models.BooleanField(default=True)
    stitched=models.BooleanField(default=True)
    description=models.TextField(null=True, blank=True, default='N/A')
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    
    class Meta:
      ordering=['-id']
      
    def __str__(self)-> None:
      return self.title
    
    @property 
    def related(self):
      return self.category.products.all().exclude(pk=self.pk)
  
class Slider(models.Model):
      title=models.CharField(max_length=50)
      banner=models.ImageField(upload_to='banners')
      show=models.BooleanField(default=True)
      created_date=models.DateTimeField(auto_now_add=True)
      
      def __str__(self)-> None:
        return self.title 
      