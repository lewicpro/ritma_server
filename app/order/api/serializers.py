from rest_framework import serializers
from app.order.models import Order


class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['user', 'from_location', 'to_location', 'pickup_location', 'dropoff_location', 'plate_number', 'package_size', 'current_mileage', 'year_of_manufacture', 'package_description', 'company_name_sender', 'sender_name',
                  'sender_email', 'sender_mobile_number', 'company_name_receiver', 'receiver_name', 'total_payment', 'transaction_id_total_payment', 'initial_payment', 'transaction_id_initial_payment', 'final_payment', 'transaction_id_final_payment']
