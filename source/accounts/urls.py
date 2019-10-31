from django.urls import path

from accounts.views import login_view, logout_view, register_view, UserDetailView, UserChangeView, \
    UserChangePasswordView, UserListView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register', register_view, name='register'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='user_profile'),
    path('profile/edit/<int:pk>/', UserChangeView.as_view(), name='user_edit'),
    path('profile/edit/pass/<int:pk>', UserChangePasswordView.as_view(), name='user_edit_pass'),
    path('users/', UserListView.as_view(), name='users_list')
]

app_name = 'accounts'
