# Generated by Django 4.2.7 on 2023-11-06 01:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_alter_product_product_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('rate', models.PositiveSmallIntegerField(editable=False)),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('downgrade', models.ManyToManyField(related_name='downgrade', to=settings.AUTH_USER_MODEL)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='about', to='product.product')),
                ('upgrade', models.ManyToManyField(related_name='upgrade', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]