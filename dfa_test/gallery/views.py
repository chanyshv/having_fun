from rest_framework.authentication import SessionAuthentication
from rest_framework import (
    viewsets,
    views,
    permissions,
    request,
    response,
)

from gallery.models import Image
from gallery.serializer import ImageSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Image.objects.filter(owner=self.request.user)

    def perform_create(self, serializer: ImageSerializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


class RemoveAllView(views.APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request: request.Request):
        if request.user.is_staff:
            Image.objects.all().delete()
            return response.Response()
        return response.Response(status=401)
