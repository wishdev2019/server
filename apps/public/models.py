import time
from django.db import models
from django.utils import timezone

from libs.utils.string_extension import md5pass

class Memu(models.Model):

    id=models.AutoField(primary_key=True)
    label = models.CharField(max_length=30,verbose_name="名称")
    path = models.CharField(max_length=255,verbose_name="路径")
    icon = models.CharField(max_length=30,verbose_name="icon")
    parentid = models.IntegerField(verbose_name="组号 0,1,2")
    i18n = models.CharField(max_length=60,verbose_name="翻译关键字")
    keepalive = models.CharField(verbose_name="是否缓存 0-是,1-否",max_length=1,default='1')
    component = models.CharField(verbose_name="组件",max_length=120,default="")

    last_menu_id = models.IntegerField(verbose_name="上级菜单ID",default=0)
    no = models.IntegerField(verbose_name="序号")
    level = models.IntegerField(verbose_name="层级",default=0)
    type = models.CharField(max_length=1,verbose_name="0-top , 1-left ,2-right菜单")

    rolecode = models.CharField(max_length=4,default="all")

    meta = None

    class Meta:
        verbose_name = '菜单表'
        verbose_name_plural = verbose_name
        db_table = 'menu'


class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="标题",max_length=100)
    content = models.TextField(verbose_name="内容")
    createtime = models.BigIntegerField(verbose_name="创建时间")

    def save(self, *args, **kwargs):
        t=time.mktime(timezone.now().timetuple())

        if not self.createtime:
            self.createtime = t
        return super(Notice, self).save(*args, **kwargs)

    class Meta:
        verbose_name = '公告表'
        verbose_name_plural = verbose_name
        db_table = 'notice'


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    bigtype = models.CharField(verbose_name="彩票大类",max_length=60)
    type  = models.CharField(verbose_name="彩票小类",max_length=60)
    createtime = models.BigIntegerField(verbose_name='创建时间')
    bigno = models.IntegerField(verbose_name="大类排序")
    no = models.IntegerField(verbose_name="小类排序")

    def save(self, *args, **kwargs):
        t=time.mktime(timezone.now().timetuple())

        if not self.createtime:
            self.createtime = t
        return super(Ticket, self).save(*args, **kwargs)

    class Meta:
        verbose_name = '彩票信息'
        verbose_name_plural = verbose_name
        db_table = 'ticket'