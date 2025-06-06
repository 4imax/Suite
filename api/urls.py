from api.models import CategoryResource, CourseResource
from tastypie.api import Api
from django.urls import path, include

api = Api(api_name="v1")
api.register(CourseResource())
api.register(CategoryResource())

# Key: Authorization
# Value: ApiKey maxfelix:123456ggggdeeerfe3


urlpatterns = [
    path('', include(api.urls), name="index")
]