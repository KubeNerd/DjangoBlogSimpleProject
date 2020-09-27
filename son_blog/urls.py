from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.teste),
    path('posts/<int:post_id>', views.post, name='posts'),

] 
