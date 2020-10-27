from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from app.order.models import Order
from app.order.api.serializers import OrdersSerializer


class ListCreateOrder(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrdersSerializer
