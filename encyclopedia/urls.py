from django.urls import path

from . import views

app_name = "wikipedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.get_article, name="get_article"),
    path("search/", views.search, name="search"),
    path("random/", views.random_page, name="random_page"),
    path("create/", views.create_article, name="create_article")
]
