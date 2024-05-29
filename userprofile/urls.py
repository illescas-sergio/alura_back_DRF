from django.urls import path
from users.views import ProfileView

urlpatterns = [
    # Profile views
    path('profile/', ProfileView.as_view(), name='user_profile'),
    path('profile/edit/', ProfileView.as_view(), name='edit_user_profile'),
]