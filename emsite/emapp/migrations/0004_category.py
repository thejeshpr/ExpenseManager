# Generated by Django 2.2.5 on 2019-09-11 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emapp', '0003_auto_20190908_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Category Name', max_length=50)),
            ],
        ),
    ]
