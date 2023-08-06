import factory
import hashlib
from .models import Wallet
from django.db.models.signals import post_save

@factory.django.mute_signals(post_save)
class WalletFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Wallet

    # Please refer to Factory boy documentation
    # https://factoryboy.readthedocs.io
