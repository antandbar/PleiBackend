from django.db import models
from django.contrib.auth.models import User
from users.settings import T_USER
from phonenumber_field.modelfields import PhoneNumberField


class RoningGaming(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    roning = models.CharField(blank=True, null=True, default="", max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Se devuelve el nombre del model
        :return: string con nombre del model
        """
        return '{}-{}'.format(self.owner, self.roning)


class RoningPay(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    roning = models.CharField(blank=True, null=True, default="", max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Se devuelve el nombre del model
        :return: string con nombre del model
        """
        return '{}-{}'.format(self.owner, self.roning)


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to='images/avatars/')
    phone_number = PhoneNumberField(unique=True, null=True, blank=False)
    wallet = models.CharField(max_length=64, blank=True, null=True)
    t_wallet = models.CharField(max_length=15, blank=True, null=True)
    date_birth = models.DateField(blank=True, null=True)
    front_DNI = models.ImageField(blank=True, null=True, upload_to='images/front_dni/')
    back_DNI = models.ImageField(blank=True, null=True, upload_to='images/back_dni/')
    # el campo T_USER esta seteado en los setting de la app users y de la app badkendplei
    tipo_user = models.CharField(max_length=3, choices=T_USER, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Se devuelve el nombre del model
        :return: string con nombre del model
        """
        return '{}-{}'.format(self.user, self.tipo_user)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"
        db_table = "person"


class CoinBalance(models.Model):
    balance = models.FloatField(blank=True, null=True)
    t_coin = models.CharField(blank=True, null=True, max_length=4)
    value = models.FloatField(blank=True, null=True)
    token = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        Se devuelve el nombre del model
        :return: string con nombre del model
        """
        return '{}-{}'.format(self.owner, self.token)

    class Meta:
        verbose_name = "CoinBalance"
        verbose_name_plural = "CoinBalances"
        db_table = "coinbalance"


class NFTBalance(models.Model):
    t_nft = models.CharField(blank=True, null=True, max_length=4)
    token = models.FloatField(blank=True, null=True, default=0)
    analyze_assets = models.CharField(blank=True, null=True, max_length=10)
    identify_assets = models.CharField(blank=True, null=True, max_length=20)
    land_item_axie = models.CharField(blank=True, null=True, max_length=15)
    acarcity_class = models.CharField(blank=True, null=True, max_length=15)
    market_price = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        Se devuelve el nombre del model
        :return: string con nombre del model
        """
        return '{}-{}'.format(self.owner, self.token)

    class Meta:
        verbose_name = "NFTBalance"
        verbose_name_plural = "NFTBalances"
        db_table = "nftbalance"


class Txn(models.Model):
    parent_txn_hash = models.CharField(primary_key=True, max_length=40)
    block = models.IntegerField(blank=True, null=True)
    from_txn = models.CharField(blank=True, null=True, max_length=40)
    to_txn = models.CharField(blank=True, null=True, max_length=40)
    value = models.FloatField(blank=True, null=True)
    t_txn = models.CharField(blank=True, null=True, max_length=4)
    txn_fees = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    coin_balance = models.ForeignKey(CoinBalance, null=True, blank=True, on_delete=models.CASCADE)
    nft_balance = models.ForeignKey(NFTBalance, null=True, blank=True, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        Se devuelve el nombre del model
        :return: string con nombre del model
        """
        return '{}-{}'.format(self.owner, self.value)

    class Meta:
        verbose_name = "Txn"
        verbose_name_plural = "Txns"
        db_table = "txns"



