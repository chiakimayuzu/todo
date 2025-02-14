from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)  # 空白可にする場合は`blank=True`
    expiry = models.DateField()

    def __str__(self):
        return self.title

    class Meta:     
        db_table='task'
    
    def clean_title(self): #titleの重複登録不可
        if Task.objects.filter(title=self.title).exclude(pk=self.pk).exists():
            raise ValidationError("このタスク名は既に登録されています。")

    def clean_expiry(self): #過去の日付を禁止するバリデーション
        if self.expiry < now().date():
            raise ValidationError('過去の日付は設定できません')

    def clean(self):  # フィールド全体のバリデーションをまとめる
        self.clean_title()  # `clean_title()` を実行
        self.clean_expiry()  # `clean_expiry()` を実行    

