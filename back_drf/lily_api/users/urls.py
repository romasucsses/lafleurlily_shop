from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import MyAccountInfoAPIView, MyAddressInfoAPIView, MyOrdersInfoAPIView, MyDetailOrderInfoAPIView, SingUpAPIView

my_account_urls = [
    path('', MyAccountInfoAPIView.as_view(), name='account_details'),
    path('view-my-shipping-info/', MyAddressInfoAPIView.as_view(), name='account_shipping'),
    path('my-orders/', MyOrdersInfoAPIView.as_view(), name='all_user_orders'),
    path('my-detail-order/<int:pk>/', MyDetailOrderInfoAPIView.as_view(), name='all_user_orders'),
]

urlpatterns = [
    path('get-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('get-refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get-verify-token/', TokenVerifyView.as_view(), name='token_verify'),
    path('my-account-details/', include(my_account_urls)),
    path('sign-up/', SingUpAPIView.as_view(), name='sign_up_view')
]
