# Generated by Django 4.1 on 2022-08-07 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PersonalColor",
            fields=[
                (
                    "type",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
            ],
            options={"db_table": "personal_colors",},
        ),
    ]
