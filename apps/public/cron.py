#
# import os
# import sys
# import django
# pathname = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, pathname)
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "education.settings")
#
# django.setup()
#
# from django.db import transaction
# from apps.order.models import Order
# from libs.utils.mytime import UtilTime

def order_valid_task():
    pass
#     """
#     订单过期处理,每天凌晨1点处理昨天的过期情况
#     :return:
#     """
#     with transaction.atomic():
#         ut = UtilTime()
#         # last_day_time = ut.string_to_timestamp(ut.arrow_to_string(ut.today.replace(days=-1), format_v="YYYY-MM-DD") + ' 00:00:01')
#         today_time = ut.string_to_timestamp(ut.arrow_to_string(ut.today,format_v="YYYY-MM-DD")+' 00:00:01')
#         Order.objects.filter(createtime__lte=today_time,status="1").update(status="3")