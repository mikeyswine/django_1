from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from products.models import Product, Inventory


def index(request):
    product_list = Product.objects.order_by('name')
    # template = loader.get_template('products/index.html')
    context = {
        'product_list': product_list
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'products/index.html', context)


def detail(request, product_id):
    return HttpResponse("You're looking at product %s." % product_id)

# Skipping "Raising a 404 error"
# Leaving off on "Back to the detail() view..."



