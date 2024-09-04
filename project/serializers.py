from rest_framework import serializers
from .models import Project,DecisionLog,Risk,Costs,ProjectFeedback
from users.serializers import CustomUserSerializer




#Project serializer
class ProjectSerializer(serializers.ModelSerializer):
    team_member = CustomUserSerializer(many=True, read_only=True)

    class Meta:
        model=Project
        fields='__all__'


#Decision Log serializer
class DecisionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model=DecisionLog
        fields='__all__'


#Risk Log serializer
class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Risk
        fields='__all__'


#Cost serializer
class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Costs
        fields='__all__'


#Feedback serializer
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectFeedback
        fields='__all__'