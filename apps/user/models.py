import binascii
import os
import time
from django.db import models
from django.utils import timezone

from libs.utils.string_extension import md5pass

class Token(models.Model):

    key = models.CharField(max_length=160, primary_key=True)
    userid  = models.BigIntegerField()
    ip = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Token'
        verbose_name_plural = verbose_name
        db_table="user_token"

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(80)).decode()

    def __str__(self):
        return self.key

class Users(models.Model):

    userid=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=120,verbose_name="名称",default='',null=True)
    rolecode = models.CharField(max_length=4,verbose_name="角色 1000-管理员,2001-玩家",default='2001')
    loginname=models.CharField(max_length=60,verbose_name="登录名称",default='',null=True)
    passwd=models.CharField(max_length=60,verbose_name='密码',default='')
    pay_passwd=models.CharField(max_length=60,verbose_name='支付密码',default='')
    pic=models.CharField(max_length=255,verbose_name="头像",default='')
    createtime=models.BigIntegerField(default=0)
    createman = models.BigIntegerField(default=0)
    createman_name = models.CharField(max_length=120,default='')
    status = models.IntegerField(default='0',verbose_name="状态:0-正常,1-删除,2-冻结",null=True)

    email  = models.CharField(max_length=60,verbose_name="邮箱",default="")
    concat = models.CharField(max_length=60,verbose_name='联系人',default="")
    mobile = models.CharField(max_length=20,verbose_name="手机号",default="")
    contype = models.CharField(max_length=60,verbose_name="联系方式",default="")

    bal = models.DecimalField(max_digits=18,decimal_places=6,default=0.000,verbose_name="余额")
    cashout_bal = models.DecimalField(max_digits=18,decimal_places=6,default=0.000,verbose_name="提现金额")

    up_bal = models.DecimalField(max_digits=18,decimal_places=6,default=0.000,verbose_name="码商流水")

    google_token = models.CharField(max_length=60,verbose_name="google_token",default="")


    ipname = None
    ip = None

    def save(self, *args, **kwargs):
        t=time.mktime(timezone.now().timetuple())

        if not self.createtime:
            self.createtime = t
        if not self.passwd :
            self.passwd = md5pass('123456')
        if not self.pay_passwd:
            self.pay_passwd = md5pass('123456')
        if not self.loginname:
            self.loginname = self.name
        return super(Users, self).save(*args, **kwargs)

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
        db_table = 'user'

class Login(models.Model):

    id=models.BigAutoField(primary_key=True)
    userid=models.BigIntegerField(default=0)
    createtime=models.BigIntegerField(default=0)
    ip = models.CharField(verbose_name="IP",max_length=60)


    ipname = None

    def save(self, *args, **kwargs):
        t=time.mktime(timezone.now().timetuple())

        if not self.createtime:
            self.createtime = t
        return super(Login, self).save(*args, **kwargs)

    class Meta:
        verbose_name = '登陆表'
        verbose_name_plural = verbose_name
        db_table = 'login'