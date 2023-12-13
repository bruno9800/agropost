from django.urls import path
from .views import profile_view

app_name = "product"

urlpatterns = [
    path("profile/<int:pk>/", profile_view, name="product_profile"),  
    
]
