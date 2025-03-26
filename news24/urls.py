from django.urls import path
from .views import index, detail, contact, about, category_detail

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('contact/', contact, name='contact'),
    path('category/<int:pk>/', category_detail, name='ctg'),
]