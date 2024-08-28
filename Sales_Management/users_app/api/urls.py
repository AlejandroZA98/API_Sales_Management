from django.urls import path 
from users_app.api.views.registration_user import RegisterUser
from users_app.api.views.logout_user import LogoutUser
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView # type: ignore

urlpatterns =[
    path('register/',RegisterUser.as_view(),name='register'),#registrar usuario
    path('logout/',LogoutUser.as_view(),name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),#generar tokens con JWT(puede ser usado como login)
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]