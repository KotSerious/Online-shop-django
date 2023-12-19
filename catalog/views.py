from django.shortcuts import render
from catalog.models import Category, Product

from .forms import ContactForm


def homepage(request):
    context = {
        'objects_list': Category.objects.all(),
        'title': 'Категории SeriousStore'
    }
    return render(request, 'catalog/homepage.html', context)


def contacts(request):
    context = {
        'title': 'Контакты SeriousStore'
    }
    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            print(f'Name: {name}, Phone: {phone}, Message: {message}')

    return render(request, 'catalog/contacts.html', context)


def products(request):
    context = {
        'objects_list': Product.objects.all(),
        'title': 'Все товары SeriousStore'
    }
    return render(request, 'catalog/products.html', context)


def category_product(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'objects_list': Product.objects.filter(category_id=pk),
        'title': f'Товары из категории: {category_item.category_name}',
        'image': Product.objects.all(),
    }
    return render(request, 'catalog/products.html', context)


def position(request, pk):
    position_name = Product.objects.get(id=pk)
    context = {
        'objects_list': Product.objects.filter(id=pk),
        'title': f'SeriousStore {position_name.product_name}',
        'image': Product.objects.all()
    }
    return render(request, 'catalog/position.html', context)
