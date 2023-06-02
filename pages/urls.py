from django.urls import path
from .views import HomePageview, AboutpageView

urlpatterns = [
    path("about/", AboutpageView.as_view(), name="about"),
    path("", HomePageview.as_view(), name="home"),
    
]