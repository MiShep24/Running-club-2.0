# Generated by Django 3.1.3 on 2021-01-18 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210118_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.DateTimeField(verbose_name='Дата рождения (DD.MM.YYYY)'),
        ),
    ]
