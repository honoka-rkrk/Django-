# Generated by Django 3.0.5 on 2020-04-30 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kakeibo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'カテゴリ', 'verbose_name_plural': 'カテゴリ'},
        ),
        migrations.AlterModelOptions(
            name='kakeibo',
            options={'verbose_name': '家計簿', 'verbose_name_plural': '家計簿'},
        ),
    ]
