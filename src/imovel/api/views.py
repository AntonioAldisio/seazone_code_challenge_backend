from rest_framework import viewsets, filters, status
from drf_yasg.utils import swagger_auto_schema
import django_filters.rest_framework
from .models import Imovel
from .serializers import ImovelSerializer


class ImovelViewSet(viewsets.ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    filter_backends = [filters.OrderingFilter,
                       filters.SearchFilter,
                       django_filters.rest_framework.DjangoFilterBackend]
    search_fields = '__all__'
    filterset_fields = '__all__'
    ordering_fields = '__all__'

    http_method_names = ['get', 'post', 'put', 'delete']

    @swagger_auto_schema(responses={200: ImovelSerializer(many=True)})
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(responses={200: ImovelSerializer()})
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(request_body=ImovelSerializer,
                         responses={201: ImovelSerializer()})
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(request_body=ImovelSerializer,
                         responses={200: ImovelSerializer()})
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(responses={204: None})
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
