from django.db.models import Q
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


# class StockFilter(django_filters.FilterSet):
#     products = django_filters.NumberFilter()
#     class Meta:
#         model = Stock
#         fields = ['products__id']


class StockSearchFilter(SearchFilter):
    def filter_queryset(self, request, queryset, view):
        queryset = super().filter_queryset(request, queryset, view)
        param = request.query_params.get('products')
        if param:
            print('True')
        else:
            return queryset


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [SearchFilter]
    filter_class = StockSearchFilter
