# Generated by Django 4.0.5 on 2022-06-27 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_index_employeeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='concern',
            field=models.TextField(default='NA'),
        ),
        migrations.AlterField(
            model_name='index',
            name='department',
            field=models.TextField(default='no information'),
        ),
        migrations.AlterField(
            model_name='index',
            name='emailid',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='index',
            name='fullname',
            field=models.CharField(max_length=120),
        ),
    ]
