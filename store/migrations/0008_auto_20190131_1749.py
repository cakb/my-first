# Generated by Django 2.0.2 on 2019-02-01 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_pub_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
    ]