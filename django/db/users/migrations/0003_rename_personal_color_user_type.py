# Generated by Django 4.1 on 2022-08-07 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_personal_color"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user", old_name="personal_color", new_name="type",
        ),
    ]