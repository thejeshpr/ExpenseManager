# Generated by Django 2.2.5 on 2019-09-11 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emapp', '0006_auto_20190911_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='emapp.Category'),
            preserve_default=False,
        ),
    ]