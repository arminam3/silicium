from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from blog.models import Article
# @login_required
# def home_view(request):
#     return render(request, 'registration/home.html')

class ArticleListView(LoginRequiredMixin, generic.ListView):
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

class ArticleCreateView(LoginRequiredMixin, generic.CreateView):
    model = Article
    template_name = 'registration/article-create-update.html'
    fields = ['author', 'title', 'slug', 'category', 'descriptions', 'thumbnail', 'published', 'status']

    def form_valid(self, form):
        form.instance.author == self.request.user
        return super(ArticleCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('account:home')