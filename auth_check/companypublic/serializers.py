from rest_framework import serializers
from companypublic.models import companypublics
class companypublicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = companypublics
        fields = '__all__'