from rest_framework import serializers
from .models import Anuncio


class AnunciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = '__all__'
