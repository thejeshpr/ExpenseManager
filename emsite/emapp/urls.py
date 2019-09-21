from django.urls import path

from . import views

app_name = 'emapp'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('trans-list', views.TransactionList.as_view(), name='trans_list'),
    path('<int:pk>/update', views.TransactionUpdate.as_view(), name='trans_update'),
    path('create', views.TransactionCreate.as_view(), name='trans_create'),

    path('src-create', views.SourceCreate.as_view(), name='src_create'),
    path('<int:pk>/src-update', views.SourceUpdate.as_view(), name='src_update'),
    path('src-list', views.SourceList.as_view(), name='src_list'),

    path('cat-create', views.CategoryCreate.as_view(), name='cat_create'),
    path('<int:pk>/cat-update', views.CategoryUpdate.as_view(), name='cat_update'),
    path('cat-list', views.CategoryList.as_view(), name='cat_list'),
]