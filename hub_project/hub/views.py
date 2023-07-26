from django.shortcuts import render
from .models import User, Student, Accomodation
from rest_framework import generics
from .serializers import UserSerializer, StudentSerializer, AccomodationSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class AccomodationList(generics.ListCreateAPIView):
    queryset = Accomodation.objects.all()
    serializer_class = AccomodationSerializer

class AccomodationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accomodation.objects.all()
    serializer_class = AccomodationSerializer