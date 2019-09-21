from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, UpdateView
from django.views.generic.edit import CreateView
from django.db.models import Sum

from . models import Source, Transaction, Category


class Home(ListView):
    model = Transaction
    context_object_name = 'transactions'
    template_name = 'emapp/home.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.all().order_by('-date')[:5]

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['ttl_trans_amt'] = Transaction.objects.aggregate(Sum('amount'))['amount__sum']
        context['tran_cnt'] = Transaction.objects.count()
        context['cat_cnt'] = Category.objects.all().count()
        context['src_cnt'] = Source.objects.all().count()
        context['categories'] = Category.objects.all()[:8]
        context['sources'] = Source.objects.all()[:8]
        context['show_view_all'] = True

        citi_credit = Source.objects.get(name="CITI - CreditCard")
        ktk_credit = Source.objects.get(name="Kotak - CreditCard")
        dbs_svg = Source.objects.get(name="DBS - Saving")
        citi_savings = Source.objects.get(name="CITI - Saving")
        stats = {}
        stats['CITI - CreditCard'] = Transaction.objects.all().filter(src=citi_credit).aggregate(Sum('amount'))['amount__sum']
        stats['Kotak - CreditCard'] = Transaction.objects.all().filter(src=ktk_credit).aggregate(Sum('amount'))['amount__sum']
        stats['DBS - Saving'] = Transaction.objects.all().filter(src=dbs_svg).aggregate(Sum('amount'))['amount__sum']
        stats['CITI - Savings'] = Transaction.objects.all().filter(src=citi_savings).aggregate(Sum('amount'))['amount__sum'] or 0
        context['stats'] = stats

        return context


class TransactionList(ListView):
    model = Transaction
    context_object_name = 'transactions'
    template_name = 'emapp/generic_display.html'
    paginate_by = 25

    def get_queryset(self):
        qs = super().get_queryset()
        cat = self.request.GET.get('cat')
        src = self.request.GET.get('src')
        if cat:
            qs = qs.filter(category=cat)
        if src:
            qs = qs.filter(src=src)
        return qs.all().order_by('-date') 

    def get_context_data(self, **kwargs):
        context = super(TransactionList, self).get_context_data(**kwargs)
        context['show_view_all'] = False
        context['page'] = 'emapp/trans_list.html'
        context['tran_cnt'] = Transaction.objects.all().count()
        return context   


class TransactionUpdate(UpdateView):
    model = Transaction
    fields = ['amount', 'date', 'src', 'typ', 'category', 'desc', 'pending', 'include_in_calcultion']
    template_name = 'emapp/trans_update.html'


class TransactionCreate(CreateView):
    model = Transaction
    fields = ['amount', 'date', 'typ', 'src', 'category', 'desc', 'pending', 'include_in_calcultion']
    template_name = 'emapp/trans_create.html'


class SourceCreate(CreateView):
    model = Source
    fields = ['name', 'src_type']
    template_name = 'emapp/src_create.html'


class SourceUpdate(UpdateView):
    model = Source
    fields = ['name', 'src_type']
    template_name = 'emapp/src_create.html'


class SourceList(ListView):
    model = Source
    context_object_name = "sources"
    template_name = 'emapp/generic_display.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super(SourceList, self).get_context_data(**kwargs)
        context['show_view_all'] = False
        context['page'] = 'emapp/src_list.html'
        context['src_cnt'] = Source.objects.all().count()
        return context


class CategoryCreate(CreateView):
    model = Category
    fields = ['name']
    template_name = 'emapp/cat_create.html'


class CategoryUpdate(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'emapp/cat_create.html'


class CategoryList(ListView):
    model = Category
    context_object_name = "categories"
    template_name = 'emapp/generic_display.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['show_view_all'] = False
        context['page'] = 'emapp/cat_list.html'
        context['cat_cnt'] = Category.objects.all().count()        
        return context