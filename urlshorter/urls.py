from django.urls import path
from .views import home
from .views import  redirect_url_view

appname = "shorter"

urlpatterns = [
    
    path("", home, name="home"),
    path('<str:shortened_part>', redirect_url_view, name='redirect'),
]