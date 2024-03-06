from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from api.views import ReservaViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register('reserva', ReservaViewSet, basename='reserva')

schema_view = get_schema_view(
    openapi.Info(
        title="Documentação da API",
        default_version='v1',
        description="Documentação da API Reserva",
        contact=openapi.Contact(email="antonioaldisio@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
