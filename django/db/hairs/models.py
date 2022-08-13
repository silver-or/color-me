from django.db import models

from db.personal_colors.models import PersonalColor


class Hair(models.Model):
    use_in_migrations = True
    color = models.CharField(primary_key=True, max_length=50)
    hex = models.TextField()
    rgb = models.TextField()
    img_path = models.TextField(null=True, default='')

    type = models.ForeignKey(PersonalColor, on_delete=models.CASCADE)

    class Meta:
        db_table = "hairs"

    def __str__(self):
        return f'{self.pk} {self.color}'
