# Generated by Django 2.1.7 on 2019-06-03 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sys_app', '0002_auto_20190529_1536'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ser_version',
            unique_together={('sys_name', 'mod_name')},
        ),
        migrations.AlterUniqueTogether(
            name='ver_repostory',
            unique_together={('sys_name', 'mod_name')},
        ),
    ]
