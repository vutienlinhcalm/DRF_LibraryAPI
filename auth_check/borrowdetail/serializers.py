from rest_framework import serializers
from borrowdetail.models import borrowdetails
class borrowdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = borrowdetails
        fields = '__all__'