from django.db import models
from django.db.models.fields import CharField
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,verbose_name="Kateqoriya")
    def __str__(self):
        return self.name
    class Meta:
            ordering = ['-id']

class Article(models.Model):
    category = models.ManyToManyField(Category,verbose_name="Kateqoriya",blank = True)
    name = models.CharField(max_length=50,verbose_name="Ad")
    content = RichTextField(verbose_name="Haqqında")
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(blank=True,null=True,verbose_name="Şəkil")

    def __str__(self):
        return self.name
    
    class Meta:
            ordering = ['id']
    
class About(models.Model):
    name = "About"
    content = RichTextField(verbose_name="Haqqında")
    image = models.FileField(blank=True,null=True,verbose_name="Şəkil")
    
    def __str__(self):
        return self.name

class Sosial(models.Model):
    name = models.CharField(max_length=50,verbose_name="Ad")
    klass = models.CharField(max_length=50,verbose_name="klass")

    def __str__(self):
        return self.name

    class Meta:
            ordering = ['-id']