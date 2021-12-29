from django.db import models
from users.models import Person


class Gamer(models.Model):
    discord_gamer = models.CharField(primary_key=True, max_length=25)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        """
        Se devuelve el nombre del model
        :return: string con nombre del model
        """
        return '{}-{}'.format(self.user_id, self.discord_gamer)

    class Meta:
        verbose_name = "Gamer"
        verbose_name_plural = "Gamers"
        db_table = "gamer"


class Scholar(models.Model):
    id_scholar = models.AutoField(primary_key=True)
    wallet_gamer = models.CharField(max_length=64, blank=True, null=True)
    t_wallet_gamer = models.CharField(max_length=15, blank=True, null=True)
    discord_manager = models.CharField(max_length=25, blank=True, null=True)
    first_name_manager = models.CharField(max_length=20, blank=True, null=True)
    last_name_manager = models.CharField(max_length=20, blank=True, null=True)
    start_date_gamer = models.DateField(blank=True, null=True)
    finish_date_gamer = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    discord_gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)

    def __str__(self):
        """
        Se devuelve el nombre del model
        :return: string con nombre del model
        """
        return '{}-{}'.format(self.discord_gamer, self.discord_manager)

    class Meta:
        verbose_name = "Scholar"
        verbose_name_plural = "Scholars"
        db_table = "scholar"


