
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home' ),
    path('edit/<str:pk>/', views.edit, name='edit'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('additem/', views.additem, name='additem'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('signup/', views.signup, name='signup'),
]