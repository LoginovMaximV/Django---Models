from django.urls import path
from .views import SignUp
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]