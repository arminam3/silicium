from django.urls import path
from django.contrib.auth import views

from .views import (
                    ArticleListView,
                    ArticleCreateView,
                    ArticleUpdateView,
                    ArticleDeleteView,
                    ArticlePreviewView,
                    ProfileView,
                    CustomLoginView,
                    CustomPasswordChangeView,

                )

app_name = "account"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path(
        "password_change/", CustomPasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    # path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    # path(
    #     "password_reset/done/",
    #     views.PasswordResetDoneView.as_view(),
    #     name="password_reset_done",
    # ),
    # path(
    #     "reset/<uidb64>/<token>/",
    #     views.PasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm",
    # ),
    # path(
    #     "reset/done/",
    #     views.PasswordResetCompleteView.as_view(),
    #     name="password_reset_complete",
    # ),
]

urlpatterns += [
    path('', ArticleListView.as_view(), name="home"),
    path('article/create/', ArticleCreateView.as_view(), name="article_create"),
    path('article/update/<slug:slug>', ArticleUpdateView.as_view(), name="article_update"),
    path('article/delete/<slug:slug>', ArticleDeleteView.as_view(), name="article_delete"),
    path('article/preview/<slug:slug>', ArticlePreviewView.as_view(), name="article_preview"),
    path('profile/', ProfileView.as_view(), name="profile"),
]