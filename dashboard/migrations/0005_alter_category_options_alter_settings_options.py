# Generated by Django 4.1.3 on 2022-12-12 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_settings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'Setting', 'verbose_name_plural': 'Settings'},
        ),
    ]