# Generated by Django 2.2.5 on 2019-09-08 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('src_type', models.TextField(choices=[('S', 'Savings Acct'), ('C', 'Credit Card')], verbose_name='Source Type')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateTimeField()),
                ('desc', models.TextField(help_text='description')),
                ('loan', models.BooleanField(help_text='is it loan?')),
                ('src', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='emapp.Source')),
            ],
        ),
    ]
