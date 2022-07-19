from django.urls import path
from django.db import router

from rest_framework.routers import DefaultRouter

from .controller import ArtworkSet, AuthorSet, MultimediaSet, PortfolioSet, ExpositionSet

router = DefaultRouter()
router.register(r'works', ArtworkSet)
router.register(r'authors', AuthorSet)
router.register(r'multimedia', MultimediaSet)
router.register(r'portfolios', PortfolioSet)
router.register(r'expositions', ExpositionSet)
urlpatterns = router.urls
