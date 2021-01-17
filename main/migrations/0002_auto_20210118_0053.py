# Generated by Django 3.1.3 on 2021-01-17 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth', models.DateTimeField(verbose_name='Дата рождения')),
                ('megafaculty', models.CharField(max_length=30, verbose_name='Мегафакультет')),
                ('group', models.CharField(max_length=10, verbose_name='Номер группы')),
                ('info', models.TextField(verbose_name='Дополнительная нформация')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]