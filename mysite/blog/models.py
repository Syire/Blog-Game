from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS=(
    (0,"Bozza"),
    (1,"Pubblicare")
)


class Post(models.Model):
    title=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique =True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    updated_on=models.DateTimeField(auto_now=True)
    content=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(choices=STATUS,default=0)
    immagine=models.ImageField(upload_to='blog/',null=True,blank=True)
