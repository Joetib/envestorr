# Generated by Django 3.2.12 on 2022-07-21 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_portfolio_portfoliostock'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='title',
            field=models.CharField(default='My First Portfolio', help_text='a label to help distinguish this portfolio', max_length=200),
            preserve_default=False,
        ),
    ]
