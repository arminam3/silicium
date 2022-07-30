from django.contrib import admin
from django.utils.translation import ngettext
from django.contrib import messages
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


from .models import Article, Category

from django.contrib.auth.admin import UserAdmin
UserAdmin.fieldsets[2][1]['fields'] = (
    "is_active",
    "is_staff",
    "is_superuser",
    "is_author",
    "special_user",
    "groups",
    "user_permissions",
)
UserAdmin.list_display += (
    'is_author',
    'is_special_user',
)


admin.site.register(get_user_model(), UserAdmin)

# def make_published(modeladmin, request, queryset):
#     queryset.update(status='p')


admin.site.site_header = 'وبلاگ جنگویی'
# admin.site.disable_action('delete_selected')
# @admin.action(description='Mark selected stories as published')
def make_published(modeladmin, request, queryset):
    updated = queryset.update(status='p')
    modeladmin.message_user(request, ngettext(
        '%d مقاله منتشر شد.',
        '%d مقاله منتشر شدند.',
        updated,
    ) % updated, messages.SUCCESS)


def make_draft(modeladmin, request, queryset):
    updated = queryset.update(status='d')
    modeladmin.message_user(request, ngettext(
        '%d عدد از مقالات تغییر یافت',
        '%d عدد از مقالات تغییر یافتند',
        updated
    ) % updated, messages.SUCCESS)

def make_armin(modeladmin, request, queryset):
    updated = queryset.update(author=1)
    modeladmin.message_user(request,
                           '%d مورد تغییر یافت' % updated,
                            messages.SUCCESS
                            )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'author', 'is_special', 'status', 'jalali_published', 'category_to_str']
    list_editable = ['status', 'author']
    list_filter = ['status', 'author']
    search_fields = ['title', 'status']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['created']

    actions = [make_published, make_draft, make_armin]
    make_published.short_description = 'منتشر کردن'
    make_draft.short_description = 'پیش نویس کردن'
    make_armin.short_description = 'Armin'

    # def category_to_str(self, obj):
    #     return ', '.join([category.title for category in obj.category_published()])








@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['position', 'title', 'slug', 'parent', 'status']
    list_editable = ['status']
    list_filter = (['status'])
    search_fields = ['slug', 'status']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-parent']





