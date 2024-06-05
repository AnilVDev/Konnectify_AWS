# Generated by Django 4.2.11 on 2024-04-30 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0008_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="chatnotification",
            name="chat",
        ),
        migrations.RemoveField(
            model_name="chatnotification",
            name="user",
        ),
        migrations.RemoveField(
            model_name="userprofilemodel",
            name="user",
        ),
        migrations.DeleteModel(
            name="ChatModel",
        ),
        migrations.DeleteModel(
            name="ChatNotification",
        ),
        migrations.DeleteModel(
            name="UserProfileModel",
        ),
    ]
