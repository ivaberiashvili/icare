from django.contrib import admin
from django.urls import path, include
from core.views import HomeView, APIView, PostListView
from core.views import RankedProductsView, ProductListCreate, ProductRetrieveUpdateDestroy
from rest_framework import permissions
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('api/', APIView.as_view()),
    path('blog/', PostListView.as_view()),
    path('ranked-products/', RankedProductsView.as_view(), name='ranked-products'),
    path('api-auth/', include('rest_framework.urls')),

    # DRF Product API
    path('products/', ProductListCreate.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-detail'),

    # drf-spectacular schema and docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
