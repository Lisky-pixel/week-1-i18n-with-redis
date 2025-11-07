from django.shortcuts import render
from .models import Produce


def produce_list(request):
    produce_list = Produce.objects.all()
    return render(request, 'farm/produce_list.html', {'produce_list': produce_list})
