# Generated by Django 4.2.1 on 2023-05-26 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0003_remove_requests_req_mail_requests_reqmail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reqmails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reqmail', models.TextField(blank=True, verbose_name='Содержание заявки')),
            ],
        ),
        migrations.RemoveField(
            model_name='requests',
            name='reqmail',
        ),
        migrations.AlterField(
            model_name='requests',
            name='request',
            field=models.TextField(blank=True, verbose_name='Заявка'),
        ),
    ]
