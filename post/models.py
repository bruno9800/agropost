from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class Post(models.Model):
    title = models.CharField(blank=False,null=False,max_length=30,editable=True)
    content = models.TextField(blank=False,null=False,editable=True)
    rate = models.PositiveSmallIntegerField(blank=False,null=False,editable=False, default=0)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product,blank=False,null=False,on_delete=models.CASCADE)
    author = models.ForeignKey(User,blank=False,null=False,on_delete=models.CASCADE)
    upgrade = models.ManyToManyField(User,related_name="upgrade",null=True,blank=True)
    downgrade = models.ManyToManyField(User,related_name="downgrade",null=True,blank=True)


    def __str__(self):
        return self.title


