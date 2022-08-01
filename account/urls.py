from django.urls import path
from django.contrib.auth import views

from .views import (
                    ArticleListView,
                    ArticleCreateView,
                    ArticleUpdateView,
                    ArticleDeleteView,
                    ArticlePreviewView,
                    ProfileView,

                )

app_name = "account"


urlpatterns = [
    path('', ArticleListView.as_view(), name="home"),
    path('article/create/', ArticleCreateView.as_view(), name="article_create"),
    path('article/update/<slug:slug>', ArticleUpdateView.as_view(), name="article_update"),
    path('article/delete/<slug:slug>', ArticleDeleteView.as_view(), name="article_delete"),
    path('article/preview/<slug:slug>', ArticlePreviewView.as_view(), name="article_preview"),
    path('profile/', ProfileView.as_view(), name="profile"),
]