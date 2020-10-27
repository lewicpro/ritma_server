from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    # path('register/', views.RegisterView.as_view(), name='register_user'),
    path('login/', obtain_auth_token, name='login'),

]
