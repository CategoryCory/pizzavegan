from django.urls import path

from .views import HomePageView, TapTheTablePageView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('tap-the-table/', TapTheTablePageView.as_view(), name='tap_the_table'),
]