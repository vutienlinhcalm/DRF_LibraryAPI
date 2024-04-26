from rest_framework import serializers
from book.models import books
class booksSerializer(serializers.ModelSerializer):
    class Meta:
        model = books
        fields = '__all__'