from django.contrib.contenttypes.models import ContentType

from rest_framework import serializers

from drf_nest.serializer_fields import TypeField, GenericRelatedField
from cbe.customer.models import Customer, CustomerAccount, CustomerAccountContact
from cbe.party.models import Individual, Organisation, TelephoneNumber, GenericPartyRole, PartyRoleAssociation
from cbe.party.serializers import IndividualSerializer, OrganisationSerializer, TelephoneNumberSerializer, PartyRoleAssociationFromBasicSerializer, PartyRoleAssociationToBasicSerializer
from cbe.credit.serializers import CreditSerializer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    type = TypeField()
    party = GenericRelatedField( many=False, 
        serializer_dict={ 
            Individual: IndividualSerializer(),
            Organisation: OrganisationSerializer(),
        })

    managed_by = serializers.HyperlinkedRelatedField( required=False, allow_null=True, view_name='organisation-detail', lookup_field='enterprise_id', queryset=Organisation.objects.all())
    associations_from = GenericRelatedField( many=True, serializer_dict={PartyRoleAssociation: PartyRoleAssociationFromBasicSerializer(), } )
    associations_to = GenericRelatedField( many=True, serializer_dict={ PartyRoleAssociation: PartyRoleAssociationToBasicSerializer(), } )
    
    class Meta:
        model = Customer
        fields = ('type', 'url', 'customer_number', 'managed_by',
                  'customer_status', 'party', 'customer_accounts', 'physical_contacts', 'telephone_numbers', 'associations_from', 'associations_to',)

    def create(self, validated_data):
        validated_data.pop('customer_accounts', None)
        validated_data.pop('associations_from', None)
        validated_data.pop('associations_to', None)
        
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('customer_accounts', None)
        validated_data.pop('associations_from', None)
        validated_data.pop('associations_to', None)
        validated_data.pop('physical_contacts', None)
        validated_data.pop('telephone_numbers', None)
        
        for key, value in validated_data.items():
            setattr( instance, key, value )

        instance.save()
        return instance  

        
class CustomerAccountContactSerializer(serializers.HyperlinkedModelSerializer):
    type = TypeField()
    party = GenericRelatedField( many=False,
        serializer_dict={ 
            Individual: IndividualSerializer(),
            Organisation: OrganisationSerializer(),
        })

    class Meta:
        model = CustomerAccountContact
        fields = ('type', 'url', 'party', 'customer_accounts')


class CustomerAccountSerializer(serializers.HyperlinkedModelSerializer):
    type = TypeField()
    credit_liabilities = CreditSerializer(many=True,)
    managed_by = serializers.HyperlinkedRelatedField(view_name='organisation-detail', lookup_field='enterprise_id', queryset=Organisation.objects.all())

    class Meta:
        model = CustomerAccount
        fields = ('type', 'url', 'created', 'valid_from', 'valid_to', 'customer', 'account_number', 'account_status', 'managed_by', 'credit_liabilities',
                  'account_type', 'name', 'pin', 'customer_account_contact', )

    def create(self, validated_data):
        credit_liabilities_data = validated_data.pop('credit_liabilities')
        account = CustomerAccount.objects.create(**validated_data)    
        return account  


    def update(self, instance, validated_data):
        credit_liabilities_data = validated_data.pop('credit_liabilities')
        
        for key, value in validated_data.items():
            setattr( instance, key, value )

        instance.save()
        return instance             
            

sample_json = """
{
    "type": "Customer",
    "customer_number": "512332",
    "customer_status": "Active",
    "party": {
        "type": "Organisation",
        "name": "A cool store4"
    }
}
{
    "type": "Customer",
    "customer_number": "1512332212",
    "customer_status": "Active",
    "party": {
        "type": "Organisation",
        "url": "http://127.0.0.1:8000/api/sid/common_business_entities/party/organisations/2/"
    }
}

{ "type": "Customer","customer_number": "512332","customer_status": "Active","party": { "url":"http://127.0.0.1:8000/api/sid/organisations/2/" } }


"""
