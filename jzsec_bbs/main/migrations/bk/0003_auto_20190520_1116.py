# Generated by Django 2.1.7 on 2019-05-20 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190520_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='create_at',
            field=models.IntegerField(default=1558322175, null=True),
        ),
    ]
