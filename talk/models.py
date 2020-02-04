from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TalkType(models.Model):
    name = models.CharField(verbose_name=('カテゴリー'), max_length=100)
    
    _admin_list_display = ['name']

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "カテゴリー"


class TalkModel(models.Model):
    talk        = models.TextField(verbose_name=('メッセージ'))
    read        = models.CharField(verbose_name=('既読'), max_length=100)
    created_at  = models.DateField(verbose_name=('日時'))
    talk_type   = models.ForeignKey(verbose_name=('カテゴリー'), to=TalkType, on_delete=models.PROTECT, null='True')
    user_id     = models.ForeignKey(verbose_name=('ユーザーID'), to=User, on_delete=models.PROTECT, null="True")
    # channels_id = models.ForeignKey(verbose_name=('チャンネルID'), null="True")

    def __str__(self):
        return self.talk

    class Meta:
        verbose_name_plural = "トーク"

class Alubum(models.Model):
    image       = models.ImageField(verbose_name=('画像'), upload_to='', null="True")
    talk_id     = models.ForeignKey(verbose_name=('トークID'), to=TalkModel, on_delete=models.PROTECT, null='False')

    _admin_list_display = ['image']

    # def __str__(self):
    #     return self.image
    
    class Meta:
        verbose_name_plural = "イメージ"





