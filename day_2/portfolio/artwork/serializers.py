from dataclasses import field
from rest_framework import serializers
from .models import Artwork, Author, Multimedia, Portfolio, Exposition

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class MultimediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multimedia
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class ExpositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exposition
        fields = '__all__'
