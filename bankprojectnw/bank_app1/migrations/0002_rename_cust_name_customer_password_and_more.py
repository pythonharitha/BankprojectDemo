# Generated by Django 4.1 on 2022-12-09 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='cust_name',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='phone_no',
            new_name='username',
        ),
    ]
