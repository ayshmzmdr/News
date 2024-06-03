from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("local/",views.lnews,name="local"),
    path("national/",views.nnews,name="national"),
    path("international/",views.inews,name="international")
]