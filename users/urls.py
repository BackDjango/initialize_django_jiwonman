from django.urls import path, include
from users import views 

urlpatterns = [
    path('signup/', views.SignUpAPIView.as_view(), name='signup')
]
