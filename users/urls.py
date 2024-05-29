from django.urls import path
from .views import LoginView, LogoutView, RegisterApiView

urlpatterns = [
    # Auth views
    path('login/', LoginView.as_view(), name='auth_login'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('register/', RegisterApiView.as_view(), name='auth_register'),
]