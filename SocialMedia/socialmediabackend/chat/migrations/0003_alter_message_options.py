# Generated by Django 4.2.11 on 2024-04-18 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0002_alter_chat_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="message",
            options={"ordering": ["created"]},
        ),
    ]
