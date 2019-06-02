from rest_framework import (viewsets)

from education.settings import ServerUrl
from apps.user.models import Users,BalList
from utils.exceptions import PubErrorCustom
from apps.public.utils import get_sysparam

class GenericViewSetCustom(viewsets.ViewSet):
    pass
