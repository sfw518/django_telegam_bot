# Generated by Django 3.2.7 on 2022-04-20 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['name'], 'verbose_name': 'Игра', 'verbose_name_plural': 'Города'},
        ),
    ]