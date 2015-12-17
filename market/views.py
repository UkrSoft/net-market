from django.contrib.auth import logout
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.utils.translation import gettext as _
from django.core.urlresolvers import reverse

from market.funcs import MagicSql
from market.models import *
from django.shortcuts import get_object_or_404
		
def shops(request, shop_id=None, good_id=None):
    if (shop_id is None):
        args = {'shops' : Shop.objects.all()}
        template = 'market/shops.html'
    else:
        if (good_id is None):
            args = {'shop' : get_object_or_404(Shop, id = shop_id)}
            template = 'market/shop.html'
        else:
            args = {'good' : get_object_or_404(Item, id = good_id)}
            template = 'market/good.html'
    context = RequestContext(request, args)
    return render(request, template, context)

def goods(request, good_id=None):
    if (good_id is None):
        args = {'goods' : Item.objects.all()}
    else:
        args = {'goods': Item.objects.filter(pk = good_id)}
    context = RequestContext(request, args)
    return render(request, 'market/goods.html', context)

def search(request):
    pass

def basket_add(request, good_id):
    return basket(request, good_id, 'add')

def basket_remove(request, good_id):
    return basket(request, good_id, 'remove')

def basket(request, good_id, action=None, quantity=1):
    good = get_object_or_404(Item, pk = good_id)
    user, person, order, payment = get_order_payment(request)
    args = {'order':order, 'payment':payment}

    prev_url = request.GET.get('from', '!nothing!')#TODO
    args = dict(args, **{'next':prev_url})

    if (action == 'add'):
        oi_added = OrderItem.new_order_item(item = good, order = order, quantity = quantity)
        log(user, _('Item was added: ')+oi_added.__str__())

    elif (action == 'remove'):
        oi_removed_str, removed = OrderItem.remove_order_item(item = good, order = order, quantity = quantity)
        log(user, _('Item was deleted: ')+oi_removed_str)
    else:
        raise Http404

    return HttpResponseRedirect(reverse('market:basket'))

def basket_show(request, args={}):
    user, person, order, payment = get_order_payment(request)
    context = RequestContext(request, dict({'order':order, 'payment':payment}, **args))
    return render(request, 'market/basket.html', context)

def compare_add(request, good_id):
    return compare(request, good_id, 'add')

def compare_remove(request, good_id):
    return compare(request, good_id, 'remove')

def compare(request, good_id=None, action=None):
    pass

def compare_show(request):
    pass

def logout_custom(request):
    logout(request)
    return HttpResponseRedirect(reverse('market:index', None, []))

def log(user, message):
    return Logging.add_entry(user, message)

def get_order_payment(request):
    user, person, person_created = Person.get_person_by_request(request)
    log(user, _('Person was created for the current user.'))

    order, order_created, payment = Order.get_order_by_person(person)
    log(user, _('Order was created from the scratch.'))
    return user, person, order, payment