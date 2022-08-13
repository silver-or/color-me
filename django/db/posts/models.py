from django.db import models

from db.personal_colors.models import PersonalColor


class Post(models.Model):
    use_in_migrations = True
    '''
    기본적으로, Django에서는 각각의 모델에 id필드를 자동으로 추가해준다.
    다만, primary_key가 명시되어있는 컬럼이 있을 경우 추가하지 않는다.
    자동추가되는 id필드는 auto_increment integer field이다.
    '''
    # auto_increment_id = models.AutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    thumbnail = models.TextField(null=True, default='')
    # 링크 연결은 안 함.

    type = models.ForeignKey(PersonalColor, on_delete=models.CASCADE)

    class Meta:
        db_table = "posts"

    def __str__(self):
        return f'{self.pk} {self.title}'
