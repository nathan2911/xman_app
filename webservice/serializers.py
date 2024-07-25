from rest_framework import serializers
from projects.models import *
from ba.models import *


class NationalFoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NationalFoods
        fields = (
            'customer_phone',
            'customer_name',
            'question1_answer',
            'question1_no_reason',
            'question1_yes_reason',
            'question2_answer',
            'question2_no_reason',
            'question3_answer',
            'question3_no_reason',
            'question4_answer',
            'question5_answer',
            'question6_answer',
            'captured_by'
        )


class BaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandAmbassador
        fields = (
            'full_name',
            'ba_code',
        )



