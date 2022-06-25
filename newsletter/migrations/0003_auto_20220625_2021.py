# Generated by Django 3.2.12 on 2022-06-25 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_newsletter_is_draft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletercontact',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='sent_to',
            field=models.ManyToManyField(blank=True, related_name='newsletters', to='newsletter.NewsLeterContact'),
        ),
    ]
