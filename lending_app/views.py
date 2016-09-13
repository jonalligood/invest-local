from django.shortcuts import render

from .models import Bank, State


def index(request):
    states = State.objects.all()
    context = {
        'states': states,
    }
    return render(request, 'index.html', context)


def state(request, pk):
    pk = int(pk)
    state = State.objects.get(pk=pk)
    banks = Bank.objects.filter(state=state).order_by('-return_on_equity')
    context = {
        'banks': banks
    }
    return render(request, 'state.html', context)


def location(request):
    context = {}
    return render(request, 'location.html', context)


def country(request):
    context = {}
    return render(request, 'country.html', context)


def bank_detail(request, bank_id):
    bank_id = int(bank_id)
    bank = Bank.objects.get(id=bank_id)
    context = {
        'bank': bank
    }
    return render(request, 'bank_detail.html', context)
