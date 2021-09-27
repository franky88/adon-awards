from rest_framework import serializers
from awards.models import Awardee, AwardTitle, CertBG


class AwardeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awardee
        fields = ['id', 'award_code', 'name', 'award_title', 'gender', 'date']
