from django.shortcuts import render

from .forms import ContactForm


def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            print(f'Name: {name}, Phone: {phone}, Message: {message}')
    else:
        form = ContactForm()
    return render(request, 'catalog/contacts.html')
