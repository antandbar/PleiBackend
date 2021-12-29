from django.contrib import admin
from django.conf.urls import url, include
from users import api_urls as users_api_url
from internal import api_urls as internal_api_url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # users URLS
    url(r'users/api/', include(users_api_url)),
    url(r'internal/api/', include(internal_api_url)),

    # static
    url(r'', include(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))),

]

"""
urlpatterns = [
    path('admin/', admin.site.urls),

    # Users path
    path('login/', login),
    path('logout/', logout),

    # Users API
    path('api/1.0/users/', UserListAPI.as_view()),
    path('api/1.0/users/<int:pk>', UserDetailAPI.as_view()),
    path('api/1.0/roningpay/', RoningPayAPI.as_view()),
    path('api/1.0/roningpay/<int:pk>', RoningPayDetailAPI.as_view()),

]
"""
