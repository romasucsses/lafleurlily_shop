from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ShippingAddressSerializer,  UserSerializer
from .models import User
from cache_control.cache_logic import *
from .tasks import update_user_task, update_address_task, create_new_user_task
from utils.get_table import get_model_by, get_serializer


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
        model = get_model_by(db, 'OrderInfo', 'orders')
        orders = model.objects.filter(user=request.user)
        serializer = get_serializer(db, 'OrderInfo')
        result = get_or_set_cache(
            queryset=orders,
            serializer=serializer,
            cache_name=f"{ORDERS_LIST_CACHE_NAME}_{db}_{request.user.id}",
            type_data='list',
            cache_duration=CACHE_DURATIONS_24h
        )
        return Response(result)


class MyDetailOrderInfoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, db):
        model = get_model_by(db, 'OrderInfo', 'orders')
        order = model.objects.get(pk=pk, user=request.user)
        serializer = get_serializer(db, 'OrderInfo')
        result = get_or_set_cache(
            queryset=order,
            serializer=serializer,
            cache_name=f"{ORDER_DETAIL_CACHE_NAME}_{db}_{request.user.id}_order_{pk}",
            type_data='detail',
            cache_duration=CACHE_DURATIONS_24h
        )
        return Response(result)



class MyAddressInfoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def getUserAddress(self, request, db):
        user = User.objects.get(id=request.user.id)
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
