from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('bio/', views.bio_view, name='bio'),
    path('bio-update/', views.bio_update, name='bio-update'),
]
