# Generated by Django 3.2.12 on 2022-06-25 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='is_draft',
            field=models.BooleanField(default=False),
        ),
    ]
