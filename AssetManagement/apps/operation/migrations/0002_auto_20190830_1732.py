# Generated by Django 2.2.4 on 2019-08-30 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='change',
            old_name='manager_id',
            new_name='manager',
        ),
        migrations.RenameField(
            model_name='change',
            old_name='summit_id',
            new_name='summit_user',
        ),
    ]