from django.db import models

from db.personal_colors.models import PersonalColor


class Youtuber(models.Model):
    use_in_migrations = True
    name = models.CharField(primary_key=True, max_length=30)
    img_path = models.TextField(null=True, default='')
    # 링크 연결은 안 함.

    type = models.ForeignKey(PersonalColor, on_delete=models.CASCADE)

    class Meta:
        db_table = "youtubers"

    def __str__(self):
        return f'{self.pk} {self.name}'
