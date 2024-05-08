from django.urls import path, include
from django.conf import settings

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.users import urls as users
from apps.api import urls as apis

schema_view = get_schema_view(
    openapi.Info(
        title="Initialize_django_jiwonman",
        default_version="0.1.0",
        description="users, api 문서",
        # terms_of_service="http://127.0.0.1:8000",
        contact=openapi.Contact(
            name="jiwonman",
            url="https://coddingjiwon.tistory.com/",
            email="kusa1230@naver.com",
        ),
        license=openapi.License(name="mit"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("users/", include(users)),
    path("api/", include(apis)),
]

if settings.DEBUG:
    urlpatterns += [
        # path(
        #     r"swagger(?P<format>\.json|\.yaml)",
        #     schema_view.without_ui(cache_timeout=0),
        #     name="schema-json",
        # ),
        path(
            r"swagger",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            r"redoc",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc-v1",
        ),
    ]
