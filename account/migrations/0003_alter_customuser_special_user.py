# Generated by Django 4.0.6 on 2022-07-28 12:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customuser_is_author_customuser_special_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='special_user',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='وضعیت اشتراک ویژه'),
        ),
    ]
