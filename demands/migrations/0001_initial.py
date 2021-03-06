# Generated by Django 3.0.8 on 2020-07-18 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Canal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_canal', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Demandante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_damandante', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Demanda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_solicitacao', models.DateField()),
                ('data_conclusao', models.DateField()),
                ('demanda', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='demandas_photos')),
                ('observacoes', models.TextField()),
                ('data_efetiva_conclusao', models.DateField()),
                ('atribuicao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('canal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='demands.Canal')),
                ('demandante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='demands.Demandante')),
            ],
        ),
    ]
