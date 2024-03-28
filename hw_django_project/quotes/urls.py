from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path("add_author/", views.add_author, name="add_author"),
    path("add_quote/", views.add_quote, name="add_quote"),
    path("my_authors/", views.my_authors, name="my_authors"),
    path("my_quotes/", views.my_quotes, name="my_quotes"),
    path('authors/<str:author_fullname>/', views.author_info, name='author_info'),
    path('search/', views.search, name='search'),
    path('tag/<str:tag>/', views.quotes_by_tag, name='quotes_by_tag'),
]