from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('visitors/', views.visitor_list, name='visitor_list'),
    path('visitors/register/', views.register_visitor, name='register_visitor'),
    path('visitors/update/<int:pk>/', views.update_visitor, name='update_visitor'),
    path('visitors/delete/<int:pk>/', views.delete_visitor, name='delete_visitor'),
]
