
from rest_framework import viewsets
from rest_framework.decorators import list_route
from core.decorator.response import Core_connector

from auth.authentication import Authentication

from apps.user.models import Token
from apps.public.models import Memu,Notice,Ticket
from django.db.models import Q
from utils.exceptions import PubErrorCustom
from apps.public.serializers import MenuModelSerializer,ManageSerializer,NoticeModelSerializer,TicketModelSerializer
from apps.user.serializers import UsersSerializer1

from apps.user.models import Users


class PublicAPIView(viewsets.ViewSet):

    def get_authenticators(self):
        return [auth() for auth in [Authentication]]


    @list_route(methods=['GET'])
    @Core_connector()
    def notice(self,request, *args, **kwargs):

        return {"data" : NoticeModelSerializer(Notice.objects.filter().order_by('-createtime')[:10],many=True).data}


    @list_route(methods=['GET'])
    @Core_connector()
    def ticket(self,request, *args, **kwargs):

        return {"data" : TicketModelSerializer(Ticket.objects.filter().order_by('bigno','no'),many=True).data}

    @list_route(methods=['GET'])
    @Core_connector(pagination=True)
    def manageadd_query(self,request, *args, **kwargs):
        query = Users.objects.filter(status=0)
        if str(request.user.rolecode) == '2001':
            query = query.filter(rolecode=2001,userid=request.user.userid)
        else:
            if request.query_params_format.get('rolecode'):
                query = query.filter(rolecode=request.query_params_format.get('rolecode'))
            else:
                request.query_params_format.get('rolecode')
                query = query.filter(rolecode=1000)

        return  {"data":  ManageSerializer(query,many=True).data}

    @list_route(methods=['POST'])
    @Core_connector(transaction=True)
    def manageadd_del(self,request, *args, **kwargs):
        userid = request.data_format.get('userid')

        try:
            user=Users.objects.get(userid=userid)
            user.status = 1
            user.save()
        except Users.DoesNotExist:
            raise PubErrorCustom("此账号不存在!")

        return None

    @list_route(methods=['POST'])
    @Core_connector(transaction=True, serializer_class=UsersSerializer1, model_class=Users)
    def manageadd_add(self,request, *args, **kwargs):

        print(request.data_format)
        serializer = kwargs.pop('serializer')
        isinstance = serializer.save()
        isinstance.createman = request.user.userid
        isinstance.createman_name = request.user.name
        isinstance.status = 0
        isinstance.save()

        return {"msg": "添加成功！"}

    @list_route(methods=['POST'])
    @Core_connector(transaction=True)
    def manageadd_upd(self,request, *args, **kwargs):

        print(request.data_format)
        serializer=UsersSerializer1(Users.objects.get(userid=request.data_format.get("userid")),data=request.data_format)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return None

    @list_route(methods=['GET'])
    @Core_connector(pagination=True)
    def get_qrtype(self, request):
        pass


    #获取菜单
    @list_route(methods=['GET'])
    @Core_connector()
    def get_menu(self,request, *args, **kwargs):

        menus = MenuModelSerializer(Memu.objects.filter(Q(rolecode='all') | Q(rolecode=request.user.rolecode),type='1'),many=True).data

        def childinsert(last_menu_id):
            childs = []
            for item in menus :
                if item['last_menu_id'] == last_menu_id:
                    tmp_data = {}
                    for tmp_item in item:
                        tmp_data[tmp_item] = item[tmp_item]
                    tmp_data['meta'] = {
                        "i18n" : tmp_data['i18n'],
                        "keepAlive" : True if tmp_data['keepalive']=='0' else False
                    }
                    childs.append(tmp_data)
            if childs:
                childs = sorted(childs, key=lambda e: e['no'], reverse=False)
            return None if not len(childs) else childs

        data = []
        for item in menus :
            if item['level'] == 1:
                tmp_data = {}
                for tmp_item in item:
                    tmp_data[tmp_item] = item[tmp_item]
                tmp_data['meta'] = {
                    "i18n": tmp_data['i18n'],
                    "keepAlive": True if tmp_data['keepalive'] == '0' else False
                }
                data.append(tmp_data)

        data=sorted(data, key=lambda e: e['no'], reverse=False)
        itemdata = data
        while True:
            inner_data = itemdata
            itemdata = []
            for item in inner_data:
                if isinstance(item,dict):
                    child = childinsert(item['id'])
                    if child:
                        item['children'] = child
                        itemdata.append(child)
                    else:
                        item['children']=[]
                elif isinstance(item,list):
                    for inner_item in item :
                        child = childinsert(inner_item['id'])
                        if child:
                            inner_item['children'] = child
                            itemdata.append(child)
                        else:
                            inner_item['children']=[]
            if not len(itemdata):
                break
        return {"data":data}


    #获取用户信息
    @list_route(methods=['GET'])
    @Core_connector()
    def get_userinfo(self,request):

        return {"data":{
            "userInfo" : {
                "username" : request.user.loginname,
                "name" : request.user.name,
                'rolecode' : request.user.rolecode,
                "avatar": 'http://allwin6666.com/nginx_upload/assets/login.jpg',
                'bal' : request.user.bal,
                'up_bal' : request.user.up_bal,
                'cashout_bal' : request.user.cashout_bal
            },
            "roles" : request.user.rolecode,
            "permission" : []
        }}

    @list_route(methods=['POST'])
    @Core_connector(transaction=True)
    def logout(self,request):
        Token.objects.filter(userid=request.user.userid).delete()
        return None

    #获取顶层菜单
    @list_route(methods=['GET'])
    @Core_connector()
    def get_menu_top(self,request):

        return {"data" : MenuModelSerializer(Memu.objects.filter(Q(rolecode='all') | Q(rolecode=request.user.rolecode),type=0 ).order_by('parentid'),many=True).data}




