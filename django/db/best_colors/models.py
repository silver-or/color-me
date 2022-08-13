from django.db import models

from db.personal_colors.models import PersonalColor


class BestColor(models.Model):
    use_in_migrations = True
    color = models.CharField(primary_key=True, max_length=30)
    hex = models.TextField()
    rgb = models.TextField()
    img_path = models.TextField(null=True, default='')

    '''
    하나의 퍼스널컬러는 여러 best 컬러를 가질 수 있다.
    이때 테이블의 관계는 OneToMany로 설정할 수 있다.
    OneToMany 관계를 만들기 위해 ForeignKey를 지정해주어야 한다.
    '''
    type = models.ForeignKey(PersonalColor, on_delete=models.CASCADE)

    class Meta:
        db_table = "best_colors"

    def __str__(self):
        return f'{self.pk} {self.color}'
