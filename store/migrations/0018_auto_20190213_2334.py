# Generated by Django 2.0.2 on 2019-02-14 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20190212_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mots',
            field=models.TextField(default='general', verbose_name='Mots clés de recherches'),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nom de la catégorie'),
        ),
    ]
