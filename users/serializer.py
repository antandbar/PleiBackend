from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import RoningPay, Person, CoinBalance, NFTBalance, Txn
from phonenumber_field.serializerfields import PhoneNumberField


class RoningPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoningPay
        fields = '__all__'


class RoningPayListSerializer(RoningPaySerializer):
    class Meta(RoningPaySerializer.Meta):
        fields = ('id', 'roning', 'owner')


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('tipo_user', 'avatar', 'phone_number', 'wallet',
                  'date_birth', 'front_DNI', 'back_DNI')


class UserListSerializer(serializers.ModelSerializer):
    person = PersonSerializer(many=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'person')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        """
        Crea una instacia de user a partir de los datos de
        validated_data que contienen valores deserializados
        y crea una instancia de Person
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

        instance.person.tipo_user = person_data.get(
            'tipo_user', instance.person.tipo_user
        )
        instance.person.avatar = person_data.get(
            'avatar', instance.person.avatar
        )
        instance.person.phone_number = person_data.get(
            'phone_number', instance.person.phone_number
        )
        instance.person.wallet = person_data.get(
            'wallet', instance.person.wallet
        )
        instance.person.date_birth = person_data.get(
            'date_birth', instance.person.date_birth
        )
        instance.person.front_DNI = person_data.get(
            'front_DNI', instance.person.front_DNI
        )
        instance.person.back_DNI = person_data.get(
            'back_DNI', instance.person.back_DNI
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
        instance.save()

        return instance


class UserSerializer(UserListSerializer):
    class Meta(UserListSerializer.Meta):
        fields = ('id', 'username', 'password', 'person')



class MailValidateSerializer(serializers.Serializer):
    """
    Sin instacia
    :param validated_data: diccionario con codigo random
    :return: objeto MailValidate
    """
    code = serializers.IntegerField()
    email = serializers.EmailField()


class SMSValidateSerializer(serializers.Serializer):
    """
    Sin instacia
    :param validated_data: diccionario con codigo random
    :return: objeto SMSValidate
    """
    code = serializers.IntegerField()
    phone_number = PhoneNumberField()


class CoinBalanceSerializer(serializers.ModelSerializer):
    """
    Devuelve todos los datos de la entidad CoinBalance
    """

    class Meta:
        model = CoinBalance
        fields = '__all__'


class NFTBalanceSerializer(serializers.ModelSerializer):
    """
    Devuelve todos los datos de la entidad NFTBalance
    """

    class Meta:
        model = NFTBalance
        fields = '__all__'


class TxnCoinSerializer(serializers.ModelSerializer):
    """
    Devuelve todos los datos de la entidad Txn
    """

    class Meta:
        model = Txn
        fields = fields = ('parent_txn_hash', 'block', 'from_txn', 'to_txn',
                           'value', 't_txn', 'txn_fees', 'coin_balance', 'owner')


class TxnNFTSerializer(serializers.ModelSerializer):
    """
    Devuelve todos los datos de la entidad Txn
    """

    class Meta:
        model = Txn
        fields = fields = ('parent_txn_hash', 'block', 'from_txn', 'to_txn',
                           'value', 't_txn', 'txn_fees', 'nft_balance', 'owner')


"""
class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):

        Crea una instacia de user a partir de los datos de
        validated_data que contienen valores deserializados
        :param validated_data: diccionario con datos de usuario
        :return: objeto User

        instance = User()

        return self.update(instance, validated_data)

    def update(self, instance, validated_data):

        Actualiza una instacia de User a partir de los datos
        del diccionario validated_data que contiene valores deserializados
        :param instance: objeto user a actualizar
        :param validated_data: diccionario con nuevos valores para el User
        :return: objeto User actualizado

        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()

        return instance

    def validate_username(self, data):

        Valida si existe un usuario con ese username

        user = User.objects.filter(username=data)
        # Si estoy creando (no hay instancia) comprobar si hay usuarios con ese
        # username
        if not self.instance and len(user) != 0:
            raise serializers.ValidationError("Ya existe un usuario con ese username")
        # Si estoy actualizando (hay instancia) y estamos cambiando el username
        # y existen usuarios con el nuevo username
        elif self.instance and self.instance.username != data and len(user) != 0:
            raise serializers.ValidationError("Ya existe un usuario con ese username")
        else:
            return data

"""
