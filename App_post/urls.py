from App_post import views
from django.urls import path


app_name = "App_post"

urlpatterns = [
    path('', views.Home, name='home'),
    path('like/<pk>/', views.LikeView, name='like'),
    path('unlike/<pk>/', views.UnLikeView, name='unlike'),


]
