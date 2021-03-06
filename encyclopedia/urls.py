from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.entry, name="entry"), #entry
    path("search/",views.search, name="search"),
    path("newPage/",views.newPage,name="newPage"),
    path("random/",views.randomPage,name="randomPage"),
    path("wiki/<str:title_edit>/edit/",views.edit, name="edit") #edit
]
