from rest_framework import serializers

from sdfood.models import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Food
        fields=('name','description')