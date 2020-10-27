from django.db import models
from app.user.models import User
from django.core.validators import RegexValidator


class Order(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    user = models.ForeignKey(
        User, related_name='user_order', on_delete=models.CASCADE)
    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    plate_number = models.CharField(max_length=100, blank=True, null=True)
    package_size = models.CharField(max_length=100, blank=True, null=True)
    current_mileage = models.CharField(max_length=100, blank=True, null=True)
    year_of_manufacture = models.PositiveBigIntegerField(blank=True, null=True)
    package_description = models.TextField(blank=True, null=True)
    company_name_sender = models.CharField(
        max_length=255, blank=True, null=True)
    sender_name = models.CharField(max_length=255)
    sender_email = models.CharField(max_length=255, blank=True, null=True)
    sender_mobile_number = models.CharField(
        validators=[phone_regex], max_length=17)
    company_name_receiver = models.CharField(
        max_length=255, blank=True, null=True)
    receiver_name = models.CharField(max_length=255)
    total_payment = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    transaction_id_total_payment = models.CharField(
        max_length=255, blank=True, null=True)
    initial_payment = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    transaction_id_initial_payment = models.CharField(
        max_length=255, blank=True, null=True)
    final_payment = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    transaction_id_final_payment = models.CharField(
        max_length=255, blank=True, null=True)
    payment_mode = models.CharField(max_length=100, blank=True, null=True)

    # def __str__(self):
    #     return '{}'.format()

    class Meta:
        ordering = ['-id']
