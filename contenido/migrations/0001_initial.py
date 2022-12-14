# Generated by Django 4.1.4 on 2022-12-08 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=300)),
                ('imagen', models.ImageField(upload_to='portoflio/images')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
