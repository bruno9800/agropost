from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class Post(models.Model):
    title = models.CharField(blank=False,null=False,max_length=30,editable=True)
    content = models.TextField(blank=False,null=False,editable=True)
    rate = models.PositiveSmallIntegerField(blank=False,null=False,editable=False, default=0)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE,related_name="about",blank=False,null=False)
    author = models.OneToOneField(User,related_name="author",on_delete=models.CASCADE,blank=False,null=False)
    upgrade = models.ManyToManyField(User,related_name="upgrade")
    downgrade = models.ManyToManyField(User,related_name="downgrade")

    def __str__(self):
        return self.title


