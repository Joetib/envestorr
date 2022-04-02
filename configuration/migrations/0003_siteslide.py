# Generated by Django 3.2.12 on 2022-04-02 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0002_auto_20220402_0428'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSlide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leading', models.CharField(help_text='Leading is the text that appears before the slide title', max_length=100)),
                ('title', models.CharField(help_text='The bold part of the slide', max_length=70)),
                ('trailing', models.CharField(help_text='Text below the title', max_length=200)),
                ('picture', models.ImageField(help_text='The slide background picture', upload_to='slides/%Y')),
                ('action_text', models.CharField(help_text='The text that shows inside the slide button', max_length=50)),
                ('action_url', models.URLField(help_text='the link that the button should go to.')),
                ('active', models.BooleanField(default=True, help_text='Tells whether the slide should show on the side.')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]
