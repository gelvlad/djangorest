from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import TaskSerializer, TasklistSerializer,\
    UserSerializer
from .models import Task, Tasklist
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import TasklistPermission, TaskPermission, IsUser


class TasklistCreateView(generics.ListCreateAPIView):
    serializer_class = TasklistSerializer

    def get_queryset(self):
        user = self.request.user
        return user.tasklists.all().union(user.shared_tasklists.all())

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TasklistDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, TasklistPermission)
    serializer_class = TasklistSerializer
    queryset = Tasklist.objects.all()


class TaskCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, TaskPermission)
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        list_id = self.kwargs.get('list_id', None)
        if list_id:
            queryset = queryset.filter(tasklist_id=list_id)
        return queryset

    def perform_create(self, serializer):
        list_id = self.kwargs.get('list_id', None)
        try:
            tasklist = Tasklist.objects.get(pk=list_id)
        except Tasklist.DoesNotExist:
            raise Tasklist.DoesNotExist()
        serializer.save(tasklist=tasklist)


class TaskDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (TaskPermission,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = None
        list_id = self.kwargs.get('list_id', None)
        if list_id is not None:
            queryset = Task.objects.filter(tasklist_id = list_id)
        return queryset


class UserCreateView(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.filter(username=self.request.user)
        return queryset


class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
