# Generated by Django 3.0.8 on 2020-07-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demands', '0002_auto_20200718_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demanda',
            name='data_conclusao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='demanda',
            name='data_efetiva_conclusao',
            field=models.DateField(blank=True, null=True),
        ),
    ]
