from django.db import models

from cbe.business_interaction.models import BusinessInteraction, BusinessInteractionItem

def POWER_STATES = (('on', 'on'), ('off', 'off'), ('starting', 'starting'), ('stopping', 'stopping'))

class Resource(models.model):
    usage_state = models.IntegerField()
    name = models.CharField(max_length=100,null=True, blank=True )

    class Meta:
        abstract = True

        
class PhysicalResource(Resource):
    power_state = models.CharField(max_length=100, null=True, blank=True, choices=POWER_STATES)
    phicial_objects = GM2MField() #TODO: Restrict to physical_object derivatives

    place_content_type = models.ForeignKey(
        ContentType, null=True, blank=True, related_name="%(app_label)s_%(class)s_ownership")
    place_object_id = models.PositiveIntegerField(null=True, blank=True)
    place = GenericForeignKey('place_content_type', 'place_object_id')

    def __str__(self):
        return "%s at %s" % (self.name, self.place)

        
class LogicalResource(Resource):
    def __str__(self):
        return "%s" % (self.name)

    
class ResourceOrder(BusinessInteraction):
    def __str__(self):
        return "%s:%s at %s" % (self.interaction_date, self.description, self.place)

    
class ResourceOrderItem(BusinessInteractionItem):
    def __str__(self):
        return "%s:%s" % (self.business_interaction, self.action)
        