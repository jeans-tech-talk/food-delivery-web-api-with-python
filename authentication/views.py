from django.contrib.auth.models import User

from authentication.serializers import UserSerializer
from common.viewsets import CreateListRetrieveViewSet


class UserViewSet(CreateListRetrieveViewSet):
    queryset = User.objects.order_by('-id')
    serializer_class = UserSerializer
