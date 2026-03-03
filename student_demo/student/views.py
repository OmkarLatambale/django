from django.shortcuts import render
from .serializers import StudentSerializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializers

class StudentListCreateView(APIView):

    def post(self,request):
        serializer = StudentSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializers(students,many=True)
        return Response(serializer.data)



