# Generated by Django 4.2.1 on 2023-05-30 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('requests', '0007_requestmessage_remove_request_reqmail'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='userid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
