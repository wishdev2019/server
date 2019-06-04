# coding:utf-8
'''
@summary: 全局常量设置
'''

import os

DBHOST = os.environ.get('DBHOST', '47.244.129.198')
DBPORT = os.environ.get('DBPORT', '3306')
DBNAME = os.environ.get('DBNAME', 'wish')
DBUSER = os.environ.get('DBUSER', 'root')
DBPASS = os.environ.get('DBPASS', '!@#wish123')

# ===============================================================================
# 数据库设置
# ===============================================================================
# 正式环境数据库设置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DBNAME,
        'USER': DBUSER,
        'PASSWORD': DBPASS,
        'HOST': DBHOST,
        'PORT': DBPORT,
    }
}
