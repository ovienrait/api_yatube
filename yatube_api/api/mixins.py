from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied


class AuthorPermissionsMixin(viewsets.ModelViewSet):
    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Нельзя изменить чужую запись!')
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Нельзя удалить чужую запись!')
        instance.delete()
