from celery import shared_task
from .models import User
from .serializers import UserSerializer, UserSignUpSerializer, ShippingAddressSerializer



@shared_task
def update_user_task(request_data, user_id, db):
    user = User.objects.get(pk=user_id)
    serializer = UserSerializer(user, data=request_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return 'updated successfully'
    return 'fail to update'


@shared_task
def update_address_task(request_data, address, db):
    new_data = ShippingAddressSerializer(address, data=request_data, partial=True)
    if new_data.is_valid():
        new_data.save()
        user = address
        user = new_data.instance
        user.save()
        return 'Done Successful'
    return 'Not Successful'


@shared_task
def create_new_user_task(request_data, db):
    new_user = UserSignUpSerializer(data=request_data)
    if new_user.is_valid():
        new_user.save()
        return 'User have been created'
    return 'User Not Created'
