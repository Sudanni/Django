# Generated by Django 2.1.7 on 2019-05-29 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sys_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ser_version',
            name='remark',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ver_repostory',
            name='remark',
            field=models.TextField(null=True),
        ),
    ]
