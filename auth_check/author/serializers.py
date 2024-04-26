from rest_framework import serializers
from author.models import authors
class authorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = authors
        fields = '__all__'
