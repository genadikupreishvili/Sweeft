from django.urls import path
from . import views

urlpatterns = [
    path('url', views.create_short_url, name='create_short_url'),
    path('url/<str:short_url>', views.redirect_short_url, name='redirect_short_url'),
]
