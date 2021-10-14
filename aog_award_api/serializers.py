from awards.models import Awardee, AwardTitle
from rest_framework import serializers


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awardee
        fields = [
            'id',
            # 'user',
            # 'award_code',
            'award_title',
            'name',
            'citation',
            'date',
            'background',
        ]


class AwardTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardTitle
        fields = [
            'id',
            'title',
        ]
