from django.db import models


class Brand(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50, editable=True)
    rate = models.FloatField(blank=True, null=True, editable=False, default=0.0)
    site = models.CharField(blank=True, null=True, editable=True, max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_types = (
        ("vermifuga", "Vermifuga"),
        ("Adubo", "Adubo"),
        ("Veneno", "Veneno"),
        ("Fertilizante", "Fertilizante"),
        ("Agrotoxico", "Agrotoxico"),
    )
    name = models.CharField(blank=False, null=False, max_length=50, editable=True)
    brand = models.ForeignKey(Brand, blank=False,null=False,on_delete=models.CASCADE)
    picture = models.ImageField(
        upload_to="product-pic",
        height_field=None,
        width_field=None,
        max_length=None,
        null=False,
        blank=False,
    )
    product_type = models.CharField(
        choices=product_types, null=False, blank=False, max_length=50
    )

    def __str__(self):
        return self.name
