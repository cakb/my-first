# Generated by Django 2.0.2 on 2019-02-13 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20190212_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='adresse',
            field=models.CharField(max_length=500, verbose_name='Lieu de livraison/références'),
        ),
        migrations.AlterField(
            model_name='pub',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nom de la pub'),
        ),
    ]