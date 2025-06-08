from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('members/', views.members, name='members'),
    path('members/<int:member_id>/', views.member_detail, name='member_detail'),
    path('getparam', views.get_param, name='get_param'),
    path('kategorie/', views.category, name='category'),
]