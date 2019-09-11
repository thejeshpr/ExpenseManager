from django.contrib import admin

from . models import Source, Transaction, Category

class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'src_type',)
    list_filter = ('src_type', )
admin.site.register(Source, SourceAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date', 'src', 'desc', 'category', 'pending',)
    list_filter = ('date', 'pending', 'category')
    list_editable = ('desc', 'category', 'pending')
    search_fields = ('amount', 'desc')
admin.site.register(Transaction, TransactionAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date', 'modified_date')
    search_fields = ('name', )
admin.site.register(Category, CategoryAdmin)
