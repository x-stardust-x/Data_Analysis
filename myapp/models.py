from django.db import models

# Create your models here.


class task(models.Model):
    obj_project = models.CharField(max_length=100,default='')  # 儲存任務編號
    parent_task = models.CharField(max_length=100,default='')  # 儲存母任務的編號
    obj_user = models.EmailField(default='')  # 儲存任務發起人的信箱
    uuid = models.CharField(max_length=100,default='')  # 儲存任務代碼
    type_task = models.CharField(max_length=100,default='')  # 儲存任務類別的代號
    name = models.CharField(max_length=100,default='')  # 儲存任務名稱
    overview = models.TextField(default='')  # 儲存任務說明
    content = models.JSONField()  # 儲存一串字典
    weight = models.JSONField()  # 儲存一串字典
    token = models.IntegerField()  # 儲存一個數字
    period = models.CharField(max_length=100,default='')  # 儲存一段時間段
    gps_flag = models.CharField(max_length=3,default='NO')  # 儲存選項 "YES" 或 "NO"
    def __str__(self):
        return self.name
