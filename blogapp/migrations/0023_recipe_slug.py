# Generated by Django 2.2.6 on 2019-11-13 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0022_contactdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
