# Generated by Django 3.2.16 on 2022-11-15 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_rename_name_todo_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateField(default='1996-05-26'),
            preserve_default=False,
        ),
    ]