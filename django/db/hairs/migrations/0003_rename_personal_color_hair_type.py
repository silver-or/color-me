# Generated by Django 4.1 on 2022-08-07 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hairs", "0002_alter_hair_img_path"),
    ]

    operations = [
        migrations.RenameField(
            model_name="hair", old_name="personal_color", new_name="type",
        ),
    ]