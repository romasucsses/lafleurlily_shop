from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ShippingAddressSerializer,  UserSerializer
from .models import User
from orders.serializers import OrdersSerializer
from orders.models import OrderInfo
from cache_control.cache_logic import *
from .tasks import update_user_task, update_address_task, create_new_user_task

class MyAccountInfoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, db):
        result = get_or_set_cache(
            queryset=User.objects.using(db).get(id=request.user.id),
            serializer=UserSerializer,
            cache_name=f"{USER_DETAIL_CACHE_NAME}_{db}_{request.user.id}",
            type_data='detail',
            cache_duration=CACHE_DURATIONS_24h
        )
        return Response(result)

    def patch(self, request, db):
        task = update_user_task.delay(request.data, request.user.id, db)
        if task:
            return Response("task is started")
        return Response("failed to start task")


class MyOrdersInfoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, db):
        orders = OrderInfo.objects.using(db).filter(user=request.user)
        result = get_or_set_cache(
            queryset=orders,
            serializer=OrdersSerializer,
            cache_name=f"{ORDERS_LIST_CACHE_NAME}_{db}_{request.user.id}",
            type_data='list',
            cache_duration=CACHE_DURATIONS_24h
        )
        return Response(result)


class MyDetailOrderInfoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, db):
        order = OrderInfo.objects.using(db).get(pk=pk, user=request.user)
        result = get_or_set_cache(
            queryset=order,
            serializer=OrdersSerializer,
            cache_name=f"{ORDER_DETAIL_CACHE_NAME}_{db}_{request.user.id}_order_{pk}",
            type_data='detail',
            cache_duration=CACHE_DURATIONS_24h
        )
        return Response(result)



class MyAddressInfoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def getUserAddress(self, request, db):
        user = User.objects.using(db).get(id=request.user.id)
        return user.user_shipping_address

    def get(self, request, db):
        result = get_or_set_cache(
            queryset=self.getUserAddress(request, db),
            serializer=ShippingAddressSerializer,
            cache_name=f"{SHIPPING_ADDRESS_DETAIL_CACHE_NAME}_{db}_{request.user.id}",
            type_data='detail',
            cache_duration=CACHE_DURATIONS_24h
        )
        return Response(result)

    def patch(self, request, db):
        task = update_address_task.delay(request.data, self.getUserAddress(request, db), db)
        if task:
            return Response("task is started")
        return Response("failed to start task")


class SingUpAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, db):
        task = create_new_user_task.delay(request.data, db)
        if task:
            return Response("task is started")
        return Response("failed to start task")
