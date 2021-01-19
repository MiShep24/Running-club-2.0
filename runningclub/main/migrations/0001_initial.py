# Generated by Django 3.1.3 on 2020-12-03 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('mainText', models.TextField(verbose_name='Описание')),
                ('timeDate', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]
