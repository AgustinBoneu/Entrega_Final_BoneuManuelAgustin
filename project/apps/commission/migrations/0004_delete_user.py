# Generated by Django 4.2.2 on 2023-06-15 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0003_alter_commissions_usf_type_cost_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]