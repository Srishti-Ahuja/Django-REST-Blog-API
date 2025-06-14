from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, instance):
        if request.method!='GET':
            return instance.author == request.user
        return True
