from rest_framework import filters


class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('products'):
            return ['products__id']
        return super().get_search_fields(view, request)
