from rest_framework import serializers
from firstapp.models import Uniinf, Program_Highlights


class uniinfserializer(serializers.ModelSerializer):
    class Meta:
        model = Uniinf
        fields = '__all__'

class Program_Highlightsserializer(serializers.ModelSerializer):
    class Meta:
        model = Program_Highlights
        fields = '__all__'