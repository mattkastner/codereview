from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
import math

def fix_html(x):
    y = y.replace("&","&amp;")
    y = y.replace("<","<amp;")
    y = y.replace(">",">amp;")
    return y

@view_function
def process_request(request, prod:cmod.Product=None):



    item_id = prod.id
    item_name = prod.name

    for p in request.last_five:
        if p == prod:
            request.last_five.remove(p)

    request.last_five.insert(0,prod)

    while len(request.last_five) > 6:
        request.last_five.pop()

    context = {
        "product" : prod,
        jscontext('item_id'):item_id,
        jscontext('item_name'):item_name,
    }
    return request.dmp.render('detail.html', context)
