# Generated by Django 4.1 on 2022-08-06 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "email",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("password", models.CharField(max_length=10)),
                ("username", models.TextField()),
                ("birth", models.TextField()),
                ("gender", models.TextField()),
            ],
            options={"db_table": "users",},
        ),
    ]
