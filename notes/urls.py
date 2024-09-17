from django.urls import path
from .views import (
    register_view,
    login_view,
    note_list_view,
    note_create_view,
    note_update_view,
    note_delete_view,
    home_view,
    logout_view,
    login_prompt_view,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", home_view, name="home"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("notes/", note_list_view, name="note-list"),
    path("notes/create/", note_create_view, name="note-create"),
    path("notes/<int:pk>/edit/", note_update_view, name="note-update"),
    path("notes/<int:pk>/delete/", note_delete_view, name="note-delete"),
    path("login_prompt/", login_prompt_view, name="login_prompt"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
