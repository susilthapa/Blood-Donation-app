
from django.urls import path, include
from .views import SignUpView, ActivateAccount
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login')

]
