# Generated by Django 4.0.5 on 2022-06-24 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_remove_index_employeeid'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='employeeid',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
