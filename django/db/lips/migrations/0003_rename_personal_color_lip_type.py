# Generated by Django 4.1 on 2022-08-07 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lips", "0002_alter_lip_img_path"),
    ]

    operations = [
        migrations.RenameField(
            model_name="lip", old_name="personal_color", new_name="type",
        ),
    ]
