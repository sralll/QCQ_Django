# Generated by Django 5.2 on 2025-05-09 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("play", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userresult",
            name="filename",
            field=models.CharField(default="unknown", max_length=255),
        ),
    ]
