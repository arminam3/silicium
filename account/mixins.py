from django.http import Http404
from django.shortcuts import get_object_or_404, redirect

from blog.models import Article

class FieldMixin():
    def dispatch(self, request, *args, **kwargs):
        self.fields = ['title', 'slug', 'category', 'descriptions', 'thumbnail', 'published', 'status', 'is_special']
        if request.user.is_superuser:
            self.fields.append("author")
        return super().dispatch(request, *args, **kwargs)

class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            obj = form.save(commit=False)
            obj.author = self.request.user
            if not obj.status in ['d', 'i']:
                obj.status = 'd'
            obj.save()
        return super().form_valid(form)

class AuthorValidMixin():
    def dispatch(self, request, *args, **kwargs):
        obj = get_object_or_404(Article, slug=kwargs['slug'])
        if self.request.user.is_superuser or obj.author == request.user and obj.status in ['b', 'd']:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("account:profile")

class IsSuperUserMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404
class IsAuthorMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_author or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('account:profile')
