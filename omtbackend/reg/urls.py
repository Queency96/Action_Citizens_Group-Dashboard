from django.urls import path
from . import views
from .register import RegisterView
from .login import LoginView
from .dashboard import HomepageView

urlpatterns = [

    path('dashboard/', HomepageView.as_view(), name='dashboard'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

]
