from django.contrib import admin
from users.models import RoningGaming, RoningPay, Person, CoinBalance, NFTBalance, Txn

admin.site.register(RoningGaming)
admin.site.register(RoningPay)
admin.site.register(Person)
admin.site.register(CoinBalance)
admin.site.register(NFTBalance)
admin.site.register(Txn)
