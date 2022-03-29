from django.shortcuts import render
from .forms import SubForm
from .models import *
from django.views.generic import DetailView, ListView


def landing(request):
    name = "EXTRA"
    form = SubForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data['name'])

        new_form = form.save()

    return render(request, 'landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True,
                                                  product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=1)
    products_images_laptops = products_images.filter(product__category__id=2)
    return render(request, 'home.html', locals())


def product(request, product_id):
    product = Product.objects.get(id=product_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'product.html', locals())
