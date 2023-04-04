# Generated by Django 3.2 on 2023-01-09 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'зарегистрированный пользователь'), ('moderator', 'модератор'), ('admin', 'администратор')], default='user', max_length=50),
        ),
    ]