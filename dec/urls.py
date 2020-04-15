from django.urls import path

from .views import get_user_object, create_user, update_user, create_table, search

urlpatterns = [

    path("get_user/", get_user_object(), name='get_user'),
    path("create_user/", create_user(), name='create_user'),
    path("create_table/", create_table(), name='create_user'),
    path("update_user/", update_user(), name='create_user'),
    path("search/", search(), name='search'),
]