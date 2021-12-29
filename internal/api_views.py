from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from internal.serializer import UserInternalListSerializer, UserInternalSerializer, \
    GamerInternalSerializer, ScholarInternalSerializer
from internal.models import Gamer, Scholar


class UserInternalViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        """
        En función si se quiere trabajar con el detalle o la vista genérica
        se devuelven dos tipo de objetos, para mostrar unos u otros campos
        :return: Serializer
        """
        if self.action == 'list':
            return UserInternalListSerializer
        else:
            return UserInternalSerializer


class GamerInternalViewSet(ModelViewSet):
    queryset = Gamer.objects.all()
    serializer_class = GamerInternalSerializer


class ScholarInternalViewSet(ModelViewSet):
    queryset = Scholar.objects.all()
    serializer_class = ScholarInternalSerializer
