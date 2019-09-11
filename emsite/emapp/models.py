from django.db import models
from django.urls import reverse

class Source(models.Model):
    SRC_TYPES = (
        ('S', 'Savings Acct'),
        ('C', 'Credit Card')
    )
    name = models.CharField(unique=True, max_length=50)
    src_type = models.TextField(choices=SRC_TYPES, verbose_name="Source Type")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('emapp:trans_list')


class Category(models.Model):    
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, help_text="Category Name")

    class Meta:        
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('emapp:trans_list')


class Transaction(models.Model):
    amount = models.FloatField()
    date = models.DateTimeField()
    src = models.ForeignKey(Source, on_delete=models.CASCADE, related_name="transactions")
    desc = models.CharField(help_text="description", max_length=200)
    # loan = models.BooleanField(help_text="is it loan?")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="transactions")
    pending = models.BooleanField(help_text="is transaction cycle is pending?", default=True)

    def __str__(self):
        return "{} - {}".format(self.amount, self.date)

    def get_absolute_url(self):
        return reverse('emapp:trans_list')
