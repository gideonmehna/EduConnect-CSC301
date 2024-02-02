from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from Accounts.views import AccountView, UpdateView, LoginView, DeleteAccountView, LogOutView, getAccountView, \
    get_user_session, UpdateSessionToken

from django.urls import path

urlpatterns = [
    path('signup/', AccountView.as_view()),
    path('update/', UpdateView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginView.as_view()),
    path('<int:pk>/delete/', DeleteAccountView.as_view()),
    path('logout/', LogOutView.as_view()),
    path('<int:id>/user/', getAccountView.as_view()),
    path('session/', get_user_session),
    path('session/update_token/', UpdateSessionToken.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


