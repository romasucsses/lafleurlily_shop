from rest_framework.response import Response
from rest_framework import serializers
from orders.models import EmailSubscription
from rest_framework.views import APIView


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSubscription
        fields = ["email"]


class SubscriberPost(APIView):
    def post(self, request, db):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(using=db)
            return Response("have got the email ")
        return Response('not valid email data')
