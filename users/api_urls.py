from users.api_views import UserViewSet, MailValidateAPI, SMSValidateAPI, CoinBalanceViewSet, NFTBalanceViewSet, \
    TxnCoinViewSet, TxnNFTViewSet
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from users.api_views import RoninPayViewSet



# API Router
api_v1_router = DefaultRouter()
api_v1_router.register(r'roningpays', RoninPayViewSet)
api_v1_router.register(r'users', UserViewSet, basename='user')
api_v1_router.register(r'coinbalance', CoinBalanceViewSet)
api_v1_router.register(r'nftbalance', NFTBalanceViewSet)
api_v1_router.register(r'txncoin', TxnCoinViewSet, basename='txncoin')
api_v1_router.register(r'txnnft', TxnNFTViewSet, basename='txnnft')




urlpatterns = [
    # API URLs
    url(r'1.0/', include(api_v1_router.urls)),
    url(r'1.0/mailvalidate/', MailValidateAPI.as_view(), name="mailvalidate"),
    url(r'1.0/smsvalidate/', SMSValidateAPI.as_view(), name="smsvalidate")


]