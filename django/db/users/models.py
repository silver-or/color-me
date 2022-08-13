from django.db import models

from db.personal_colors.models import PersonalColor


class User(models.Model):
    use_in_migrations = True
    email = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=10)
    username = models.TextField()
    birth = models.TextField()
    gender = models.TextField()

    type = models.OneToOneField(PersonalColor, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return f'{self.pk} {self.email}'
