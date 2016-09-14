from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q


from .models import Bank, State


def index(request):

    if request.POST:
        banks = request.POST.getlist('bankArray[]')

        queries = [Q(name__icontains=bank) for bank in banks]
        query = queries.pop()
        for item in queries:
            query |= item

        filtered_banks = Bank.objects.filter(query)
        data = serializers.serialize('json', filtered_banks)
        request.session['bank_list'] = data
        # RETURNS TO AJAX CALL
        return HttpResponseRedirect(reverse('location'))

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
    serialized_banks = request.session.get('bank_list')
    deserialized_banks = serializers.deserialize("json", serialized_banks)
    bank_list = [bank.object for bank in deserialized_banks]
    context = {
        'bank_list': bank_list
    }
    return render(request, 'location.html', context)


def country(request):
    context = {}
    return render(request, 'country.html', context)


def bank_detail(request):
    pass
