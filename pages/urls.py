from django.urls import path

from .views import HomePageView, RegisterPageView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('register/', RegisterPageView.as_view(), name='register'),
]