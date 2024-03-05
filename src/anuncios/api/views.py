from rest_framework import viewsets, filters, status
from drf_yasg.utils import swagger_auto_schema
import django_filters.rest_framework
from .models import Anuncio
from .serializers import AnunciosSerializer


class AnunciosViewSet(viewsets.ModelViewSet):
    queryset = Anuncio.objects.all()
    serializer_class = AnunciosSerializer
    filter_backends = [filters.OrderingFilter,
                       filters.SearchFilter,
                       django_filters.rest_framework.DjangoFilterBackend]
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'

    http_method_names = ['get', 'post', 'put']

    @swagger_auto_schema(responses={200: AnunciosSerializer(many=True)})
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(responses={200: AnunciosSerializer()})
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(request_body=AnunciosSerializer,
                         responses={201: AnunciosSerializer()})
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(request_body=AnunciosSerializer,
                         responses={200: AnunciosSerializer()})
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
