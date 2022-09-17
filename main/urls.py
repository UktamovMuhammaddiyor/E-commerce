from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('index/', index),
    path('single/', single, name='single'),
    path('men/', men, name='men'),
    path('contact/', contact, name='contact'),
    path('xato/', xato, name='xato'),
    path('checkout/', checkout, name='checkout'),
    path('add-cart/', addcart, name='add-cart'),
    path('about/', about, name='about'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('register/', register, name='register'),
    path('index_single/', index_single, name='index_single'),
    path('och/', och, name='och'),
    path('getpost/', get_post),
    path('setwebhook', setwebhook),
    path('jonat/', jonat),
    path('search/', search, name='search'),
]