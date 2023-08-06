from django.db import models
from djangoldp.models import Model
from django.conf import settings

class Wallet(Model):
    """ Add a field which associate this model to the user model"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wallet')

    class Meta(Model.Meta):
        anonymous_perms = ["view"]
        authenticated_perms = ["inherit"]
        owner_perms = ["inherit", "add", "change", "delete"]
        auto_author = "user"
        serializer_fields = ['@id', 'accounts']
        container_path = "/wallets/"

"""Add a model to store a blockchain public and private key and the list of networks associated with it and associate it with the walletmodel"""
class BlockchainAccount(Model):
    """Add a field which store the public key of the user"""
    public_key = models.CharField(max_length=42, blank=True, null=True)
    """Add a field which store the private key of the user"""
    private_key = models.CharField(max_length=42, blank=True, null=True)
    """Add a field which store the list of networks associated with this key"""
    network = models.CharField(max_length=42, blank=True, null=True)
    """ Add a field which associate this model to the wallet model"""
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='accounts')

    class Meta(Model.Meta):
        anonymous_perms = ["view"]
        authenticated_perms = ["inherit"]
        owner_perms = ["inherit", "add", "change", "delete"]
        container_path = "/chain_accounts/"
        serializer_fields = ['@id', 'public_key', 'network', 'wallet', 'nfts']

    def __str__(self):
        return self.public_key


""" Add a model to store the nft addresses and associate that to the current user model"""
class NFTAddress(Model):
    address = models.CharField(max_length=42, blank=True, null=True)
    account = models.ForeignKey(BlockchainAccount, on_delete=models.CASCADE, related_name='nfts')

    def __str__(self):
        return self.address