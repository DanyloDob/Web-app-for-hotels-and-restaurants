# Generated by Django 3.1.3 on 2020-12-14 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hot_res_app', '0004_auto_20201214_2051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='is_awailable',
            new_name='is_available',
        ),
    ]