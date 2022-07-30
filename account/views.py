from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .forms import ProfileForm
from django.contrib.auth.views import LoginView, PasswordChangeView

from .mixins import (
                    FieldMixin,
                    FormValidMixin,
                    AuthorValidMixin,
                    IsSuperUserMixin,
                    IsAuthorMixin,
                    )
from blog.models import Article


class ArticleListView(LoginRequiredMixin,IsAuthorMixin, generic.ListView):
    # queryset = Article.objects.all()
    template_name = 'registration/home.html'

    def get_queryset(self):
        if self.request.user.is_superuser and self.request.user.is_active:
            queryset = Article.objects.all()
            return queryset

        elif self.request.user.is_active:
            queryset = Article.objects.filter(author=self.request.user)
            return queryset
        else:
            return None

class ArticleCreateView(LoginRequiredMixin,IsAuthorMixin, FieldMixin, FormValidMixin, generic.CreateView):
    model = Article
    template_name = 'registration/article-create-update.html'

    def get_success_url(self):
        return reverse_lazy('account:home')


class ArticlePreviewView(AuthorValidMixin, generic.DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    slug_url_kwarg = 'slug'

class ArticleUpdateView(AuthorValidMixin, FieldMixin, FormValidMixin, generic.UpdateView):
    model = Article
    template_name = 'registration/article-create-update.html'

    def get_object(self, queryset=None):
        return Article.objects.get(slug=self.kwargs['slug'])

    def get_success_url(self):
        return reverse_lazy('account:home')

class ArticleDeleteView(AuthorValidMixin,IsSuperUserMixin, generic.DeleteView):
    model = Article
    slug_url_kwarg = 'slug'
    template_name = 'registration/article_confirm_delete.html'
    success_url = reverse_lazy('account:home')

class ProfileView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = ProfileForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy("account:profile")

    def get_object(self, queryset=None):
        return get_object_or_404(get_user_model(), pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(ProfileView, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class CustomLoginView(LoginView):
    def get_success_url(self):
        if self.request.user.is_superuser or self.request.user.is_author:
            return reverse_lazy('account:home')
        else:
            return reverse_lazy('account:profile')

class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('account:password_change_done')
