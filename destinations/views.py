from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Destination
from .serializiers import DestinationSerializer
from .permissions import IsOwner


class DestinationViewSet(ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    def get_queryset(self):
        user = self.request.user
        print(user.pk)
        queryset = Destination.objects.filter(user=user.pk)
        return queryset

    def get_permissions(self):
        if (
            self.action == "list"
            or self.action == "retrieve"
            or self.action == "destroy"
        ):
            # print(IsOwner.has_object_permission)
            permission_classes = [IsOwner]
        elif self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]
