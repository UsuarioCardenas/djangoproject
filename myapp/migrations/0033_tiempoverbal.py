# Generated by Django 4.2.7 on 2023-12-10 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0032_irregular'),
    ]

    operations = [
        migrations.CreateModel(
            name='tiempoverbal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('past', models.CharField(max_length=50)),
                ('participe', models.CharField(max_length=50)),
                ('gerundio', models.CharField(max_length=50)),
                ('texto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tiempos_verbales', to='myapp.elegirrespuesta')),
            ],
            options={
                'db_table': 'pasado_simple',
            },
        ),
    ]
