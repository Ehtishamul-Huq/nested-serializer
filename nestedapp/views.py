import re
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import QuestionSerializer
from rest_framework import status
# Create your views here.

class QuestionView(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.save()
            serializer = QuestionSerializer(question)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)