from rest_framework import serializers
from .models import Opportunity,OpportunityComment


#Opportunity serializer
class OpportunitySerializer(serializers.ModelSerializer):
    created_by_name=serializers.SerializerMethodField()
    
    class Meta:
        model=Opportunity
        fields='__all__'

    def get_created_by_name(self, obj):
        return f"{obj.created_by.first_name} {obj.created_by.last_name}".strip()

#comment
class CommentSerializer(serializers.ModelSerializer):
    created_by_name = serializers.SerializerMethodField()

    class Meta:
        model=OpportunityComment
        fields='__all__'
    

    def get_created_by_name(self, obj):
        return f"{obj.created_by.first_name} {obj.created_by.last_name}".strip()