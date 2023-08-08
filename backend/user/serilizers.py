from rest_framework import serializers

from .models import Alum, Team_Member

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team_Member
        fields = "__all__"
        
class AlumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alum
        fields = "__all__"


