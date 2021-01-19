# Generated by Django 3.1.3 on 2021-01-19 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_auto_20210118_1903'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.CreateModel(
            name='RunPosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название тренировки')),
                ('link_post', models.TextField(verbose_name='Ссылка на пост в Strava')),
                ('distance', models.CharField(max_length=15, verbose_name='Дистанция')),
                ('run_time', models.CharField(max_length=20, verbose_name='Итоговое время')),
                ('date_running', models.CharField(max_length=30, verbose_name='Дата тренировки')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
