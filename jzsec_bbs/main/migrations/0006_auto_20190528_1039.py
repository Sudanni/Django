# Generated by Django 2.1.7 on 2019-05-28 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190523_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='create_at',
            field=models.IntegerField(default=1559011173, null=True),
        ),
    ]
