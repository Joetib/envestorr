# Generated by Django 3.2.12 on 2022-07-10 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_tools', '0002_alter_currency_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='rate',
            field=models.DecimalField(blank=True, decimal_places=10, default=0, max_digits=25),
        ),
    ]