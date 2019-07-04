
import requests


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
        print("123123123")


print(get_ip_info('49.144.216.13'))