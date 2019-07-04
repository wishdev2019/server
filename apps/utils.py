from rest_framework import (viewsets)

from education.settings import ServerUrl
from apps.user.models import Users
from utils.exceptions import PubErrorCustom
import requests

class GenericViewSetCustom(viewsets.ViewSet):

    pass

def get_ip_info(ip):

    r = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=%s' % ip)
    if r.json()['code'] == 0:
        i = r.json()['data']
        country = i['country']  # 国家
        area = i['area']  # 区域
        region = i['region']  # 地区
        city = i['city']  # 城市
        isp = i['isp']  # 运营商
        return  u'%s%s%s' % (country,  region, city)
    else:
        raise PubErrorCustom("IP不正确!")
