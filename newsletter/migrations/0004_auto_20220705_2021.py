# Generated by Django 3.2.12 on 2022-07-05 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_auto_20220625_2021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletercontact',
            options={'ordering': ('date_created',), 'verbose_name_plural': 'NewsLetter Contacts'},
        ),
        migrations.RemoveField(
            model_name='newsletercontact',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='newsletercontact',
            name='last_name',
        ),
    ]
