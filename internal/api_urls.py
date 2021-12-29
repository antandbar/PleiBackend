from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from internal.api_views import UserInternalViewSet, GamerInternalViewSet, ScholarInternalViewSet




# API Router
api_v1_router = DefaultRouter()

api_v1_router.register(r'user_internal', UserInternalViewSet, basename='user_internal')
api_v1_router.register(r'gamer_internal', GamerInternalViewSet, basename='gamer_internal')
api_v1_router.register(r'scholar_internal', ScholarInternalViewSet, basename='scholar_internal')


urlpatterns = [
    # API URLs
    url(r'1.0/', include(api_v1_router.urls)),


]