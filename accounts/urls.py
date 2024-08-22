from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts.views import CustomUserViewset, RegistrationViews, LoginViewset, LogoutView, ProfileViewset


router = DefaultRouter()

router.register(r"users", CustomUserViewset,basename="users")
router.register(r"profile", ProfileViewset, basename="profile")

urlpatterns = [
    path("", include(router.urls)),

    path("registration/", RegistrationViews.as_view(), name="registration"),
    path("login/", LoginViewset.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]