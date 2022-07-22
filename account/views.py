from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from blog.models import Article
# @login_required
# def home_view(request):
#     return render(request, 'registration/home.html')

class ArticleListView(LoginRequiredMixin, generic.ListView):
    queryset = Article.objects.all()
    template_name = 'registration/home.html'