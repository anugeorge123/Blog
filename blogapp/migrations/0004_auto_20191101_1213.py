# Generated by Django 2.2.6 on 2019-11-01 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=70, null=True),
        ),
    ]
