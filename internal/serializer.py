from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User

from internal.models import Gamer, Scholar
from users.serializer import Person


class PersonInternalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('tipo_user', 'wallet', 't_wallet')


class UserInternalListSerializer(serializers.ModelSerializer):
    person = PersonInternalSerializer(many=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'person')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        """
        Crea una instacia de user a partir de los datos de
        validated_data que contienen valores deserializados
        y crea una instancia de Person para el perfil UserInternal
        :param validated_data: diccionario con datos de usuario,
                person: dicionario con datos de Person
        :return: objeto User
        """
        person_data = validated_data.pop('person')
        user = User.objects.create_user(**validated_data)
        user.person = Person.objects.create(user=user, **person_data)

        user.save

        return user

    def update(self, instance, validated_data):
        """
        Actualiza una instacia de User y Person a partir de los datos
        del diccionario validated_data que contiene valores deserializados
        :param instance: objeto user a actualizar
        :param validated_data: diccionario con nuevos valores para el User
        :return: objeto User actualizado
        """
        person_data = validated_data.get('person')

        instance.person.wallet = person_data.get(
            'wallet', instance.person.wallet
        )
        instance.person.t_wallet = person_data.get(
            't_wallet', instance.person.t_wallet
        )

        instance.person.save()

        instance.username = validated_data.get(
            'username',
            instance.username
        )
        instance.password = validated_data.get(
            'password',
            instance.password
        )
        instance.email = validated_data.get(
            'email',
            instance.email
        )
        instance.save()

        return instance


class UserInternalSerializer(UserInternalListSerializer):
    class Meta(UserInternalListSerializer.Meta):
        fields = ('id', 'username', 'password', 'email', 'person')


class GamerInternalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamer
        fields = '__all__'


class ScholarInternalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholar
        fields = '__all__'
