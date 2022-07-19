from rest_framework import viewsets
from .models import Artwork, Author, Multimedia, Portfolio, Exposition
from .serializers import ArtworkSerializer, AuthorSerializer, MultimediaSerializer, PortfolioSerializer, ExpositionSerializer

class ArtworkSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer


class AuthorSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class MultimediaSet(viewsets.ModelViewSet):
    queryset = Multimedia.objects.all()
    serializer_class = MultimediaSerializer

class PortfolioSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class ExpositionSet(viewsets.ModelViewSet):
    queryset = Exposition.objects.all()
    serializer_class = ExpositionSerializer