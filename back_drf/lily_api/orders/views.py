import os
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import create_new_order_task, send_emails_task
from cache_control.cache_logic import *
from dotenv import load_dotenv

load_dotenv()


class CreateOrderAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request, db):
        task = create_new_order_task.delay(request.data, request.user.id, db)
        if task:
            return Response("task is started")
        return Response("failed to start task")



class ContactUsViewAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request, db):
        task = send_emails_task.delay(
            emails_list=os.getenv('email_from'), 
            title='New Request to Contact', 
            msg=request.data.msg
        )
        if task:
            return Response("task is started")
        return Response("failed to start task")




