# Generated by Django 3.2.15 on 2024-06-26 06:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('bkmonitor', '0163_auto_20240619_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='bcspod',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='bcscontainer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
