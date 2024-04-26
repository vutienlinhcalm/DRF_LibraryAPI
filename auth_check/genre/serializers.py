from rest_framework import serializers
from genre.models import genres
class genresSerializer(serializers.ModelSerializer):
    class Meta:
        model = genres
        fields = '__all__'