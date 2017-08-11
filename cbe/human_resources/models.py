from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from cbe.party.models import PartyRole, Individual, Organisation


class IdentificationType( models.Model ):
    name = models.CharField(primary_key=True, max_length=200)
    issuer = models.ForeignKey(Organisation, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return "{}".format(self.name,)
        

class Identification( models.Model ):
    number = models.CharField(max_length=200)
    pin = models.CharField(max_length=50, null=True, blank=True)
    identification_type = models.ForeignKey( IdentificationType )

    party_content_type = models.ForeignKey(
        ContentType, related_name="%(app_label)s_%(class)s_ownership")
    party_object_id = models.PositiveIntegerField()
    party = GenericForeignKey('party_content_type', 'party_object_id')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return "{}:{}".format(self.identification_type, self.number,)    


class Staff(PartyRole):
    company = models.ForeignKey(Organisation, null=True, blank=True, related_name='employer')

    def save(self, *args, **kwargs):
        if self.name is None or self.name == "":
            self.name = "Staff"
        super(Staff, self).save(*args, **kwargs)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return "{}".format(self.name,)