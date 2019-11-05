# Generated by Django 2.2.6 on 2019-11-05 05:27

from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0011_about_about_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
            ],
            options={
                'db_table': 'googlemap',
            },
        ),
    ]
