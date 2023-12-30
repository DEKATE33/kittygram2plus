from django.http import HttpResponse
from rest_framework.pagination import PageNumberPagination


class CatsPagination(PageNumberPagination):
    page_size = 20


class CustomPagination(PageNumberPagination)
    def paginate_queryset(self, queryset, request, view=None):
        return super().paginate_queryset(queryset, request, view)
    
    def get_paginated_response(self, data):
        data = {
            'count': self.page.paginator.count,
            'response': data
        }
        return super().get_paginated_response(data)
    
HttpResponse
