# Generated by Django 2.2.6 on 2019-11-04 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_auto_20191104_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Image slider',
                'db_table': 'imageslider',
            },
        ),
        migrations.AlterModelOptions(
            name='realuser',
            options={'verbose_name_plural': 'User'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name_plural': 'Slider'},
        ),
    ]