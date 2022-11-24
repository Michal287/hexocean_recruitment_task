from rest_framework.pagination import PageNumberPagination


class ImageCreateListViewPagination(PageNumberPagination):
    page_size = 5
