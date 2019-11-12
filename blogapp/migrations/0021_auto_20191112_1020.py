# Generated by Django 2.2.6 on 2019-11-12 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0020_newsletter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'verbose_name_plural': 'News Letter'},
        ),
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='blogapp.Recipe'),
        ),
    ]
