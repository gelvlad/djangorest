from rest_framework import permissions
from .models import Tasklist


class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.username == request.user.username


class TasklistPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        list_id = view.kwargs.get('pk', None)
        if list_id:
            tasklist = Tasklist.objects.get(id=list_id)
            if tasklist.owner == request.user:
                return True
            elif tasklist in request.user.shared_tasklists.all()\
                    and request.method in permissions.SAFE_METHODS:
                return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        elif obj in request.user.shared_tasklists.all() \
                and request.method in permissions.SAFE_METHODS:
            return True
        return False


class TaskPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        list_id = view.kwargs.get('list_id', None)
        if list_id:
            tasklist = Tasklist.objects.get(id=list_id)
            if tasklist.owner == request.user\
                    or tasklist in request.user.shared_tasklists.all():
                return True
        return False

    def has_object_permission(self, request, view, obj):
        return obj.tasklist.owner == request.user\
               or obj.tasklist in request.user.shared_tasklists.all()