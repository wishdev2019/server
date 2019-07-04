from django.db import models

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