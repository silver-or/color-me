# Generated by Django 4.1 on 2022-08-07 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("youtubers", "0002_alter_youtuber_img_path"),
    ]

    operations = [
        migrations.RenameField(
            model_name="youtuber", old_name="personal_color", new_name="type",
        ),
    ]
