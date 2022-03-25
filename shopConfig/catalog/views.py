from django.shortcuts import render
from .forms import SubForm
from django.views.generic import DetailView, ListView


def home(request):
    name = "EXTRA"
    form = SubForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data['name'])

        new_form = form.save()

    return render(request, 'base.html', locals())
