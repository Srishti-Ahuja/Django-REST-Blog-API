from rest_framework.throttling import UserRateThrottle

class BlogPostThrottle(UserRateThrottle):
    scope = 'blogpost'
