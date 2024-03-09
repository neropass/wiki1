from django.urls import path

from . import views

app_name = "wikipedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.get_article, name="get_article"),
    path("search", views.search, name="search")
]
