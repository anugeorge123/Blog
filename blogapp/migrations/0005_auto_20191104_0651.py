# Generated by Django 2.2.6 on 2019-11-04 06:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_auto_20191101_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='steps',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]