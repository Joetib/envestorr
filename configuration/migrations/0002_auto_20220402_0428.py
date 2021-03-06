# Generated by Django 3.2.12 on 2022-04-02 04:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='email',
            field=models.EmailField(default='envestorr@envestorr.com', max_length=254),
        ),
        migrations.AddField(
            model_name='configuration',
            name='facebook_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='configuration',
            name='linkedin_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='configuration',
            name='location',
            field=models.CharField(default='Kumasi', max_length=350),
        ),
        migrations.AddField(
            model_name='configuration',
            name='phone_number',
            field=models.CharField(default='+2331111111111', help_text='must be 10-15 characters long', max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '024 XXX XXXX'. Up to 10 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AddField(
            model_name='configuration',
            name='twitter_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='configuration',
            name='whatsapp_link',
            field=models.URLField(blank=True),
        ),
    ]
