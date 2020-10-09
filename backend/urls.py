from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"), 
    path("register", views.register, name="register"),

    #API endpoints
    path("appliances", views.appliances, name="appliances"),
    path("appliances_post", views.appliances_post, name="appliances_post")


]