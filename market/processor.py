# -*- coding:utf-8 -*-
from market.models import *
# from django.conf import settings

def person_data(request):
    args = {}#TODO think over messages output and order creation for the anonymous users
    if hasattr(request, 'user') and request.user.is_authenticated():
        user = request.user
        person = Person.get_person_by_user(user)
        messages = Logging.get_entries(user = user)
        args = dict({'user': user,
                     'person': person,
                     'messages': messages
                    }, **args)
    return args