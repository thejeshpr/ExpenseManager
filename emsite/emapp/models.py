from django.db import models
from django.urls import reverse


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Source(BaseModel):
    SRC_TYPES = (
        ('S', 'Savings Acct'),
        ('C', 'Credit Card')
    )
    name = models.CharField(unique=True, max_length=50, help_text="Source Name")
    src_type = models.TextField(choices=SRC_TYPES, verbose_name="Source Type", help_text="Source Type")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('emapp:home')


class Category(BaseModel):    
    name = models.CharField(max_length=50, help_text="Category Name", unique=True)    

    class Meta:        
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('emapp:home')


class Transaction(BaseModel):
    TRAN_TYPE = (
        ('CR', 'Credit'),
        ('DB', 'Debit')
    )
    amount = models.FloatField(help_text="Transaction Amount")
    date = models.DateTimeField(help_text="Transaction Date")
    src = models.ForeignKey(Source, on_delete=models.CASCADE, related_name="transactions")    
    desc = models.CharField(help_text="Description", max_length=200, verbose_name="Description")
    typ = models.CharField(choices=TRAN_TYPE, help_text="Transaction Type", max_length=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="transactions")
    pending = models.BooleanField(help_text="Is transaction cycle is pending?", default=True)
    include_in_calcultion = models.BooleanField(help_text="Include in any calculations?", default=True)

    def __str__(self):
        return "{} - {}".format(self.amount, self.date)

    def get_absolute_url(self):
        return reverse('emapp:home')
