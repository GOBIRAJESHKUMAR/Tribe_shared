# Generated by Django 2.0.5 on 2021-03-10 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wholesalers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wholesaler_reg',
            name='lname',
            field=models.CharField(max_length=300),
        ),
    ]
