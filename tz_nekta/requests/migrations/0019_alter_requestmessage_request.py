# Generated by Django 4.2.1 on 2023-05-31 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0018_remove_requestmessage_request_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestmessage',
            name='request',
            field=models.TextField(blank=True, verbose_name='id заявки'),
        ),
    ]
