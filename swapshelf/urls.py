from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path, re_path
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.BASE_DIR / "market" / "static"}),
    path("", include("market.urls")),
]
