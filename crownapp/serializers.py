from rest_framework import serializers
from .models import School, Family

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = "__all__"
