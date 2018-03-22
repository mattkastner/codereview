from django.conf import settings
from django_mako_plus import view_function, jscontext
from django.http import HttpResponseRedirect
from catalog import models as cmod
import math

@view_function
def process_request(request, product:cmod.Product=None):
    category_list = cmod.Category.objects.all()
    image_urls = []
    image_urls = product.image_urls()

    for p in request.last_five:
        if product == p:
            request.last_five.remove(p)

    request.last_five.insert(0, product)

    while len(request.last_five) > 6:
        request.last_five.pop()

    if product.TITLE == 'Bulk':
        quantity = product.quantity
    else:
        quantity = 1

    context = {
            # 'cat_name':cat_name,
            'first_img': product.image_url(),
            'image_urls' : image_urls,
            'name': product.name,
            'description': product.description,
            'product':product,
            'title':product.TITLE,
            'quantity': quantity,
            # 'p_id':p_id,
            # jscontext('num_page'):num_pages,
            # jscontext('cat_ids') : cat_id,
            # jscontext('p_ids') : p_id,
            # 'num_pages':num_pages,
    }

    return request.dmp.render('detail.html', context)
