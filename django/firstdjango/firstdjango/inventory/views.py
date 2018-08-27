from django.shortcuts import render
from django.http import Http404
from inventory.models import Item


def index(req):
    items = Item.objects.exclude(amount=4)
    return render(req, 'inventory/index.html', {'items': items})


def item_detail(req, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404('This item does not exist')
    return render(req, 'inventory/show.html', {'item': item, })
