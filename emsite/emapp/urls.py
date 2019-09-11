from django.urls import path

from . import views

app_name = 'emapp'

urlpatterns = [
    path('', views.TransactionList.as_view(), name='trans_list'),
    path('<int:pk>/update', views.TransactionUpdate.as_view(), name='trans_update'),
    path('create', views.TransactionCreate.as_view(), name='trans_create'),

    path('src-create', views.SourceCreate.as_view(), name='src_create'),
]