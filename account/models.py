from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="ایمیل")
    is_author = models.BooleanField(default=False, verbose_name="وضعیت نویسنده بودن")
    special_user = models.DateTimeField(default=timezone.now, verbose_name='وضعیت اشتراک ویژه')

    def is_special_user(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False
    is_special_user.boolean = True
    is_special_user.short_description = 'وضعیت اشتراک ویژه'

