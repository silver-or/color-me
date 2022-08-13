from django.db import models

from db.personal_colors.models import PersonalColor


class Lip(models.Model):
    use_in_migrations = True
    product_name = models.CharField(primary_key=True, max_length=50)
    brand = models.TextField()
    color = models.TextField()
    img_path = models.TextField(null=True, default='')

    type = models.ForeignKey(PersonalColor, on_delete=models.CASCADE)

    class Meta:
        db_table = "lips"

    def __str__(self):
        return f'{self.pk} {self.product_name} {self.brand} {self.color}'
