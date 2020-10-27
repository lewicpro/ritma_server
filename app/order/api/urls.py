from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('list-create-order/', views.ListCreateOrder.as_view(),
         name='list_create_order'),
]
