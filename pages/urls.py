from django.urls import path

from .views import HomePageView, TapTheTablePageView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('register/', TapTheTablePageView.as_view(), name='tap_the_table'),
]