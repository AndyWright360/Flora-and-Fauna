# Generated by Django 3.2.25 on 2024-05-06 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0002_review_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='user_profile',
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]