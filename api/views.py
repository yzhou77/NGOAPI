from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import generics
from flask import json

from User.models import Myuser
from Event.models import Event
from Event.models import Registration
from api.serializers import UserSerializer
from api.serializers import EventSerializer
from api.serializers import RegistrationSerializer
from api.serializers import EventSerializer2

class UserList(APIView):
    def get(self,request):
        """
        List all users, or create a new user.
        """
        users = Myuser.objects.all()
        serializer = UserSerializer(users, many=True)
        # pagination_class = 'rest_framework.pagination.LimitOffsetPagination'
        return Response(serializer.data)

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):

    def get(self,pk):
        try:
            user = Myuser.objects.get(pk=pk)
        except Myuser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self,):
        pass


@api_view(['GET', 'POST'])
def user_list(request):
    """
    List all user, or create a new user.
    """
    if request.method == 'GET':
        users = Myuser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """
    Get, udpate, or delete a specific user
    """
    try:
        user = Myuser.objects.get(pk=pk)
    except Myuser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EventList(generics.ListAPIView):
    queryset = Event.objects.all() ####
    serializer_class = EventSerializer  ####

    def get(self,request):
        """
        List all events, or create a new event.
        """
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        # pagination_class = 'rest_framework.pagination.LimitOffsetPagination'
        return Response(serializer.data)

    def post(self,request):
        serializer = EventSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventList2(generics.ListAPIView):
    queryset = Event.objects.all() ####
    serializer_class = EventSerializer  ####

    def get(self,request):
        """
        List all events, or create a new event.
        """
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        # pagination_class = 'rest_framework.pagination.LimitOffsetPagination'
        return Response(serializer.data)

    def post(self,request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetail(generics.ListAPIView):#### ####

    def get(self,pk):
        try:
            event = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EventSerializer(event)
        return Response(serializer.data)

    def post(self,):
        pass


@api_view(['GET', 'POST'])
def event_list(request):
    """
    List all events, or create a new event.
    """
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def event_detail(request, pk):
    """
    Get, udpate, or delete a specific event
    """
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventSerializer(event)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EventSerializer2(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegistrationList(APIView):
    def get(self,request):
        """
        List all registrations, or create a new registration.
        """
        registrations = Registration.objects.all()
        serializer = RegistrationSerializer(registrations, many=True)
        # pagination_class = 'rest_framework.pagination.LimitOffsetPagination'
        return Response(serializer.data)

    def post(self,request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistrationDetail(APIView):

    def get(self,pk):
        try:
            registration = Registration.objects.get(pk=pk)
        except Registration.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RegistrationSerializer(registration)
        return Response(serializer.data)

    def post(self,):
        pass


@api_view(['GET', 'POST'])
def registration_list(request):
    """
    List all registrations, or create a new registration.
    """
    if request.method == 'GET':
        registrations = Registration.objects.all()
        serializer = RegistrationSerializer(registrations, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def registration_detail(request, pk):
    """
    Get, udpate, or delete a specific registration
    """
    try:
        registration = Registration.objects.get(pk=pk)
    except Registration.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RegistrationSerializer(registration)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RegistrationSerializer(registration, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        registration.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

### upload image
class ImageViewSet(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
        #file = request.data['file']
            serializer = EventSerializer(data=request.data)
            file = request.POST.get('Event_image')
            #Event_image = Event.objects.create(Event_image=file)
            return Response(json.dumps({'message': "Uploaded"}), status=200)
