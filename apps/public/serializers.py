from rest_framework import serializers
from apps.public.models import Memu,Notice,Ticket
from apps.user.models import Users,Login
from django.utils import timezone
from rest_framework.validators import UniqueTogetherValidator
from apps.utils import get_ip_info

from libs.utils.mytime import timestamp_toTime,UtilTime



class NoticeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'

class TicketModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class MenuModelSerializer(serializers.ModelSerializer):

	meta = serializers.SerializerMethodField()

	def get_meta(self,obj):
		return {
			"i18n": obj.i18n,
			"keepAlive": True if obj.keepalive == '0' else False
		}

	class Meta:
		model = Memu
		fields = '__all__'


class ManageSerializer(serializers.Serializer):

    userid = serializers.IntegerField()
    loginname = serializers.CharField()
    name  = serializers.CharField()
    ipname = serializers.SerializerMethodField()

    logintime = serializers.SerializerMethodField()
    logincount = serializers.SerializerMethodField()

    bal = serializers.DecimalField(max_digits=18,decimal_places=2)

    def get_logintime(self,obj):
        login=Login.objects.filter(userid=obj.userid).order_by("-createtime")
        return timestamp_toTime(login[0].createtime) if login.exists() else ""

    def get_logincount(self,obj):
        return Login.objects.filter(userid=obj.userid).count()

    def get_ipname(self,obj):
        login = Login.objects.filter(userid=obj.userid).order_by("-createtime")
        ip = login[0].ip if login.exists() else ""
        print(ip)
        return get_ip_info(ip)