# Generated by Django 4.1 on 2022-08-07 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("skins", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="skin",
            name="img_path",
            field=models.TextField(default="", null=True),
        ),
    ]
