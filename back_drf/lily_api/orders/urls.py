from django.urls import path
from .views import CreateOrderAPI, ContactUsViewAPI
from utils.subsciber_post import SubscriberPost


urlpatterns = [
    path('create-new-order/', CreateOrderAPI.as_view(), name='create_new_order'),
    path('contact-us/', ContactUsViewAPI.as_view(), name='contact_us'),
    path('email-subscrube/', SubscriberPost.as_view(), name='email_subscribe')
]
