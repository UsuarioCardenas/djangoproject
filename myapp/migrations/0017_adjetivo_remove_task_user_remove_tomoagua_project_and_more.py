# Generated by Django 4.2.7 on 2023-12-04 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_rename_verbosirregulares_irregular_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adjetivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advetivo', models.CharField(max_length=50)),
                ('comparativo', models.CharField(max_length=50)),
                ('superlativo', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'adjetivo',
            },
        ),
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tomoagua',
            name='project',
        ),
        migrations.DeleteModel(
            name='intentoproyecto',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.DeleteModel(
            name='tomoagua',
        ),
    ]