from rest_framework import serializers
from borrow.models import borrows
class borrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = borrows
        fields = '__all__'