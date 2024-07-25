from rest_framework import serializers
from ba import models


class BaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'full_name',
            'ba_code'
        )
        model = models.BrandAmbassador