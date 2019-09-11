from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, UpdateView
from django.views.generic.edit import CreateView

from . models import Source, Transaction


class TransactionList(ListView):
    model = Transaction
    context_object_name = 'transactions'
    template_name = 'emapp/trans_list.html'


class TransactionUpdate(UpdateView):
    model = Transaction
    fields = ['amount', 'date', 'src', 'category', 'desc', 'pending']
    template_name = 'emapp/trans_update.html'


class TransactionCreate(CreateView):
    model = Transaction
    fields = ['amount', 'date', 'src', 'category', 'desc', 'pending']
    template_name = 'emapp/trans_create.html'


class SourceCreate(CreateView):
    model = Source
    fields = ['name', 'src_type']
    template_name = 'emapp/src_create.html'