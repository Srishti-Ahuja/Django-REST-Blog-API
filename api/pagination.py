from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class BlogPagination(LimitOffsetPagination):
    page_size = 4
    offset_query_param = 'starting'

class CommentPagination(PageNumberPagination):
    page_size = 3
    default_limit = 3
    page_size_query_param = 'size'
    last_page_strings = ('last', 'end', )
