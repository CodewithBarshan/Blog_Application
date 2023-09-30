from django.db import models
from django.utils.html import format_html 
from tinymce.models import HTMLField
# Create your models here.

class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    url=models.CharField(max_length=100)
    image=models.ImageField(upload_to='category/')
    datetime=models.DateTimeField(auto_now_add=True,null=True)

    def image_tag(self): #to show images in admin panel in object showing page
        return format_html('<img src="/media/{}" style="width:40px;height:40px;border-radius:50%"/> '.format(self.image))
    
    def __str__(self): # to print title instead of object name
        return self.title

class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=1000)
    content = HTMLField()
    url=models.CharField(max_length=100)
    cat=models.ForeignKey(Category,on_delete=models.CASCADE) # on deleting cat ,the post will be deleted too
    image=models.ImageField(upload_to='post/')    

    

    def __str__(self): # to print title instead of object name
        return self.title