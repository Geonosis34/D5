# Generated by Django 3.2.8 on 2021-10-28 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsmodel',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
