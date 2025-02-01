from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)  # 空白可にする場合は`blank=True`
    expiry = models.DateField()

    def __str__(self):
        return self.title

    class Meta:     
        db_table='task'



