from django.db import models


class PersonalColor(models.Model):
    use_in_migrations = True

    type = models.CharField(primary_key=True, max_length=30)

    # Django doesn't have ArrayField when if DB is MySql. It has ArrayField if DB is Postgresql.
    # posts = models.TextField()

    class Meta:
        db_table = "personal_colors"

    def __str__(self):
        return f'{self.pk} {self.type}'
