# from django.views.generic import View
from django.core.mail import send_mail
from django.http import HttpResponse
import random
from sendsms import api
from backendPlei.settings import PHONE_HOST_USER, DEFAULT_FROM_EMAIL
from users.settings import HEAD_EMAIL, MESSAGE_EMAIL, MESSAGE_PHONE
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import views
from users.models import RoningPay, CoinBalance, NFTBalance, Txn
from users.serializer import RoningPaySerializer, RoningPayListSerializer, UserListSerializer, MailValidateSerializer, \
    UserSerializer, SMSValidateSerializer, CoinBalanceSerializer, NFTBalanceSerializer, TxnCoinSerializer, \
    TxnNFTSerializer
# from django.shortcuts import get_object_or_404
from rest_framework import status
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        """
        En función si se quiere trabajar con el detalle o la vista genérica
        se devuelven dos tipo de objetos, para mostrar unos u otros campos
        :return: Serializer
        """
        if self.action == 'list':
            return UserListSerializer
        else:
            return UserSerializer


class RoninPayViewSet(ModelViewSet):
    queryset = RoningPay.objects.all()

    def get_serializer_class(self):
        """
        En función si se quiere trabajar con el detalle o la vista genérica
        se devuelven dos tipo de objetos, para mostrar unos u otros campos
        :return: Serializer
        """
        if self.action == 'list':
            return RoningPayListSerializer
        else:
            return RoningPaySerializer


class MailValidateAPI(views.APIView):

    def get(self, request):
        serializer = MailValidateSerializer()
        return Response(serializer.data)

    def post(self, request):
        # Se crea número random
        random_num = random.randint(111112, 999999)

        # Se captura email y se setean en la request tanto code como email
        email = request.data["email"]
        request.data.update({"code": random_num, "email": email})

        serializer = MailValidateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Los propiedas para enviar el correo están el setting global
        try:
            send_mail(HEAD_EMAIL + email, MESSAGE_EMAIL + str(random_num),
                      DEFAULT_FROM_EMAIL, [email], fail_silently=False)
        except Exception as e:
            return HttpResponse('Error %s' % e)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SMSValidateAPI(views.APIView):

    def get(self, request):
        serializer = SMSValidateSerializer()
        return Response(serializer.data)

    def post(self, request):
        # Se crea número random
        random_num = random.randint(111112, 999999)

        # Se captura phone_number  y se setean en la request tanto code como phone_number
        phoneNumber = request.data["phone_number"]
        request.data.update({"code": random_num, "phone_number": phoneNumber})

        serializer = SMSValidateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            api.send_sms(body=MESSAGE_PHONE + str(random_num), from_phone=PHONE_HOST_USER,
                         to=[phoneNumber], fail_silently=False)
        except Exception as e:
            return HttpResponse('Error %s' % e)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CoinBalanceViewSet(ModelViewSet):
    queryset = CoinBalance.objects.all()
    serializer_class = CoinBalanceSerializer


class NFTBalanceViewSet(ModelViewSet):
    queryset = NFTBalance.objects.all()
    serializer_class = NFTBalanceSerializer


class TxnCoinViewSet(ModelViewSet):
    queryset = Txn.objects.all()
    serializer_class = TxnCoinSerializer


class TxnNFTViewSet(ModelViewSet):
    queryset = Txn.objects.all()
    serializer_class = TxnNFTSerializer

"""
class UserListAPI(APIView):

    def get(self, request):
        # instancion paginador
        paginator = PageNumberPagination()
        users = User.objects.all()
        # paginar el queryset
        paginator.paginate_queryset(users, request)
        serializer = UserSerializer(users, many=True)
        # devolver respuesta paginada
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPI(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RoningPayAPI(ListCreateAPIView):
    queryset = RoningPay.objects.all()
    # serializer_class = RoningPayListSerializer

    def get_serializer_class(self):
        return RoningPaySerializer if self.request.method == "POST" else RoningPayListSerializer


class RoningPayDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = RoningPay.objects.all()
    serializer_class = RoningPaySerializer

"""

"""
class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request):
        #users = User.objects.all()
        #serializer = UserSerializer(users, many=True)
        #return Response(serializer.data)
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""
