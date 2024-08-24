from django.contrib.sessions.models import Session
from django.db import models


# class Coupon(models.Model):
#     coupons = models.CharField(max_length=155)
#     date_expiration = models.DateField(format('%Y/%m/%d'))
#     percent_discount = models.FloatField()


class ShippingInfo(models.Model):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    street_address_1 = models.TextField()
    city = models.CharField(max_length=155)
    state = models.CharField(max_length=155)
    zip_code = models.CharField(max_length=55)
    phone = models.CharField(max_length=155)
    email = models.EmailField()


class BaseOrderInfoModel(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    date_to_deliver = models.DateTimeField(null=True)

    STATUS_LIST = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]

    status = models.CharField(max_length=255, choices=STATUS_LIST, default=STATUS_LIST[0][1])
    cart_data = models.JSONField()
    is_paid = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=255, default=None)
    total_sum = models.DecimalField(decimal_places=2, max_digits=15)

    user = models.ForeignKey('users.User', on_delete=models.PROTECT, null=True)
    shipping_data = models.ForeignKey('orders.ShippingInfo', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Order Nr.{self.pk}'

    class Meta:
        abstract = True


class OrderInfoBastina(BaseOrderInfoModel):
    pass


class OrderInfoDA(BaseOrderInfoModel):
    pass


class OrderInfoLily(BaseOrderInfoModel):
    pass


class EmailSubscription(models.Model):
    email = models.EmailField()
    date_subscription = models.DateField(auto_now=True)
    site = models.CharField(max_length=20)

